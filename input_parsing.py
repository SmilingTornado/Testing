# author:
# assignment:
# description:

def int_input(message, error='Not a number! Please try again'):
    valid = False
    while (valid == False):
        try:
            return int(input(message))
        except ValueError:
            print(error)


def ranged_int_input(min, max, message, error='Incorrect option, try again:'):
    valid = False
    while (valid == False):
        try:
            parsed_input = int(input('%s\nPlease insert a number between %d and %d\n' % (message, min, max)))
            if (parsed_input >= min and parsed_input <= max):
                valid = True
                return parsed_input
            else:
                print(error)
        except ValueError:
            print(error)


def give_options(message, options, error='Incorrect option, try again:'):
    valid = False
    while (valid == False):
        parsed_input = input('%s' % message)
        if (parsed_input in options):
            valid = True
            return parsed_input
        else:
            print(error, end='')
