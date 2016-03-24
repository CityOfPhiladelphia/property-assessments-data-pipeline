PROPERTIES_LAYOUT = [
  {'start': 0,    'end': 9,    'name': 'PARCEL',        'alias': 'parcel_number'},
  {'start': 9,    'end': 34,   'name': 'LOC',           'alias': 'location'},
  {'start': 34,   'end': 59,   'name': 'OWNER1',        'alias': 'owner_1'},
  {'start': 59,   'end': 84,   'name': 'OWNER2',        'alias': 'owner_2'},
  {'start': 84,   'end': 87,   'name': 'CENSUS',        'alias': 'census_tract'},
  {'start': 87,   'end': 96,   'name': 'ZIP',           'alias': 'zip_code'},
  {'start': 96,   'end': 98,   'name': 'WD_GEO',        'alias': 'geographic_ward'},
  {'start': 98,   'end': 103,  'name': 'ST_CD',         'alias': 'street_code'},
  {'start': 103,  'end': 108,  'name': 'HOUSE_NO',      'alias': 'house_number',            'type': 'number'},
  {'start': 108,  'end': 109,  'name': 'SUFF',          'alias': 'suffix'},
  {'start': 109,  'end': 116,  'name': 'UNIT',          'alias': 'unit'},
  {'start': 116,  'end': 118,  'name': 'EXT',           'alias': 'house_extension',         'type': 'number'},
  {'start': 118,  'end': 126,  'name': 'RCD_DT',        'alias': 'recording_date',          'type': 'date'}, # date
  {'start': 126,  'end': 134,  'name': 'SALE_DATE',     'alias': 'sale_date',               'type': 'date'}, # date
  {'start': 134,  'end': 146,  'name': 'SALE_PR',       'alias': 'sale_price',              'type': 'number'}, # money
  {'start': 146,  'end': 147,  'name': 'SALE_TY',       'alias': 'sale_type',               'skip': True}, # excluded
  {'start': 147,  'end': 148,  'name': 'UNF',           'alias': 'unfinished'},
  {'start': 148,  'end': 156,  'name': 'ASSMT_DT',      'alias': 'assessment_date',         'type': 'date'}, # date
  {'start': 156,  'end': 164,  'name': 'MV_DT',         'alias': 'market_value_date',       'type': 'date'}, # date
  {'start': 164,  'end': 176,  'name': 'MV',            'alias': 'market_value',            'type': 'number'}, # money
  {'start': 176,  'end': 186,  'name': 'TX_LND',        'alias': 'taxable_land',            'type': 'number'}, # money
  {'start': 186,  'end': 196,  'name': 'TX_BLDG',       'alias': 'taxable_building',        'type': 'number'}, # money
  {'start': 196,  'end': 206,  'name': 'XMPT_LND',      'alias': 'exempt_land',             'type': 'number'}, # money
  {'start': 206,  'end': 216,  'name': 'XMPT_BLDG',     'alias': 'exempt_building',         'type': 'number'}, # money
  {'start': 216,  'end': 217,  'name': 'CAT_CD',        'alias': 'category_code',           'type': 'number'}, # also category_code_description
  {'start': 217,  'end': 220,  'name': 'XMPT_CD',       'alias': 'exempt_code',             'skip': True}, # excluded
  {'start': 220,  'end': 228,  'name': 'XMPT_DT',       'alias': 'exempt_date',             'skip': True}, # excluded
  {'start': 228,  'end': 233,  'name': 'BLDG_CD',       'alias': 'building_code'},
  {'start': 233,  'end': 238,  'name': 'ZONE',          'alias': 'zoning'},
  {'start': 238,  'end': 244,  'name': 'LND_USE',       'alias': 'land_use',                'skip': True}, # excluded
  {'start': 244,  'end': 246,  'name': 'DES_AREA',      'alias': 'designated_area',         'skip': True}, # excluded
  {'start': 246,  'end': 247,  'name': 'AREA_USE',      'alias': 'area_usage',              'skip': True}, # excluded
  {'start': 247,  'end': 248,  'name': 'SITE_TYP',      'alias': 'site_type'},
  {'start': 248,  'end': 259,  'name': 'FRT',           'alias': 'frontage',                'type': 'number'}, # number
  {'start': 259,  'end': 270,  'name': 'DPT',           'alias': 'depth',                   'type': 'number'}, # number
  {'start': 270,  'end': 271,  'name': 'SHP',           'alias': 'parcel_shape'}, # used to be 'shape'
  {'start': 271,  'end': 282,  'name': 'TOT_AREA',      'alias': 'total_area',              'type': 'number'}, # number
  {'start': 282,  'end': 283,  'name': 'TOP',           'alias': 'topography'},
  {'start': 283,  'end': 284,  'name': 'GRG_TYP',       'alias': 'garage_type'},
  {'start': 284,  'end': 286,  'name': 'GRG_SP',        'alias': 'garage_spaces',           'type': 'number'}, # number
  {'start': 286,  'end': 288,  'name': 'OFF_ST',        'alias': 'off_street_open',         'type': 'number'}, # number
  {'start': 288,  'end': 289,  'name': 'VIEW',          'alias': 'view'}, # is this reserved word in oracle?
  {'start': 289,  'end': 290,  'name': 'OTR_BLDG',      'alias': 'other_building'},
  {'start': 290,  'end': 293,  'name': 'STORIES',       'alias': 'number_stories',          'type': 'number'}, # number
  {'start': 293,  'end': 294,  'name': 'GEN_CONST',     'alias': 'general_construction'},
  {'start': 294,  'end': 295,  'name': 'TYP_DWELL',     'alias': 'type_dwelling'},
  {'start': 295,  'end': 303,  'name': 'DT_EXT_COND',   'alias': 'date_exterior_condition', 'type': 'date'}, # date
  {'start': 303,  'end': 304,  'name': 'EXT_COND',      'alias': 'exterior_condition',      'type': 'number'},
  {'start': 304,  'end': 305,  'name': 'QLT_GRD',       'alias': 'quality_grade',           'type': 'number'},
  {'start': 305,  'end': 309,  'name': 'YR_BUILT',      'alias': 'year_built'},
  {'start': 309,  'end': 310,  'name': 'EST_YR_BUILT',  'alias': 'year_built_estimate'},
  {'start': 310,  'end': 311,  'name': 'FLR_PLAN',      'alias': 'floor_plan',              'skip': True}, # excluded
  {'start': 311,  'end': 314,  'name': 'NO_RM',         'alias': 'number_of_rooms',         'type': 'number'}, # number
  {'start': 314,  'end': 317,  'name': 'NO_BD',         'alias': 'number_of_bedrooms',      'type': 'number'}, # number
  {'start': 317,  'end': 320,  'name': 'NO_BATH',       'alias': 'number_of_bathrooms',     'type': 'number'}, # number
  {'start': 320,  'end': 321,  'name': 'BASMT',         'alias': 'basements'},
  {'start': 321,  'end': 332,  'name': 'BASMT_SQFT',    'alias': 'basement_square_feet',    'skip': True}, # excluded
  {'start': 332,  'end': 334,  'name': 'FIRE',          'alias': 'fireplaces',              'type': 'number'},
  {'start': 334,  'end': 335,  'name': 'TYP_HEAT',      'alias': 'type_heater'},
  {'start': 335,  'end': 336,  'name': 'FUEL',          'alias': 'fuel'},
  {'start': 336,  'end': 337,  'name': 'CNT_AIR',       'alias': 'central_air'},
  {'start': 337,  'end': 338,  'name': 'INT_COND',      'alias': 'interior_condition',      'type': 'number'},
  {'start': 338,  'end': 342,  'name': 'AMTY',          'alias': 'amenity',                 'skip': True}, # excluded
  {'start': 342,  'end': 343,  'name': 'TYP_IMP',       'alias': 'type_improvement',        'skip': True}, # excluded
  {'start': 343,  'end': 344,  'name': 'UTLY',          'alias': 'utility'},
  {'start': 344,  'end': 345,  'name': 'SEW',           'alias': 'sewer'},
  {'start': 345,  'end': 346,  'name': 'SEP_UTS',       'alias': 'separate_utilities'},
  {'start': 346,  'end': 353,  'name': 'TOT_LIV_AREA',  'alias': 'total_livable_area',      'type': 'number'},
  {'start': 353,  'end': 354,  'name': 'OFF_PROP',      'alias': 'off_property_flag',       'skip': True}, # excluded
  {'start': 354,  'end': 361,  'name': 'BK_PG',         'alias': 'book_and_page'},
  {'start': 361,  'end': 376,  'name': 'REG_NO',        'alias': 'registry_number'},
  {'start': 376,  'end': 385,  'name': 'CROSS_REF',     'alias': 'cross_reference'},
  {'start': 385,  'end': 386,  'name': 'END',           'alias': 'end_of_record',           'skip': True}, # excluded
]

BUILDING_CODES_LAYOUT = [
  {'start': 0,   'end': 5,   'name': 'BLDG_CD_BLDGCODE'},
  {'start': 5,   'end': 30,  'name': 'BLDG_CD_DESCRIPTION',   'alias': 'building_code_description'},
  {'start': 30,  'end': 31,  'name': 'BLDG_CD_CATEGORY_CODE'},
  {'start': 31,  'end': 35,  'name': 'BLDG_CD_STATE_CODE',    'alias': 'state_code'},
  {'start': 35,  'end': 42,  'name': 'BLDG_CD_REMASTTALLY'},
  # {'start': 42,  'end': 45,  'name': 'BLDG_CD_NEW_BUILDING_CODE', 'skip': True},
  # {'start': 45,  'end': 48,  'name': 'BLDG_CD_RESERVED_BUILDING_CODE', 'skip': True},
]

OFF_PROPERTY_LAYOUT = [
  {'start': 0,    'end': 9,   'name': 'OFFPROP_ACCTNO'},
  {'start': 9,    'end': 34,  'name': 'OFFPROP_CAREOFNAME', 'alias': 'mailing_care_of'},
  {'start': 34,   'end': 59,  'name': 'OFFPROP_ADDR1',      'alias': 'mailing_address_1'},
  {'start': 59,   'end': 84,  'name': 'OFFPROP_ADDR2',      'alias': 'mailing_address_2'},
  {'start': 84,   'end': 109, 'name': 'OFFPROP_STNAME',     'alias': 'mailing_street'},
  {'start': 109,  'end': 134, 'name': 'OFFPROP_CITYST',     'alias': 'mailing_city_state'},
  {'start': 134,  'end': 143, 'name': 'OFFPROP_ZIPCODE',    'alias': 'mailing_zip'},
]

STREET_CODES_LAYOUT = [
  {'start': 0,   'end': 15,  'name': 'ST_CD_STREETNAME',  'alias': 'street_name'},
  {'start': 15,  'end': 16,  'name': 'ST_CD_DIRECTION',   'alias': 'street_direction'},
  {'start': 16,  'end': 19,  'name': 'ST_CD_DESIGNATION', 'alias': 'street_designation'},
  {'start': 19,  'end': 25,  'name': 'ST_CD_STREETCODE'},
  # {'start': 25,  'end': 27,  'name': 'ST_CD_UNKNOWN_FIELD', 'skip': True},
  # {'start': 27,  'end': 177, 'name': 'ST_CD_RELOC', 'skip': True},
]

ASSESSMENT_HISTORY_LAYOUT = [
  {'start': 0,    'end': 5,    'name': 'STREET_CODE'},
  {'start': 5,    'end': 10,   'name': 'HOUSE_NUMBER'},
  {'start': 10,   'end': 11,   'name': 'SUFFIX'},
  {'start': 11,   'end': 18,   'name': 'UNIT_NUMBER'},
  {'start': 18,   'end': 20,   'name': 'CERT_YEAR'},
  {'start': 20,   'end': 29,   'name': 'ACCOUNT_NUMBER'},
  {'start': 41,   'end': 42,   'name': 'ACTION_CODE'},
  {'start': 229,  'end': 238,  'name': 'CERTIFIED_TAXABLE_LAND'},
  {'start': 238,  'end': 247,  'name': 'CERTIFIED_TAXABLE_BUILD'},
  {'start': 247,  'end': 256,  'name': 'CERTIFIED_EXEMPT_LAND'},
  {'start': 256,  'end': 265,  'name': 'CERTIFIED_EXEMPT_BUILDING'},
  {'start': 265,  'end': 276,  'name': 'MARKET_VALUE'},
]
