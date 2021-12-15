def double(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1



values = [6, 3, 9, 1, 0, 2]

double(values)
print(values)
