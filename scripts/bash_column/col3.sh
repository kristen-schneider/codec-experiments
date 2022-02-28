#!/bin/sh

data_file="../data/col3.tsv"
col="COL3"
block_size=$1

# COL4
echo "BZ2 for $col"
python main.py $data_file $block_size 3 bz2

echo "GZIP for $col"
python main.py $data_file $block_size 3 gzip

echo "ZLIB for $col"
python main.py $data_file $block_size 3 zlib