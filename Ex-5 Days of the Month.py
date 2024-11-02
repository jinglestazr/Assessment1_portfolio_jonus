# Dictionary with month numbers as keys and days in those months as values

days={1:31,
        2:28,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31}
# Get the month number from the user
month=int(input('Enter the month number (1-12): '))
if 1 <= month <= 12:
# Check if it's February and ask about leap year if needed
    if month==2:
        leap=input('Are you checking for leap year (yes or no): ')

        if leap=='yes':
            print('The month has 29 days')
        else:
            print('The month has 28 days')
# Prints days for months other than February
    else:
        print(f'The month has {days[month]} days')
else:
    print('Please enter a valid number given above')

