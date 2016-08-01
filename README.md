# Property Assessments Pipeline
Data pipeline for processing OPA Property Assessment data

Note: This is a work in progress to replace the current FME-based workflow.

## Source files
- `'br63trf.os13sd'` Properites
- `'br63trf.buildcod'` Building codes
- `'br63trf.stcode'` Street codes
- `'br63trf.offpr'` Off property (owners)
- `'br63trf.nicrt4wb'` Assessment histories
- `category_codes.csv` Category codes

## Usage

Install this package:

```bash
pip install git+https://github.com/CityOfPhiladelphia/property-assessments-data-pipeline.git
```

Run the pipeline scripts:

```bash
cat \'br63trf.os13sd\' | phl-properties > properties.csv
cat \'br63trf.buildcod\' | phl-building-codes > building_codes.csv
cat \'br63trf.stcode\' | phl-street-codes > street_codes.csv
cat \'br63trf.offpr\' | phl-off-property > off_property.csv
cat \'br63trf.nicrt4wb\' | phl-assessment-history > assessment_history.csv
```

## Merging process (deprecated)
**This merging is no longer necessary; we will use a database view instead**
To join the lookup tables to the properties table, use
[csvjoin](http://csvkit.readthedocs.org/en/0.9.1/scripts/csvjoin.html):

```bash
cat input/\'br63trf.os13sd\' | phl-properties \
| csvjoin -c BLDG_CD,BLDG_CD_BLDGCODE - <(cat input/\'br63trf.buildcod\' | phl-building-codes) \
| csvjoin -c ST_CD,STCODE - <(cat input/\'br63trf.stcode\' | phl-street-codes) \
| csvjoin -c PARCEL,OPARCEL - <(cat input/\'br63trf.offpr\' | phl-off-property) \
| csvcut --not-columns BLDG_CD_BLDGCODE,STCODE,OPARCEL \
> output/merged_properties.csv
```

Alternatively, you can run the [Drakefile](Drakefile) using [drake](https://github.com/Factual/drake).
```bash
drake
```
Set environment variables for `USERNAME`, `PASSWORD`, `SERVER`, and `TABLE` of the
database or pass them to the `drake` command using
`--vars="USERNAME=xx,PASSWORD=xx,SERVER=xx,TABLE=xx"`

![drake workflow](http://i.imgur.com/62xrLKi.png)
