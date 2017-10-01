# declare a list of city items
cities = ['Madrid', 'Dublin', 'New York', 'Paris', 'London']

# create a menu for user to interact with the list
print('\n Here is the list\n', cities, '\n\n')

print('1. To add an element to the list, enter "A"\n')
print('2. To remove an element from the list, enter "R"\n')
print('3. To replace an element from the list, enter "P"\n')
print('4. To sort the list, enter "S"\n')

# gather user's input
action = input('What would you like to do?: \n')
action.lower()

if action == 'a':
    mycity = input('Enter the name of the city: \n')
    cities.append(mycity)
    print('\n Here is the new list\n', cities, '\n\n')
elif action == 'r':
    mycity = input('Enter the name of the city you want to remove: \n')
    cities.remove(mycity)
    print('\n Here is the new list\n', cities, '\n\n')
elif action == 'p':
    mycity1 = input('Enter the name of the city you want to replace: \n')
    mycity2 = input('Enter the name of the new city: \n')

    myindex = cities.index(mycity1)
    cities.pop(myindex)
    cities.insert(myindex, mycity2)

    print('\n Here is the new list\n', cities, '\n\n')
elif action == 's':
    cities.sort()

    print('\n Here is the new list\n', cities, '\n\n')
else:
    print('I did not understood your choice!')
