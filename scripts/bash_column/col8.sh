#!/bin/sh

data_file="../data/col8.tsv"
col="COL8"
block_size=$1

# COL8
echo "BZ2 for $col"
python main.py $data_file $block_size 3 bz2

echo "GZIP for $col"
python main.py $data_file $block_size 3 gzip

echo "ZLIB for $col"
python main.py $data_file $block_size 3 zlib