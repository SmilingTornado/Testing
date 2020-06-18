def big_diff(lists):
    if len(lists) != 1:
        current = lists[0]
        lists = lists[1:]
        previous = big_diff(lists)[0]
        if max(i for i in previous) - min(i for i in previous) > \
                max(i for i in current) - min(i for i in current):
            return [previous]
        else:
            return [current]
    else:
        return lists


my_parameter = [[3, 9], [4, 8], [5, 6], [7, 8], [6, 8], [6, 9]]
print(big_diff(my_parameter))
