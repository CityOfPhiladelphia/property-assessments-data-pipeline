"""
Assessment history parser
File: 'br63trf.nicrt4wb'
"""
from struct import Struct, calcsize
from csv import DictWriter
from sys import stdin, stdout

from layouts import ASSESSMENT_HISTORY_LAYOUT
from util import construct_layout, get_active_header, are_all_chars

layout = construct_layout(ASSESSMENT_HISTORY_LAYOUT)
header = get_active_header(ASSESSMENT_HISTORY_LAYOUT)

output_header = ['RECORD_ID', 'PROPERTY_ID', 'ACCOUNT_NUMBER', 'CERT_YEAR', 'MARKET_VALUE', 'CERTIFIED_TAXABLE_LAND', 'CERTIFIED_TAXABLE_BUILD', 'CERTIFIED_EXEMPT_LAND', 'CERTIFIED_EXEMPT_BUILDING']
numeric_fields = ['CERTIFIED_TAXABLE_LAND', 'CERTIFIED_TAXABLE_BUILD', 'CERTIFIED_EXEMPT_LAND', 'CERTIFIED_EXEMPT_BUILDING', 'MARKET_VALUE']

# Prepare CSV output to stdout
writer = DictWriter(stdout, fieldnames=output_header, extrasaction='ignore')
writer.writeheader()

parse = Struct(layout).unpack_from
struct_length = calcsize(layout)

for line in stdin.readlines():
  # Decode line
  line = line.decode('ascii', 'ignore')

  # Ensure string length is what deconstructer expects
  if len(line) != struct_length:
    line = '{:<{}s}'.format(line, struct_length)

  # Deconstruct fixed-width string
  row = parse(line)

  # Trim whitespace in each field
  row = [field.strip() for field in row]

  # Convert to dict using header
  row = dict(zip(header, row))

  # Filter out records where action code is not 'A'
  if row['ACTION_CODE'] != 'A':
    continue

  # Use full certification year instead of last 2 chars
  if row['CERT_YEAR']:
    row['CERT_YEAR'] = '20' + row['CERT_YEAR']

  # Enforce numeric fields
  for field in numeric_fields:
    try:
      row[field] = int(row[field])
    except ValueError:
      row[field] = 0

  # Unit numbers should be padded with leading zeros or empty
  if are_all_chars(row['UNIT_NUMBER'], '0'):
    row['UNIT_NUMBER'] = ''
  else:
    row['UNIT_NUMBER'] = row['UNIT_NUMBER'].zfill(7)

  # Construct property id from street code + house number + suffix + unit
  row['PROPERTY_ID'] = '{0}{1}{2}{3}'.format(row['STREET_CODE'], row['HOUSE_NUMBER'], row['SUFFIX'], row['UNIT_NUMBER'])

  # Construct unique record id from property id + certification year
  row['RECORD_ID'] = '{0}{1}'.format(row['PROPERTY_ID'], row['CERT_YEAR'])

  # Filter out 
  writer.writerow(row)
