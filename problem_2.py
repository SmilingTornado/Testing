def missing_digits(n):
    if n>=10:
        diff = int(str(n)[1]) - int(str(n)[0])
        if diff > 1:
            return diff-1 + missing_digits(int(str(n)[1:]))
        else:
            return missing_digits(int(str(n)[1:]))
    else:
        return 0

print(missing_digits(125679))