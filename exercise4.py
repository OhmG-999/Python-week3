# define a list of months
months = ['january', 'february','march','april','may','june','july','august','september','october','november','december']

# gather user input
monthnumber = int(input('Enter a month of the year: \n'))

# check if the input a valid input
def isvalidatemonthnumber(number):
    if int(number) > 0 and int(number) <=12:
        return True
    else:
        print('invalid input, make sure it is a number between 1 and 12')
        return False

# search the month associated with the input
def findmonth(number):
    print('The number', number, 'is the month of', months[number - 1].title(),'\n\n')

# use the input in the function
mychoice = isvalidatemonthnumber(monthnumber)

#
while mychoice == True:
    findmonth(monthnumber)
    monthnumber = int(input('Enter a month of the year: \n'))
    mychoice = isvalidatemonthnumber(monthnumber)

print('Goodbye!')
