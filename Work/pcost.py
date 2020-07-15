# pcost.py

import csv
import sys
import report

def portfolio_cost(filename):
    total_cost = 0
    portfolio = report.read_portfolio(filename)
    for stock in portfolio:
        total_cost += stock.cost()
    return total_cost

def main(argv):
    if len(argv) != 2:
        raise SystemExit(f'Usage: {sys.argv[0]} ' 'portfile')
    portfile = argv[1]
    cost = portfolio_cost(portfile)
    print(f'Total cost {cost}')

if __name__ == '__main__':
    import sys
    main(sys.argv)

