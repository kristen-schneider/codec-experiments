#!/bin/sh

data_file='../data/col1.tsv'
block_size=1000
data_type=1
codec='gzip'

echo "Running program..."
python main.py $data_file $block_size $data_type $codec

