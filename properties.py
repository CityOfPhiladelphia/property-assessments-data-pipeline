import struct
from csv import DictWriter
from sys import stdin, stdout

layout = '9s 25s 25s 25s 3s 9s 2s 5s 5s 1s 7s 2s 8s 8s 12s 1s 1s 8s 8s 12s 10s 10s 10s 10s 1s 3s 8s 5s 5s 6s 2s 1s 1s 11s 11s 1s 11s 1s 1s 2s 2s 1s 1s 3s 1s 1s 8s 1s 1s 4s 1s 1s 3s 3s 3s 1s 11s 2s 1s 1s 1s 1s 4s 1s 1s 1s 1s 7s 1s 7s 15s 9s 1s'

header = ['PARCEL', 'LOC', 'OWNER1', 'OWNER2', 'CENSUS', 'ZIP', 'WD_GEO', 'ST_CD', 'HOUSE_NO', 'SUFF', 'UNIT', 'EXT', 'RCD_DT', 'SALE_DATE', 'SALE_PR', 'SALE_TY', 'UNF', 'ASSMT_DT', 'MV_DT', 'MV', 'TX_LND', 'TX_BLDG', 'XMPT_LND', 'XMPT_BLDG', 'CAT_CD', 'XMPT_CD', 'XMPT_DT', 'BLDG_CD', 'ZONE', 'LND_USE', 'DES_AREA', 'AREA_USE', 'SITE_TYP', 'FRT', 'DPT', 'SHP', 'TOT_AREA', 'TOP', 'GRG_TYP', 'GRG_SP', 'OFF_ST', 'VIEW_TYP', 'OTR_BLDG', 'STORIES', 'GEN_CONST', 'TYP_DWELL', 'DT_EXT_COND', 'EXT_COND', 'QLT_GRD', 'YR_BUILT', 'EST_YR_BUILT', 'FLR_PLAN', 'NO_RM', 'NO_BD', 'NO_BATH', 'BASMT', 'BASMT_SQFT', 'FIRE', 'TYP_HEAT', 'FUEL', 'CNT_AIR', 'INT_COND', 'AMTY', 'TYP_IMP', 'UTLY', 'SEW', 'SEP_UTS', 'TOT_LIV_AREA', 'OFF_PROP', 'BK_PG', 'REG_NO', 'CROSS_REF', 'END']

# Prepare CSV output to stdout
writer = DictWriter(stdout, fieldnames=header)
writer.writeheader()

parse = struct.Struct(layout).unpack_from

for line in stdin.readlines():
  # Deconstruct fixed-width string
  row = parse(line)

  # Trim whitespace in each field
  row = [field.strip() for field in row]

  # Convert to dict using headers
  row = dict(zip(header, row))

  writer.writerow(row)
