# author:
# assignment:
# description:

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
