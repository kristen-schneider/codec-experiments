#!/bin/sh

data_file="../data/col7.tsv"
col="COL7"
block_size=$1

# COL7
echo "BZ2 for $col"
python main.py $data_file $block_size 3 bz2

echo "GZIP for $col"
python main.py $data_file $block_size 3 gzip

echo "ZLIB for $col"
python main.py $data_file $block_size 3 zlib