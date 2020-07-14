import csv
from fileparse import parse_csv

def read_portfolio(filename):
    '''
    Reads a portfolio file into a list of 
    dictionaries with keys name, shares, and price.
    '''
    with open(filename, 'rt') as file:
        portfolio = parse_csv(file, select=['name', 'shares', 'price'], types=[str, int, float])
    return portfolio

def read_prices(filename):
    '''
    Read a CSV file of price data into 
    a dict mapping names to prices.
    '''
    with open(filename, 'rt') as file:
        pricelist = parse_csv(file, has_headers=False, types=[str, float])
    prices = dict(pricelist) 
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

def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')
    portfile = argv[1]
    pricefile = argv[2]
    portfolio_report(portfile, pricefile)

if __name__ == '__main__':
    import sys
    main(sys.argv)
    

