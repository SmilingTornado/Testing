def align(filename):
    out = {}
    with open(filename, 'r') as file:
        for line in file:
            character = line.split(',')
            alignment = character[2]
            character.pop(2)
            if alignment in out:
                out[alignment].append(character)
            else:
                out[alignment] = [character]
    return out

print(align('Marvel.csv'))