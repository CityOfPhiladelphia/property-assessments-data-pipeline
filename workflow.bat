winscp /command "open %ETL_FTP_USERNAME%:%ETL_FTP_PASSWORD%@%ETL_FTP_HOSTNAME%" "get OPA_Property_CD/* input\"

cat "input\'br63trf.buildcod'" | python building_codes.py > output/building_codes.csv
cat "input\'br63trf.stcod'" | python street_codes.py > output/street_codes.csv
cat "input\'br63trf.offpr'" | python off_property.py > output/off_property.csv
cat "input\'br63trf.os13sd'" | python properties.py > output/properties.csv

cat output/properties.csv | csvjoin -c building_code - output/building_codes.csv \
    | csvjoin -c street_code - output/street_codes.csv \
    | csvjoin -c parcel_number - output/off_property.csv \
    | csvcut -c parcel_number,1:22,category_code_description,building_code,building_code_description,state_code,23:58,63:66,68:73 \
    > output/merged_properties.csv

cp output/merged_properties.csv %ETL_EXTERNAL_TABLE_PATH%

echo "delete from %ETL_REAL_TABLE_NAME%; insert into %ETL_REAL_TABLE_NAME% select * from %ETL_EXTERNAL_TABLE_NAME%"
