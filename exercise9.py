# Write a function which finds all the words beginning with “s” in a list
# and prints them out. It also should say how many words it has found beginning with “s”.

mylist = ['switch', 'battery', 'spoon', 'plate', 'sponge', 'glass']

def startingletter(list):
    letter = set('s')
    for item in list:
        if item in letter:
            print(item, '\n')
            list.count()

startingletter(mylist)