# Gather input from the user
day = input('Enter a day of the week or 0 to quit: \n')

# Define list of days of the week
dayoftheweek = ['', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'sathurday', 'sunday']

def searchforday(myday):
    number = dayoftheweek.index(myday)
    print('it is the day',number,'of the week \n')

while day != '0':
    theday = day.lower()
    searchforday(theday)
    day = input('Enter a day of the week or 0 to quit: \n')
