import csv

def read_portfolio(filename):
    '''Reads a portfolio file into a list of tuples'''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        header = next(rows)
        for row in rows:
            holding = {}
            holding['name'] = row[0]
            holding['shares'] = int(row[1])
            holding['price'] = float(row[2])
            portfolio.append(holding)
    return portfolio

def read_prices(filename):
    '''Reads a prices file into a dictionary'''
    prices = {}
    
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                print('Row contains no data. Continuing to next row')
    return prices

def compute(portfolio, prices):
    '''Reads a portfolio list and prices dictionary and computes value of portfolio along with gain/loss'''
    previous = 0.0
    diff = 0.0
    current = 0.0

    for holding in portfolio:
        previous += holding['shares']*holding['price']

        new_price = prices[holding['name']]
        diff += (new_price-holding['price'])*holding['shares']

        current += previous + diff
    return print(f'The value of the portfolio currently is ${current}. The gain/loss on the portfolio is ${diff}')
