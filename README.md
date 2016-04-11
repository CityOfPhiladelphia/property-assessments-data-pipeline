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
```bash
cat \'br63trf.os13sd\' | python properties.py > properties.csv
cat \'br63trf.buildcod\' | python building_codes.py > building_codes.csv
cat \'br63trf.stcode\' | python street_codes.py > street_codes.csv
cat \'br63trf.offpr\' | python off_property.py > off_property.csv
cat \'br63trf.nicrt4wb\' | python assessment_history.py > assessment_history.csv
```

To join the lookup tables to the properties table, use
[csvjoin](http://csvkit.readthedocs.org/en/0.9.1/scripts/csvjoin.html):

```bash
cat input/\'br63trf.os13sd\' | python properties.py \
| csvjoin -c building_code - <(cat input/\'br63trf.buildcod\' | python building_codes.py) \
| csvjoin -c street_code - <(cat input/\'br63trf.stcode\' | python street_codes.py) \
| csvjoin -c parcel_number - <(cat input/\'br63trf.offpr\' | python off_property.py) \
| csvcut --not-columns building_code,street_code,parcel_number \
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