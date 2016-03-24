"""
Assessment history parser
File: 'br63trf.nicrt4wb'
"""
from struct import Struct, calcsize
from csv import DictWriter
from sys import stdin, stdout

from layouts import ASSESSMENT_HISTORY_LAYOUT
from util import (construct_layout, get_active_header, get_fields_by_type,
                  are_all_chars, warning)

layout = construct_layout(ASSESSMENT_HISTORY_LAYOUT)
header = get_active_header(ASSESSMENT_HISTORY_LAYOUT)

output_header = ['record_id'] + header
output_header.remove('action_code')
numeric_fields = get_fields_by_type(ASSESSMENT_HISTORY_LAYOUT, 'number')

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
  if row['action_code'] != 'A':
    continue

  # Use full certification year instead of last 2 chars
  if row['year']:
    row['year'] = '20' + row['year']

  # Enforce numeric fields
  for field in numeric_fields:
    try:
      row[field] = int(row[field])
    except ValueError:
      warning('[{0}] Invalid integer conversion of {1} for "{2}"'.format(
          row['parcel_number'], field, row[field]))
      row[field] = 0

  # Construct unique record id from property id + certification year
  row['record_id'] = '{0}{1}'.format(row['parcel_number'], row['year'])

  # Filter out 
  writer.writerow(row)
