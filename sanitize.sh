#!/bin/sh

FILES=$(tail -n +2 "$1" | cut -d , -f 1)

PATTERN=""

for FILE in $FILES; do
    FILE_PATH="data/images/${FILE}.jpg"
    if [ ! -f "$FILE_PATH" ]; then
        echo "File not found: $FILE_PATH" 1>&2
        if [ '' = "$PATTERN" ]
        then
            PATTERN=$FILE
        else
            PATTERN="${PATTERN}|${FILE}"
        fi
    fi
done

set -x

sed -E "/^($PATTERN)/d" "$1"
