#!/bin/sh

data_file="../data/col6.tsv"
col="COL6"
block_size=$1

# COL6
echo "BZ2 for $col"
python main.py $data_file $block_size 2 bz2
python main.py $data_file $block_size 3 bz2

echo "GZIP for $col"
python main.py $data_file $block_size 2 gzip
python main.py $data_file $block_size 3 gzip

echo "ZLIB for $col"
python main.py $data_file $block_size 2 zlib
python main.py $data_file $block_size 3 zlib