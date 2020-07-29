from . import stock
from . import fileparse 
from .portfolio import Portfolio
from . import tableformat

def read_portfolio(filename, **opts):
    '''
    Reads a portfolio file into a list of 
    dictionaries with keys name, shares, and price.
    '''
    with open(filename) as lines:
        return Portfolio.from_csv(lines, **opts)

def read_prices(filename, **opts):
    '''
    Read a CSV file of price data into 
    a dict mapping names to prices.
    '''
    with open(filename) as lines:
        return dict(fileparse.parse_csv(lines, types=[str,float], has_headers=False, **opts))

def make_report(portfolio, prices):
    '''
    Takes a list of stocks and dictionary of prices
    as input and returns a list of tuples containing
    name, shares, price and change.
    '''
    rows = []
    for s in portfolio:
        current_price = prices[s.name]
        change = current_price - s.price
        summary = (s.name, s.shares, current_price, change)
        rows.append(summary)
    return rows

def print_report(reportdata, formatter):
    '''
    Takes a list-of-tuples report and prints it in
    an easy to read manner.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    for name, shares, price, change in reportdata:
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)

def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    '''
    Make a stock report given portfolio and price files.
    '''
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    
    # Create the report data
    report = make_report(portfolio,prices)

    # Print it out
    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)

def main(argv):
    if len(argv) != 4:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile pricefile format')
    portfolio_report(argv[1], argv[2], argv[3])

if __name__ == '__main__':
    import sys
    main(sys.argv)
    import logging
    logging.basicConfig(level = logging.DEBUG)

