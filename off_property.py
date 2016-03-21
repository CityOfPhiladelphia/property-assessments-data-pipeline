"""
Off property parser
File: 'br63trf.offpr'
"""
from struct import Struct, calcsize
from csv import DictWriter
from sys import stdin, stdout

layout = '9s 25s 25s 25s 25s 25s 9s'

header = ['OFFPROP_ACCTNO', 'OFFPROP_CAREOFNAME', 'OFFPROP_ADDR1', 'OFFPROP_ADDR2', 'OFFPROP_STNAME', 'OFFPROP_CITYST', 'OFFPROP_ZIPCODE']

# Prepare CSV output to stdout
writer = DictWriter(stdout, fieldnames=header)
writer.writeheader()

parse = Struct(layout).unpack_from
struct_length = calcsize(layout)

for line in stdin.readlines():
  # Ensure string length is what deconstructer expects
  if len(line) != struct_length:
    line = '{:<{}s}'.format(line, struct_length)

  # Deconstruct fixed-width string
  row = parse(line)

  # Trim whitespace in each field
  row = [field.strip() for field in row]

  # Convert to dict using header
  row = dict(zip(header, row))

  writer.writerow(row)
