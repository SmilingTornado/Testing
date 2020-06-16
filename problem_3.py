def partials(n, l):
    n = str(n)
    if len(n) <= l:
        max = int(n)
    else:
        max = 0
    for i in range(len(n)):
        if (n[0:i] + n[i + 1:]) != '':
            temp = partials(int(n[0:i] + n[i + 1:]), l)
            if max < temp:
                max = temp
    return max


print(partials(20125, 4))
