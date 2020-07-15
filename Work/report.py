import csv
import stock
from fileparse import parse_csv

import tableformat

def read_portfolio(filename):
    '''
    Reads a portfolio file into a list of 
    dictionaries with keys name, shares, and price.
    '''
    with open(filename, 'rt') as file:
        portdicts = parse_csv(file, select=['name', 'shares', 'price'], types=[str, int, float])
    portfolio = [ stock.Stock(d['name'], d['shares'], d['price']) for d in portdicts ]
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
    for stock in portfolio:
        row = (stock.name,
        stock.shares, 
        stock.price, 
        prices[stock.name] - stock.price
        )
        report.append(row)
    return report


def print_report(reportdata, formatter):
    '''
    Takes a list-of-tuples report and prints it in
    an easy to read manner.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename):
    '''
    Make a stock report given portfolio and price files.
    '''
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    
    # Create the report data
    report = make_report(portfolio,prices)

    # Print it out
    formatter = tableformat.HTMLTableFormatter()
    print_report(report, formatter)

def main(argv):
    if len(argv) != 3:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile')
    portfile = argv[1]
    pricefile = argv[2]
    portfolio_report(portfile, pricefile)

if __name__ == '__main__':
    import sys
    main(sys.argv)
    

