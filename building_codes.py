"""
Building codes parser
File: 'br63trf.buildcod'
"""
from struct import Struct
from csv import DictWriter
from sys import stdin, stdout

layout = '5s 25s 1s 4s 7s'

# Leaves off BLDG_CD_NEW_BUILDING_CODE & BLDG_CD_RESERVED_BUILDING_CODE fields since they're not in every row
header = ['BLDG_CD_BLDGCODE', 'BLDG_CD_DESCRIPTION', 'BLDG_CD_CATEGORY_CODE', 'BLDG_CD_STATE_CODE', 'BLDG_CD_REMASTTALLY']

# Prepare CSV output to stdout
writer = DictWriter(stdout, fieldnames=header)
writer.writeheader()

parse = Struct(layout).unpack_from

for line in stdin.readlines():
  # Deconstruct fixed-width string
  row = parse(line)

  # Trim whitespace in each field
  row = [field.strip() for field in row]

  # Convert to dict using header
  row = dict(zip(header, row))

  # Strip leading zeros from one field
  row['BLDG_CD_REMASTTALLY'] = row['BLDG_CD_REMASTTALLY'].lstrip('0')

  writer.writerow(row)
