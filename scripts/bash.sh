#!/bin/sh

data_file='../data/col1.tsv'
block_size=10000
codec='gzip'

echo "Running program..."
echo "BZ2"
python main.py $data_file $block_size 1 bz2
python main.py $data_file $block_size 3 bz2

echo "GZIP"
python main.py $data_file $block_size 1 gzip
python main.py $data_file $block_size 3 gzip


echo "ZLIB"
python main.py $data_file $block_size 1 zlib
python main.py $data_file $block_size 3 zlib




