"""
Properties file parser
File: 'br63trf.os13sd'
"""
from struct import Struct
from csv import DictWriter
from sys import stdin, stdout

from layouts import PROPERTIES_LAYOUT
from util import construct_layout, get_active_header, clean_date, are_all_chars

layout = construct_layout(PROPERTIES_LAYOUT)
header = get_active_header(PROPERTIES_LAYOUT)

date_fields = ['ASSMT_DT', 'DT_EXT_COND', 'MV_DT', 'RCD_DT', 'SALE_DATE', 'XMPT_DT']
numeric_fields = ['CENSUS', 'SALE_PR', 'MV', 'TX_LND', 'TX_BLDG', 'XMPT_LND', 'XMPT_BLDG', 'FRT', 'DPT', 'TOT_AREA', 'GRG_SP', 'OFF_ST', 'STORIES', 'NO_RM', 'NO_BD', 'NO_BATH', 'BASMT_SQFT', 'FIRE', 'TOT_LIV_AREA']

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

  # Convert to dict using headers
  row = dict(zip(header, row))

  # Format date fields
  for field in date_fields:
    row[field] = clean_date(row[field])

  # Enforce numeric fields
  for field in numeric_fields:
    try:
      row[field] = int(row[field])
    except ValueError:
      row[field] = 0

  # Strip leading zeros from other non-numeric fields
  for field in ['HOUSE_NO', 'UNIT', 'EXT']:
    row[field] = row[field].lstrip('0')

  # Empty fields of all zeros
  for field in ['YR_BUILT', 'BK_PG']:
    if are_all_chars(row[field], '0'): row[field] = ''

  # Fix math of some fields
  for field in ['TOT_AREA', 'FRT', 'DPT']:
    if row[field] > 0: row[field] /= 100
  for field in ['NO_BATH', 'NO_BD', 'NO_RM', 'STORIES']:
    if row[field] > 0: row[field] /= 10

  writer.writerow(row)
