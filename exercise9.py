# Write a function which finds all the words beginning with “s” in a list
# and prints them out. It also should say how many words it has found beginning with “s”.

mylist = ['fork','switch', 'battery', 'spoon', 'plate', 'sponge', 'glass']

# the function takes the list as an argument
def startingLetter(list):
# counter to keep track of the number of word found
    counter = 0
# loop to iterate through the list
    for item in range(len(list)):
# if an item is found with the letter 's' then it is printed out and the counter increment by 1
        if list[item][0] == 's':
            counter = counter + 1
            print(list[item], '\n')
# print the total number of word found
    print('There is',counter,'word found with the letter \'s\'')

# pass the list to the function
startingLetter(mylist)