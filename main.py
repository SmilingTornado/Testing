# author:
# assignment:
# description:

import input_parsing as ip
import option_functions as of

day = ip.ranged_int_input(1, 31, 'Please input the date')
month = ip.ranged_int_input(1, 12, 'Please input the month')
year = ip.ranged_int_input(1900, 2020, 'Please input the year of birth')
choice = ip.give_letter_options('What would you like to do?\n'
                                'a) Show day of the week for date\n'
                                'b) Show the hit songs of the week\n'
                                'q) Quit', ['a', 'b', 'q'])

if choice == 'a':
    of.a_condition(day, month, year)
elif choice == 'b':
    of.b_condition(day, month, year)
else:
    print('Goodbye')
