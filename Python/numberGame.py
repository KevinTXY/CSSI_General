from random import randint
number = randint(0,100)
print("I've thought of a number between 0 and 100, try to guess what it is")
guessCounter = 1
while True:
    guess = raw_input("Your Guess: ")
    if (int(guess) > number):
        print "Try Smaller"
    elif (int(guess) < number):
        print "Try larger"
    elif (int(guess) == number):
        break
    else:
        print "error, try again"
    guessCounter += 1
if guessCounter == 1:
    tryGrammar = "try"
else:
    tryGrammar = "tries"
print ("Congratulations, the number was %s and it took you %s %s to guess it!") % (number, guessCounter, tryGrammar)
