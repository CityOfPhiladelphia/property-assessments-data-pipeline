PROPERTIES_LAYOUT = [
  {'start': 0,    'end': 9,    'source_name': 'PARCEL',        'name': 'parcel_number'},
  {'start': 9,    'end': 34,   'source_name': 'LOC',           'name': 'location'},
  {'start': 34,   'end': 59,   'source_name': 'OWNER1',        'name': 'owner_1'},
  {'start': 59,   'end': 84,   'source_name': 'OWNER2',        'name': 'owner_2'},
  {'start': 84,   'end': 87,   'source_name': 'CENSUS',        'name': 'census_tract'},
  {'start': 87,   'end': 96,   'source_name': 'ZIP',           'name': 'zip_code'},
  {'start': 96,   'end': 98,   'source_name': 'WD_GEO',        'name': 'geographic_ward'},
  {'start': 98,   'end': 103,  'source_name': 'ST_CD',         'name': 'street_code'},
  {'start': 103,  'end': 108,  'source_name': 'HOUSE_NO',      'name': 'house_number',            'type': 'number'},
  {'start': 108,  'end': 109,  'source_name': 'SUFF',          'name': 'suffix'},
  {'start': 109,  'end': 116,  'source_name': 'UNIT',          'name': 'unit'},
  {'start': 116,  'end': 118,  'source_name': 'EXT',           'name': 'house_extension',         'type': 'number'},
  {'start': 118,  'end': 126,  'source_name': 'RCD_DT',        'name': 'recording_date',          'type': 'date'}, # date
  {'start': 126,  'end': 134,  'source_name': 'SALE_DATE',     'name': 'sale_date',               'type': 'date'}, # date
  {'start': 134,  'end': 146,  'source_name': 'SALE_PR',       'name': 'sale_price',              'type': 'number'}, # money
  {'start': 146,  'end': 147,  'source_name': 'SALE_TY',       'name': 'sale_type',               'skip': True}, # excluded
  {'start': 147,  'end': 148,  'source_name': 'UNF',           'name': 'unfinished'},
  {'start': 148,  'end': 156,  'source_name': 'ASSMT_DT',      'name': 'assessment_date',         'type': 'date'}, # date
  {'start': 156,  'end': 164,  'source_name': 'MV_DT',         'name': 'market_value_date',       'type': 'date'}, # date
  {'start': 164,  'end': 176,  'source_name': 'MV',            'name': 'market_value',            'type': 'number'}, # money
  {'start': 176,  'end': 186,  'source_name': 'TX_LND',        'name': 'taxable_land',            'type': 'number'}, # money
  {'start': 186,  'end': 196,  'source_name': 'TX_BLDG',       'name': 'taxable_building',        'type': 'number'}, # money
  {'start': 196,  'end': 206,  'source_name': 'XMPT_LND',      'name': 'exempt_land',             'type': 'number'}, # money
  {'start': 206,  'end': 216,  'source_name': 'XMPT_BLDG',     'name': 'exempt_building',         'type': 'number'}, # money
  {'start': 216,  'end': 217,  'source_name': 'CAT_CD',        'name': 'category_code',           'type': 'number'}, # also category_code_description
  {'start': 217,  'end': 220,  'source_name': 'XMPT_CD',       'name': 'exempt_code',             'skip': True}, # excluded
  {'start': 220,  'end': 228,  'source_name': 'XMPT_DT',       'name': 'exempt_date',             'skip': True}, # excluded
  {'start': 228,  'end': 233,  'source_name': 'BLDG_CD',       'name': 'building_code'},
  {'start': 233,  'end': 238,  'source_name': 'ZONE',          'name': 'zoning'},
  {'start': 238,  'end': 244,  'source_name': 'LND_USE',       'name': 'land_use',                'skip': True}, # excluded
  {'start': 244,  'end': 246,  'source_name': 'DES_AREA',      'name': 'designated_area',         'skip': True}, # excluded
  {'start': 246,  'end': 247,  'source_name': 'AREA_USE',      'name': 'area_usage',              'skip': True}, # excluded
  {'start': 247,  'end': 248,  'source_name': 'SITE_TYP',      'name': 'site_type'},
  {'start': 248,  'end': 259,  'source_name': 'FRT',           'name': 'frontage',                'type': 'number'}, # number
  {'start': 259,  'end': 270,  'source_name': 'DPT',           'name': 'depth',                   'type': 'number'}, # number
  {'start': 270,  'end': 271,  'source_name': 'SHP',           'name': 'parcel_shape'}, # used to be 'shape'
  {'start': 271,  'end': 282,  'source_name': 'TOT_AREA',      'name': 'total_area',              'type': 'number'}, # number
  {'start': 282,  'end': 283,  'source_name': 'TOP',           'name': 'topography'},
  {'start': 283,  'end': 284,  'source_name': 'GRG_TYP',       'name': 'garage_type'},
  {'start': 284,  'end': 286,  'source_name': 'GRG_SP',        'name': 'garage_spaces',           'type': 'number'}, # number
  {'start': 286,  'end': 288,  'source_name': 'OFF_ST',        'name': 'off_street_open',         'type': 'number'}, # number
  {'start': 288,  'end': 289,  'source_name': 'VIEW',          'name': 'view'}, # is this reserved word in oracle?
  {'start': 289,  'end': 290,  'source_name': 'OTR_BLDG',      'name': 'other_building'},
  {'start': 290,  'end': 293,  'source_name': 'STORIES',       'name': 'number_stories',          'type': 'number'}, # number
  {'start': 293,  'end': 294,  'source_name': 'GEN_CONST',     'name': 'general_construction'},
  {'start': 294,  'end': 295,  'source_name': 'TYP_DWELL',     'name': 'type_dwelling'},
  {'start': 295,  'end': 303,  'source_name': 'DT_EXT_COND',   'name': 'date_exterior_condition', 'type': 'date'}, # date
  {'start': 303,  'end': 304,  'source_name': 'EXT_COND',      'name': 'exterior_condition',      'type': 'number'},
  {'start': 304,  'end': 305,  'source_name': 'QLT_GRD',       'name': 'quality_grade',           'type': 'number'},
  {'start': 305,  'end': 309,  'source_name': 'YR_BUILT',      'name': 'year_built'},
  {'start': 309,  'end': 310,  'source_name': 'EST_YR_BUILT',  'name': 'year_built_estimate'},
  {'start': 310,  'end': 311,  'source_name': 'FLR_PLAN',      'name': 'floor_plan',              'skip': True}, # excluded
  {'start': 311,  'end': 314,  'source_name': 'NO_RM',         'name': 'number_of_rooms',         'type': 'number'}, # number
  {'start': 314,  'end': 317,  'source_name': 'NO_BD',         'name': 'number_of_bedrooms',      'type': 'number'}, # number
  {'start': 317,  'end': 320,  'source_name': 'NO_BATH',       'name': 'number_of_bathrooms',     'type': 'number'}, # number
  {'start': 320,  'end': 321,  'source_name': 'BASMT',         'name': 'basements'},
  {'start': 321,  'end': 332,  'source_name': 'BASMT_SQFT',    'name': 'basement_square_feet',    'skip': True}, # excluded
  {'start': 332,  'end': 334,  'source_name': 'FIRE',          'name': 'fireplaces',              'type': 'number'},
  {'start': 334,  'end': 335,  'source_name': 'TYP_HEAT',      'name': 'type_heater'},
  {'start': 335,  'end': 336,  'source_name': 'FUEL',          'name': 'fuel'},
  {'start': 336,  'end': 337,  'source_name': 'CNT_AIR',       'name': 'central_air'},
  {'start': 337,  'end': 338,  'source_name': 'INT_COND',      'name': 'interior_condition',      'type': 'number'},
  {'start': 338,  'end': 342,  'source_name': 'AMTY',          'name': 'amenity',                 'skip': True}, # excluded
  {'start': 342,  'end': 343,  'source_name': 'TYP_IMP',       'name': 'type_improvement',        'skip': True}, # excluded
  {'start': 343,  'end': 344,  'source_name': 'UTLY',          'name': 'utility'},
  {'start': 344,  'end': 345,  'source_name': 'SEW',           'name': 'sewer'},
  {'start': 345,  'end': 346,  'source_name': 'SEP_UTS',       'name': 'separate_utilities'},
  {'start': 346,  'end': 353,  'source_name': 'TOT_LIV_AREA',  'name': 'total_livable_area',      'type': 'number'},
  {'start': 353,  'end': 354,  'source_name': 'OFF_PROP',      'name': 'off_property_flag',       'skip': True}, # excluded
  {'start': 354,  'end': 361,  'source_name': 'BK_PG',         'name': 'book_and_page'},
  {'start': 361,  'end': 376,  'source_name': 'REG_NO',        'name': 'registry_number'},
  {'start': 376,  'end': 385,  'source_name': 'CROSS_REF',     'name': 'cross_reference'},
  {'start': 385,  'end': 386,  'source_name': 'END',           'name': 'end_of_record',           'skip': True}, # excluded
]

BUILDING_CODES_LAYOUT = [
  {'start': 0,   'end': 5,   'source_name': 'BLDG_CD_BLDGCODE',      'name': 'building_code'},
  {'start': 5,   'end': 30,  'source_name': 'BLDG_CD_DESCRIPTION',   'name': 'building_code_description'},
  {'start': 30,  'end': 31,  'source_name': 'BLDG_CD_CATEGORY_CODE', 'name': 'category_code',             'skip': True}, 
  {'start': 31,  'end': 35,  'source_name': 'BLDG_CD_STATE_CODE',    'name': 'state_code'},
  {'start': 35,  'end': 42,  'source_name': 'BLDG_CD_REMASTTALLY',   'name': 'unknown_field',             'skip': True},
  # {'start': 42,  'end': 45,  'source_name': 'BLDG_CD_NEW_BUILDING_CODE', 'skip': True},
  # {'start': 45,  'end': 48,  'source_name': 'BLDG_CD_RESERVED_BUILDING_CODE', 'skip': True},
]

OFF_PROPERTY_LAYOUT = [
  {'start': 0,    'end': 9,   'source_name': 'OFFPROP_ACCTNO',     'name': 'parcel_number'},
  {'start': 9,    'end': 34,  'source_name': 'OFFPROP_CAREOFNAME', 'name': 'mailing_care_of'},
  {'start': 34,   'end': 59,  'source_name': 'OFFPROP_ADDR1',      'name': 'mailing_address_1'},
  {'start': 59,   'end': 84,  'source_name': 'OFFPROP_ADDR2',      'name': 'mailing_address_2'},
  {'start': 84,   'end': 109, 'source_name': 'OFFPROP_STNAME',     'name': 'mailing_street'},
  {'start': 109,  'end': 134, 'source_name': 'OFFPROP_CITYST',     'name': 'mailing_city_state'},
  {'start': 134,  'end': 143, 'source_name': 'OFFPROP_ZIPCODE',    'name': 'mailing_zip'},
]

STREET_CODES_LAYOUT = [
  {'start': 0,   'end': 15,  'source_name': 'ST_CD_STREETNAME',  'name': 'street_name'},
  {'start': 15,  'end': 16,  'source_name': 'ST_CD_DIRECTION',   'name': 'street_direction'},
  {'start': 16,  'end': 19,  'source_name': 'ST_CD_DESIGNATION', 'name': 'street_designation'},
  {'start': 19,  'end': 25,  'source_name': 'ST_CD_STREETCODE',  'name': 'street_code'},
  # {'start': 25,  'end': 27,  'source_name': 'ST_CD_UNKNOWN_FIELD', 'skip': True},
  # {'start': 27,  'end': 177, 'source_name': 'ST_CD_RELOC', 'skip': True},
]

ASSESSMENT_HISTORY_LAYOUT = [
  {'start': 0,    'end': 5,    'source_name': 'STREET_CODE',                'name': 'street_code',      'skip': True},
  {'start': 5,    'end': 10,   'source_name': 'HOUSE_NUMBER',               'name': 'house_number',     'skip': True},
  {'start': 10,   'end': 11,   'source_name': 'SUFFIX',                     'name': 'suffix',           'skip': True},
  {'start': 11,   'end': 18,   'source_name': 'UNIT_NUMBER',                'name': 'unit',             'skip': True},
  {'start': 18,   'end': 20,   'source_name': 'CERT_YEAR',                  'name': 'year'},
  {'start': 20,   'end': 29,   'source_name': 'ACCOUNT_NUMBER',             'name': 'parcel_number'},
  {'start': 41,   'end': 42,   'source_name': 'ACTION_CODE',                'name': 'action_code'},
  {'start': 229,  'end': 238,  'source_name': 'CERTIFIED_TAXABLE_LAND',     'name': 'taxable_land',     'type': 'number'},
  {'start': 238,  'end': 247,  'source_name': 'CERTIFIED_TAXABLE_BUILD',    'name': 'taxable_building', 'type': 'number'},
  {'start': 247,  'end': 256,  'source_name': 'CERTIFIED_EXEMPT_LAND',      'name': 'exempt_land',      'type': 'number'},
  {'start': 256,  'end': 265,  'source_name': 'CERTIFIED_EXEMPT_BUILDING',  'name': 'exempt_building',  'type': 'number'},
  {'start': 265,  'end': 276,  'source_name': 'MARKET_VALUE',               'name': 'market_value',     'type': 'number'},
]
