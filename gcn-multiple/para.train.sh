#!/bin/bash
for i in $(seq 0 12)  
do 
  echo $i 
  bash train.sh $1 $i 
done 

