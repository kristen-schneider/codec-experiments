#!/bin/sh

data_file="../data/col2.tsv"
col="COL2"
block_size=$1

# COL2
echo "BZ2 for $col"
python main.py $data_file $block_size 1 bz2
python main.py $data_file $block_size 3 bz2

echo "GZIP for $col"
python main.py $data_file $block_size 1 gzip
python main.py $data_file $block_size 3 gzip

echo "ZLIB for $col"
python main.py $data_file $block_size 1 zlib
python main.py $data_file $block_size 3 zlib