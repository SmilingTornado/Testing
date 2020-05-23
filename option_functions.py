# author:
# assignment:
# description:

import webbrowser


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
    if len(str(month)) == 1:
        month = "0" + str(month)
    else:
        month = str(month)
    if len(str(day)) == 1:
        day = "0" + str(day)
    else:
        day = str(day)
    date_string = '%d-%s-%s' % (year, month, day)
    url = 'https://www.billboard.com/charts/hot-100/' + date_string
    webbrowser.open(url)
