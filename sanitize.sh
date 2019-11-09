#!/bin/sh

FILES=$(cut -d , -f 1 data/images.csv)

for FILE in $FILES; do
    FILE_PATH="data/images/${FILE}.jpg"
    if [ ! -f "$FILE_PATH" ]; then
        echo "$FILE_PATH"
    fi
done
