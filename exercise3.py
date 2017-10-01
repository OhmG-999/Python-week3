# define 2 lists, one for seasons and the other for months
seasons = ['Winter', 'Spring', 'Summer', 'Autumn']
months = ['december','january', 'february','march','april','may','june','july','august','september','october','november']

# gather user input
month = input('Enter a month of the year: \n')
# convert input to lowercase
themonth = month.lower()
result = months.index(themonth)

if (result <= 2):
    print('The season is', seasons[0])
else:
    print('I don\'t recognise this month')

if result > 2 | result <= 5:
    print('The season is', seasons[1])
else:
    print('I don\'t recognise this month')

if result > 5 | result <= 8:
    print('The season is', seasons[2])
else:
    print('I don\'t recognise this month')
    
if result > 8:
    print('The season is', seasons[3])
else:
    print('I don\'t recognise this month')