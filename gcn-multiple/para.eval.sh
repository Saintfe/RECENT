#!/bin/bash
for i in $(seq 0  12)
do 
bash eval.sh 0  $i 1 test
done
