#!/bin/bash



if [[ -z "$1" ]]; then
    echo "No input file provided"
    exit 1
fi

if [[ ! -f "$1" ]]; then
    echo "Input file not found"
    exit 1
fi

python3 - <<EOF
import numpy as np

def transform_data(data):
    transformed = []
    for row in data:
        avg = np.mean(row)
        std = np.std(row)
        transformed.append([(num - avg) / std for num in row])
    return transformed

with open("$1", "r") as file:
    lines = file.readlines()[1:] # Skip the first line

data = [[float(num) for num in line.split(',')] for line in lines]
transformed_data = transform_data(data)

with open("transformed_data.txt", "w") as file:
    file.write(str(transformed_data))

EOF

