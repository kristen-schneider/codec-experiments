#!/bin/sh

block_size=$1
data_dir=$2
data_file=$data_dir"col10.tsv"
col="COL10"

# COL10
echo "BZ2 for $col"
python main.py $data_file $block_size 1 bz2 s
python main.py $data_file $block_size 2 bz2 s
python main.py $data_file $block_size 3 bz2 s

echo "GZIP for $col"
python main.py $data_file $block_size 1 gzip s
python main.py $data_file $block_size 2 gzip s
python main.py $data_file $block_size 3 gzip s

echo "ZLIB for $col"
python main.py $data_file $block_size 1 zlib s
python main.py $data_file $block_size 2 zlib s
python main.py $data_file $block_size 3 zlib s