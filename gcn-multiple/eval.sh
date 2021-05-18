#!/bin/bash
CUDA_VISIBLE_DEVICES=$1 python eval.py saved_models/$2-$3/ --type_pair_id $2  --dataset $4 > saved_models/$2-$3/results.txt 

