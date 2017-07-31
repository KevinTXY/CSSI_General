from random import randint
characters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
'q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0'
'!', '@', '#', '$' ,'%', '&', '*']
length = raw_input("Enter a Password Length: ")
def grabElement(myList):
    index = randint(0,len(myList) - 1)
    return myList[index];
def createPassword(passwordLength,passwordList):
    password = ''
    for letter in range (passwordLength):
        l = grabElement(passwordList)
        password += l
    return password
print "Your Password is " + createPassword(int(length),characters)
