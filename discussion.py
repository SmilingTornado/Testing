def big_diff(list):
    if len(list)!=1:
        current = list
        list = list[1:]
        previous = big_diff(list)[0]
        if max(i for i in previous)-min(i for i in previous) > \
                max(i for i in current[0]) - min(i for i in current[0]):
            return [previous]
        else:
            return [current[0]]
    else:
        return [list[0]]

my_parameter = [[3,9],[4,8],[5,6],[7,8],[6,8],[6,9]]
print(big_diff(my_parameter))