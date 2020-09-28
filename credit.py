#CREDIT PROBLEM SET

#MODULES
#Used to check if a file path contains a valid file
from os import path
#Used to generate random numbers
from random import randint

#FUNCTIONS

#Function used to check if a 16 digit number is a valid credit card number, by implementing Luhn's Algorithm
def checkCc(number):
#Splits a string into a list of characters
    number = [char for char in number]
#Takes every second number(Starting from the index 0) to be multiplied
    multers =  number[::2]
#Takes every second number(starting from index -1) to be added at the end
    adders = number[::-2]
    total = 0
#Adds the multers to Total
    for i in range(len(multers)):
        adder = int(multers[i])*2
        if adder < 10:
            total += adder
        else:
#If the multiplied is more than a single digit, the digits are added individually
            adder = [char for char in str(adder)]
            for j in range(len(adder)):
                total += int(adder[j])
#Adds the adders to Total
    for j in range(len(adders)):
        total += int(adders[j])
#Returns the remainder after total is divided by 10 (If 0, the credit card number is valid)
    if total % 10 == 0:
        return 0
    else:
        return total % 10

#Function used to check if an input is an integer
def checkNum(num):
    try:
        int(num)
        return True
    except:
        return False

#Function used to take a credit card number one by one, and convert it into a form which Luhn's algorithm can be applied to
def oneByOne():
    ccNum = []
    length = 1
#Loop used to add numbers to the list one by one
    while length <= 16:
        valid = False
#Validates each input value
        while not valid:
            num = input("Number: ")
            if checkNum(num):
                if len(num) == 1:
                    ccNum.append(num)
                    length += 1
                    valid = True
                else:
                    print("Invalid Input - Enter Again\n")
            else:
                print("Invalid Input - Enter Again\n")
#Returns a string of numbers
    return ''.join(ccNum)


#Function used to check if a file full of creadit card numbers
def readFromFile():
#Takes and validates a file location
    fileLoc = input("File Location: ")
    while not fileLoc.endswith(".txt") or not path.exists(fileLoc) or len(fileLoc) == 0:
        print("File Location does not  exist")
        fileLoc = input("File Location: ")
#Opens the file to read
    file = open(fileLoc, "r")
#Goes through the file, line by line, and tells the user whether or not the content of the line is a valid credit card number
    for line in file:
        if len(line) > 0:
            line = [char for char in line]
            line.pop(-1)
            line = ''.join(line)
            if checkNum(line):
                if len(line) == 16:
                    print("")
                    print(line)
                    validNum = checkCc(line)
                    if validNum == 0:
                        print("This is a VALID Credit Card Number")
                    else:
                        print("This is an INVALID Credit Card Number")
                    print("")
                else:
                    print("")
                    print(line)
                    print("This is an INVALID Credit Card Number\n")
            else:
                print("")
                print(line)
                print("This is an INVALID Credit Card Number\n")


#Function used to generate a series of random valid numbers, then write them to a file or print them
def generateFile():
    goBack = False
    validChoice = False
    writeToFile = True
    while not validChoice:
        print ("Options:\n1 - Add to Existing File\n2 - Create New File\n3 - Print Numbers\n4 - Return to Menu")
        option = input("Option: ")
        if option == "1":
            fileLoc = input("\nEnter File Location: ")
#Validates the file path
            while not fileLoc.endswith(".txt") or not path.exists(fileLoc) or len(fileLoc) == 0:
                print("\nFile Location does not  exist\n")
                fileLoc = input("Enter File Location: ")
#Opens the file to append
            writefile = open(fileLoc, "a")
            validChoice = True
        elif option == "2":
            print("")
            fileLoc = input("Enter New File Location: ")
#Validates the new file name
            while not fileLoc.endswith(".txt") or  len(fileLoc) == 0:
                print("\nFile Location Invalid\n")
                fileLoc = input("Enter File Location: ")
#Opens the file to write (Clears any existing content)
            writefile = open(fileLoc, "w")
            validChoice = True
        elif option == "3":
#If the user selects option 3, the file part of this function is skipped, and instead the valid numbers are printed
            writeToFile = False
            validChoice = True
        elif option == "4":
            goBack = True
            validChoce = True
            print("")
        else:
            print("\nInvalid Option\n")
    if not goBack:
#Takes and validates the number of valid numbers the user wants to be given
        numbers = input("\nNumber of Credit Card Numbers: ")
        print("")
        while not checkNum(numbers) or int(numbers) > 100 or int(numbers) <= 0:
            print("\nInvalid Input\n")
            numbers = input("Number ofCredit Card Numbers: ")
        validnums = []
        numToGo = int(numbers)
#Generates the correct amount of valid numbers
        while numToGo != 0:
            curnum = []
#This method takes the first fifteen digits of the credit card number
            for i in range(15):
                digit = randint(0,9)
                curnum.append(str(digit))
#Then adds a zero to the end
            curnum.append('0')
            checker = ''.join(curnum)
#Then uses the checker function to take the remainder of the Luhn's algorithm calculaation
            enddigit = checkCc(checker)
            if enddigit == 0:
                curnum = ''.join(curnum)
#and if the remainder is not zero, replaces the last digit with 10 minus the remainder
            else:
                curnum[-1] = str(10 - enddigit)
                curnum = ''.join(curnum)
            if curnum not in validnums:
                validnums.append(curnum)
                numToGo -= 1

#If the user chooses to write to a file, the numbers will then be added one by one to the file
        if writeToFile:
            for item in validnums:
                item = item + "\n"
                writefile.write(item)
            print ("\nDone!",numbers,"more valid credit card numbers have been added to",fileLoc,"\n")
#otherwise each number will be printed
        else:
            for item in validnums:
                print(item)
                print("")








#Main Event Loop

cont = True
while cont:
    print("Menu:\n1 - Enter Credit Card Number\n2 - Enter File of Credit Card Numbers\n3 - Generate Valid Credit Card Numbers\n4 - Quit")
    option = input("Option: ")
    print("")
#Iteration used to create a menu system
    if option == "1":
        cont2 = True
        while cont2:
#Second round of iteration to create a sub-menu
            print ("Options:\n1 - Enter Entire Number\n2 - Enter Number Character by Character\n3 - Go Back")
            option2 = input("Option: ")
            print("")
            if option2 == "1":
#Calls the functions above to validate a given credit card number
                validInput = False
                while not validInput:
                    ccnum = input("Credit Card Number: ")
                    if checkNum(ccnum):
                        validInput = True
                    else:
                        print("Invalid Input")
                print("")
                validNum = checkCc(ccnum)
#Returns appropriate messages depending on results from function
                if validNum == 0:
                    print("This is a VALID Credit Card Number")
                else:
                    print("This is an INVALID Credit Card Number")
                print("\n")
                cont2 = False
            elif option2 == "2":
#Uses the functions above to take the number, digit by digit, and then validate it
                ccnum = oneByOne()
                print("")
                validNum = checkCc(ccnum)
#Returns appropriate messages depending on results from function
                if validNum == 0:
                    print("This is a VALID Credit Card Number")
                else:
                    print("This is an INVALID Credit Card Number")
                print("")
                cont2 = False
            elif option2 == "3":
                cont2 = False
            else:
                print("Invalid - Path not found\n")
    elif option == "2":
#Calls functions above to complete tasks depending on user choice
        readFromFile()
    elif option == "3":
        generateFile()
    elif option == "4":
        print("Goodbye!")
        cont = False
    else:
        print("Invalid Input\n")
