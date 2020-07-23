# ticker.py

from follow import follow
import tableformat
import csv

def select_columns(rows, indices):
    for row in rows:
        yield [row[index] for index in indices]

def convert_types(rows, types):
    for row in rows:
        yield [func(val) for func, val in zip(types, row)]

def make_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def parse_stock_data(lines):
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])
    rows = convert_types(rows, [str, float, float])
    rows = make_dicts(rows, ['name', 'price', 'change'])
    return rows

def ticker(portfile, logfile, fmt):
    import report
    portfolio = report.read_portfolio(portfile)
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = (row for row in rows if row['name'] in portfolio)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(['Name', 'Price', 'Change'])
    for row in rows:
        formatter.row( [row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"] ) 

def main(args):
    if len(args) != 4:
        raise SystemExit(f'Usage: {args[0]}: portfoliofile logfile fmt')
    ticker(args[1], args[2], args[3]) 

if __name__ == '__main__':
    import sys
    main(sys.argv)

