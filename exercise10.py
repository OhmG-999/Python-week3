# declare an empty list and a counter initialised to 0
numberlist = []
total = 0

# ask the user for input until 5 input have been entered
for i in range(5):
    numberlist.append(round(float(input('Enter a number: \n')),2))
    item = numberlist[i]
# add item to the total
    total = total + item

# print the list items
print(numberlist)

# print the average of all list items
final = round(total / len(numberlist),2)
print('The average of the list is: ', final )