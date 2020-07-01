import csv

def read_portfolio(filename):
    '''
    Reads a portfolio file into a list of dictionaries with keys
    name, shares, and price
    '''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            holding = {
            'name': row[0],
            'shares': int(row[1]),
            'price': float(row[2])
            }
            portfolio.append(holding)

    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into a dict mapping names to prices.
    '''
    prices = {}
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print('Row contains no data. Continuing to next row')
    return prices

portfolio = read_portfolio('Data/portfolio.csv')
prices = read_prices('Data/prices.csv')

#Calculate total cost of the portfolio
total_cost = 0.0
for holding in portfolio:
    total_cost += holding['shares']*holding['price']
print('Total cost:', total_cost)

#Compute the current value of portfolio
total_value = 0.0
for holding in portfolio:
    total_value += holding['shares']*prices[holding['name']]
print('Total value:', total_value)
print('Gain:', total_value - total_cost)

