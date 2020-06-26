# pcost.py
#
# Exercise 1.27
total = 0

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        lst = line.split(',')
        total += int(lst[1]) * float(lst[2])

print(f'Total cost {total}')

