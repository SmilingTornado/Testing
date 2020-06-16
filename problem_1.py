def num_nines(n):
    if n>=10:
        if int(str(n)[0])==9:
            return 1 + num_nines(int(str(n)[1:]))
        else:
            return num_nines(int(str(n)[1:]))
    else:
        if n==9:
            return 1
        else:
            return 0

print(num_nines(9923499))