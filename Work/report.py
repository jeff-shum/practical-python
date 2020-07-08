import csv

def read_portfolio(filename):
    '''
    Reads a portfolio file into a list of 
    dictionaries with keys name, shares, and price.
    '''
    portfolio = []

    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for rowno, row in enumerate(rows):
            record = dict(zip(headers, row))
            try:
                name = record['name']
                shares = int(record['shares'])
                price = float(record['price'])
            except ValueError:
                print(f'Row {rowno}: Bad row: {row}')
            portfolio.append({
            'name': name,
            'shares': shares,
            'price': price
            })

    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into 
    a dict mapping names to prices.
    '''
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                prices[row[0]] = float(row[1])
            except IndexError:
                pass
    return prices


def make_report(portfolio, prices):
    '''
    Takes a list of stocks and dictionary of prices
    as input and returns a list of tuples containing
    name, shares, price and change.
    '''
    report = []
    for holding in portfolio:
        row = (holding['name'],
        holding['shares'], 
        holding['price'], 
        prices[holding['name']] - holding['price']
        )
        report.append(row)
    return report


def print_report(report):
    '''
    Takes a list-of-tuples report and prints it in
    an easy to read manner.
    '''
    headers = ('Name', 'Shares', 'Price', 'Change')
    print('%10s %10s %10s %10s' % headers)
    print(('-' * 10 + ' ') * len(headers))
    for name, shares, price, change in report:
        print('{:>10s} {:>10d} {:>10.2f} {:>10.2f}'
        .format(name, shares, price, change))
    

def portfolio_report(portfolio_filename, prices_filename):
    '''
    Make a stock report given portfolio and price files.
    '''
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    report = make_report(portfolio,prices)
    print_report(report)
    
portfolio_report('Data/portfolio.csv',
                 'Data/prices.csv')

