import csv

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        try:
            lst = line.split(',')
            total += int(lst[1]) * float(lst[2])

print(f'Total cost {total}')

