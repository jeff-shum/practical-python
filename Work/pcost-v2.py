import csv
import sys

def portfolio_cost(filename):
    total = 0
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                total += int(row[1]) * float(row[2])
            except ValueError:
                print('Encountered invalid or missing data. Continuing to next line.')
    return total

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f'Total cost {cost}')

