# Property Assessments Pipeline
Data pipeline for processing OPA Property Assessment data

Note: This is a work in progress to replace the current FME-based workflow.

## Source files
- `‘br63trf.os13sd’` Properites
- `‘br63trf.buildcod’` Building codes
- `‘br63trf.stcode’` Street codes
- `‘br63trf.offpr’` Off property (owners)
- `‘br63trf.nicrt4wb’` Assessment histories
- `category_codes.csv` Category codes

## Usage
```bash
cat \‘br63trf.os13sd\’ | python properties.py > properties.csv
```
