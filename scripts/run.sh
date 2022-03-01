#!/bin/sh

data_dir="/home/krsc0813/projects/gwas-compress/gwas_files/columns/"
#data_dir="../data/"
bash_dir="./bash_column/"
block_size=10000

echo "Running experiments..."
bash $bash_dir"col6.sh" $block_size $data_dir
#for col_bash in `ls $bash_dir`
#do
#  echo $col_bash
#  bash $bash_dir$col_bash $block_size $data_dir
#done






