#!/bin/sh

data_file='../data/col1.tsv'
block_size=1000

echo "Running column 1. integers."
python integers.py $data_file $block_size

