def ranged_int_input(min, max, message):
    valid = False
    while (valid == False):
        try:
            parsed_input = int(input('%s\nPlease insert a number between %d and %d\n' % (message, min, max)))
            if (parsed_input >= min and parsed_input <= max):
                valid = True
                return parsed_input
            else:
                print('Invalid Input. Please Try again.')
        except:
            print('Invalid Input. Please Try again.')


def give_letter_options(message, options):
    valid = False
    while (valid == False):
        parsed_input = input('%s\n' % message)
        if (parsed_input in options):
            valid = True
            return parsed_input
        else:
            print('Invalid Input. Please Try again.')


def a_condition(day, month, year):
    if month <= 2:
        m = month + 10
        c = int(year / 100)
        y = (year - 1) - (c * 100)
    else:
        m = month - 2
        c = int(year / 100)
        y = year - (c * 100)

    day_integer = (day + int(2.6 * m - 0.2) - (2 * c) + y + int(y / 4) + int(c / 4)) % 7

    if day_integer == 0:
        print('%d/%d/%d was a Sunday' % (day, month, year))
    elif day_integer == 1:
        print('%d/%d/%d was a Monday' % (day, month, year))
    elif day_integer == 2:
        print('%d/%d/%d was a Tuesday' % (day, month, year))
    elif day_integer == 3:
        print('%d/%d/%d was a Wednesday' % (day, month, year))
    elif day_integer == 4:
        print('%d/%d/%d was a Thursday' % (day, month, year))
    elif day_integer == 5:
        print('%d/%d/%d was a Friday' % (day, month, year))
    elif day_integer == 6:
        print('%d/%d/%d was a Saturday' % (day, month, year))


def b_condition(day, month, year):
    print()


day = ranged_int_input(1, 31, 'Please input the date')
month = ranged_int_input(1, 12, 'Please input the month')
year = ranged_int_input(1900, 2020, 'Please input the year of birth')
choice = give_letter_options('What would you like to do?\n'
                             'a) Show day of the week for date\n'
                             'b) Show the hit songs of the week\n'
                             'q) Quit', ['a', 'b', 'q'])

if choice == 'a':
    a_condition(day, month, year)
elif choice == 'b':
    b_condition()
else:
    print('Goodbye')
