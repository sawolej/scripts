#!/bin/bash

# Define output file
output_file="output.js"

# Empty the output file
> $output_file

# Iterate through the text files
for i in {1..13}
do
    # Check if the file exists
    if [[ -f "l$i.txt" ]]
    then
        # Read the data from the text file
        echo -e "export var d$i = \c" >> $output_file
        cat "l$i.txt" >> $output_file
        echo "" >> $output_file
    else
        echo "File l$i.txt not found."
    fi
done

