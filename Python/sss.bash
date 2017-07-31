#!/bin/bash
# spritz- OPS435 - Assignment 2
# Written by Daniel Ray - December 2016
#
# BASH script to allow reading files in an optimized, customizeable manner.
#
# Usage notes: Accepts one or two arguements. The first argument must be a valid, non-empty file. This file should contain the text that should be "spritzed" through.
# The second argument should be the rate at which to spritz through the file, given in words per minute. This value must be between 100-1000, inclusive.
#
# Usage: spritz filename [speed]
#
# Notes for the assignment: I had to make a choice between attempting to make the k and j functions separate from the spritz loop or opting for a cleaner script.
# I took the choice of making it more functional while also being messier. Therefore, this file uses temporary files it creates to move data between two processes.
# I considered using named pipes for this, but found that they weren't really what I was looking for. The script should exit cleanly and get rid of all temp files
# and extraneous processes. I will try to explain what I've attempted to do throughout.
#  -Daniel Ray, student ID 126524156
#
#This function runs in the background(see where it is invoked) and displays the words in the file
function spritz
{
        #Run for every word in the given file
        for word in `cat $fileName`
        do
                #Store the length of the word and initialize the other two variables
                wordLength=${#word}
                orpIndex=0
                vowelCount=0
                #Run once for each number 1 to the total length of the word
                for position in `seq ${#word}`
                do
                        #Check if the given letter is a vowel
                        if [[ ${word:$((position - 1)):1} =~ [AaEeIiOoUu] ]]
                        then
                                #Set the position of the ORP when a vowel is found
                                if [ $vowelCount -lt 2 ]
                                then
                                        orpIndex=$((position - 1))
                                fi
                                vowelCount=$(($vowelCount + 1))
                        fi

                done
                #Set the cursor offset from the middle of the screen so that the ORP letter will line up with the centre
                tput cup $midLine $(($midCol - orpIndex))
                #Use indexing and escape codes to print the word, with the ORP being printed in red
                echo -en "${word:0:$orpIndex}\e[0;31m${word:$orpIndex:1}\e[0m${word:$(($orpIndex + 1))}"
                #Increment the number stored in the file by 1
                echo "$((`cat spritzWordsDisplayed` + 1))" >spritzWordsDisplayed
                #Sleep for the number of seconds stored in the file
                sleep `cat spritzDelay`
                #Erase the entire middle line to clear room for another word
                tput cup $midLine 0
                tput el
        done
        #Once all words in the file have been displayed, put 1 into the file
        echo "1" >spritzDone
}

#This function simply allows output to STDERR instead of STDOUT easily
function errorEcho
{
        echo "$@" 1>&2
}

#Remove temp files, kill background process, set terminal settings back to default, clear the screen, and output the number of words and time alotted if SIGTERM or SIGKILL is recieved(Ctrl+C)
trap 'wordsDisplayed=`cat spritzWordsDisplayed`;rm spritzDelay spritzDone spritzWordsDisplayed;tput cnorm;kill -9 "$spritzID";stty sane;clear;echo "You read $wordsDisplayed words, taking $((`date +%s` - $startTime)) seconds.";exit' SIGINT SIGTERM

###################ERROR CHECKING##############################
#All the error messages use the errorEcho function to output to STDERR
#Checks for correct number of arguments
if [ $# -lt 1 -o $# -gt 2 ]
then
        errorEcho "Usage: spritz filename [speed]"
        exit 4
#Checks for a non-empty file given as an argument
elif  [ ! -s $1 ]
then
        errorEcho "Usage: spritz filename [speed]"
        exit 1
#Checks that the script is being run from a terminal
elif  [ ! -t 0 ]
then
        errorEcho "spritz must be run from a terminal."
        exit 5
#Checks if there are 2 arguments, performing checks on the second if there are
elif [ $# -eq 2 ]
then
        #Checks that the 2nd argument is an integer
        if ! [[ $2 =~ ^[0-9]+$ ]]
        then
                errorEcho "Speed given must be a positive integer from 100 to 1000."
                exit 2
        #Checks that the 2nd argument is between 100 and 1000 inclusive
        elif [ $2 -lt 100 -o $2 -gt 1000 ]
        then
                errorEcho "Speed given must be a positive integer from 100 to 1000."
                exit 3
        fi
#Checks that the current directory is writeable by this process, as the script requires use of temp files and so will not function if it cannot write
elif [ ! -w . ]
then
        echo "Current directory is not writeable. Script likely will not function. Input Y to continue, or any key to exit."
        read -n 1 errorResponse
        if ! [ $errorResponse = "Y" ]
        then
                exit 6
        fi
fi

##############################VARIABLE & FILE INITIALIZATION################################
#Clears screen, then deletes(if they exist) and creates temporary files to store data
clear
#Stores the signal that the spritz process is done
rm spritzDone 2>/dev/null
touch SpritzDone
#Stores the delay time between words
rm spritzDelay 2>/dev/null
touch spritzDelay
#Stores the count of words displayed
rm spritzWordsDisplayed 2>/dev/null
touch spritzWordsDisplayed
#Stores the name of the target file
fileName=$1
#Stores the initial words per minute
if [ $# -eq 2 ]
then
        wpm=$2
else
        wpm=120
fi
#Uses WPM to generate delay between each word
echo "`echo "scale=20;1 / ($wpm / 60)"|bc`" >spritzDelay
#Stores the total number of columns in the terminal
rightCol=`tput cols`
#Stores the total number of rows in the terminal
bottomLine=`tput lines`
#Stores the horizontal midpoint in the terminal
midLine=$(($bottomLine / 2))
#Stores the vertical midpoint in the terminal
midCol=$(($rightCol / 2))
#Initializes two of the temporary files
echo "0" >spritzWordsDisplayed
echo "0" >spritzDone

#Disables echoing of keypresses, which would interrupt reading
stty -echo
#Makes the cursor invisible
tput civis

##############################FRAME GENERATION##############################################
#Sets the cursor position to 2 columns right of the left border of the terminal, one row above centre
tput cup $((midLine - 1)) 2
#Prints boxes until the midpoint of the terminal is reached
for ((i=2;i<$midCol;i++))
do
        echo -en "═"
done
#Prints a T box in the middle of the terminal(ORP point)
echo -en "╦"
#Continues to print boxes until 2 colimns left of the right border
for ((i=$(($midCol + 1));i<$(($rightCol - 2));i++))
do
        echo -en "═"
done
#Identical to the above, but with the T box flipped, and the actions being done one row below centre
tput cup $((midLine + 1)) 2
for ((i=2;i<$midCol;i++))
do
        echo -en "═"
done
echo -en "╩"
for ((i=$(($midCol + 1));i<$(($rightCol - 2));i++))
do
        echo -en "═"
done

#Prints a heading showing the file being read from, using the filename length to centre the heading
tput cup $((midLine - 2)) $((midCol - (18 + ${#fileName})/2))
echo -n "Reading from file:$fileName"

#Prints the counter showing words per minute aligned to the left and 2 rows below centre
tput cup $((midLine + 2)) 2
echo -n "Current WPM:"
echo -n "$wpm"

###################################MAIN PROCESS#########################################################
#Stores UNIX timestamp before beginning reading
startTime=`date +%s`

#Runs the spritz function in the background. This was the only way I could get both loops to run at the same time. When the function completes, it edits the spritzDone file. The processID of this is stored in spritzID.
spritz &
spritzID=$!

#Loop waiting for input of k or j, and communicating changes to the background spritz function. Exits when the spritzDone file has been edited(so when all words have been read)
while [ `cat spritzDone` -eq 0 ]
do
        #Waits for input of a single letter. Timeout is only neccessary so the script automatically ends without a keypress and doesn't really have to be 1.
        read -s -n 1 -t 1 inputLetter
        #Checks if the input letter is k or j, and adjusts wpm accordingly. Does nothing on any other key.
        case $inputLetter in
        k)      if [ $wpm -lt 1000 ]
                then
                        wpm=$(($wpm + 10))
                fi;;
        j)      if [ $wpm -gt 100 ]
                then
                        wpm=$(($wpm - 10))
                fi;;
        *);;
        esac
        #Recalculates delay between words and writes to file to be used by spritz process
        echo `echo "scale=20; 1 / ($wpm / 60)"|bc` >spritzDelay
        #Updates the visual display of words per minute
        tput cup $(($midLine + 2)) 14
        tput el
        echo -n "$wpm"
done

##################################CLEANUP##############################################################
#Reads count of words from temp file and stores into variable
wordsDisplayed=`cat spritzWordsDisplayed`
#The background spritz process SHOULD end on its own, but this make sure it does
kill -9 "$spritzID"
#Removes temporary files
rm spritzDone spritzDelay spritzWordsDisplayed 2>/dev/null
#Restores terminal to defaults and clears screen
tput cnorm
stty sane
clear
#Outputs read words and time alotted
echo "You read $wordsDisplayed words, taking $((`date +%s` - $startTime)) seconds."
