"""
Street codes parser
File: 'br63trf.stcode'
"""
from struct import Struct
from csv import DictWriter
from sys import stdin, stdout

layout = '15s 1s 3s 6s'

# Leave off last 2 cols
header = ['ST_CD_STREETNAME', 'ST_CD_DIRECTION', 'ST_CD_DESIGNATION', 'ST_CD_STREETCODE']

# Prepare CSV output to stdout
writer = DictWriter(stdout, fieldnames=header)
writer.writeheader()

parse = Struct(layout).unpack_from

for line in stdin.readlines():
  # Decode line
  line = line.decode('ascii', 'ignore')

  # Deconstruct fixed-width string
  row = parse(line)

  # Trim whitespace in each field
  row = [field.strip() for field in row]

  # Convert to dict using header
  row = dict(zip(header, row))

  writer.writerow(row)
