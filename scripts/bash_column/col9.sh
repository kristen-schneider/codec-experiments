#!/bin/sh

block_size=$1
data_dir=$2
data_file=$data_dir"col9.tsv"
col="COL9"


# COL9
echo "BZ2 for $col"
#python main.py $data_file $block_size 2 bz2 s
python main.py $data_file $block_size 2 bz2 s o
#python main.py $data_file $block_size 3 bz2 s

echo "GZIP for $col"
#python main.py $data_file $block_size 2 gzip s
python main.py $data_file $block_size 2 gzip s o
#python main.py $data_file $block_size 3 gzip s

echo "ZLIB for $col"
#python main.py $data_file $block_size 2 zlib s
python main.py $data_file $block_size 2 zlib s o
#python main.py $data_file $block_size 3 zlib s

echo "FPZIP for $col"
#python main.py $data_file $block_size 2 fpzip n
python main.py $data_file $block_size 2 fpzip n o

echo "ZFPY for $col"
#python main.py $data_file $block_size 1 zfpy n
#python main.py $data_file $block_size 2 zfpy n
python main.py $data_file $block_size 2 zfpy n o

echo "PYZFP for $col"
#python main.py $data_file $block_size 1 pyzfp n
#python main.py $data_file $block_size 2 pyzfp n
python main.py $data_file $block_size 2 pyzfp n o