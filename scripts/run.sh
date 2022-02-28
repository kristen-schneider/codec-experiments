#!/bin/sh

#data_dir="/home/krsc0813/projects/gwas-compress/gwas_files/columns/col1.tsv"
bash_dir="./bash_column/"
block_size=3

echo "Running experiments..."
for col_bash in `ls $bash_dir`
do
  echo $col_bash
  bash $bash_dir$col_bash $block_size
done






