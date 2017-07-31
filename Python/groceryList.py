amount = raw_input("How many groceries do you want?")
print ("Please enter the four grocery items you want")
grocery = []
groceryAmount = []
for i in range(int(amount)):
    grocery.append(raw_input("Item Number " + (str(i + 1)) +": "))
    if grocery[i] == "rutabaga":
        print "rutabagas are dumb"
    groceryAmount.append(raw_input("How Many? "))

def printList(myList, myAmount):
    for index in range(int(amount)):
        print ("%s. %s %s") % ((str(index+1)), myAmount[index], myList[index] )
printList(grocery,groceryAmount)
