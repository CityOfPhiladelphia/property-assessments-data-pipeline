"""
Street codes parser
File: 'br63trf.stcode'
"""
from struct import Struct
from csv import DictWriter
from sys import stdin, stdout

from layouts import STREET_CODES_LAYOUT
from util import construct_layout, get_active_header

layout = construct_layout(STREET_CODES_LAYOUT)
header = get_active_header(STREET_CODES_LAYOUT)

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
