# pcost.py

import csv
import sys
import report

def portfolio_cost(filename):
    portfolio = report.read_portfolio(filename)
    return portfolio.total_cost

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile')
    portfile = argv[1]
    cost = portfolio_cost(portfile)
    print(f'Total cost {cost}')

if __name__ == '__main__':
    import sys
    main(sys.argv)

