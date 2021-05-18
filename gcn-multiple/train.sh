#!/bin/bash

mkdir -p ./saved_models/$2-$1/
python train.py --id $1 --seed 0 --prune_k 1 --type_pair_id $2 --lr 0.3 --no-rnn  --num_epoch 100 --pooling max  --log_step 100 --save_epoch 101 --mlp_layers 2 --pooling_l2 0.003 
