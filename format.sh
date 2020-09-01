#!/bin/bash
./doctojson.py
cd data
for i in *.json;
    do cat $i | python -m json.tool > temp.json
    cat temp.json > $i
done;
rm temp.json