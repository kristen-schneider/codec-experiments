#!/bin/sh

block_size=$1
data_dir=$2
data_file=$data_dir"col4.tsv"
col="COL4"

# COL4
echo "BZ2 for $col"
python main.py $data_file $block_size 3 bz2 s

echo "GZIP for $col"
python main.py $data_file $block_size 3 gzip s

echo "ZLIB for $col"
python main.py $data_file $block_size 3 zlib s