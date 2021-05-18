mkdir saved_models
python code/run_tacred_multiple.py --do_train --do_eval --eval_test  \
--data_dir ./dataset/tacred/entity_type_restriction   --model local_model/spanbert-large  \
--train_batch_size 32   --eval_batch_size 32   --num_train_epochs 10  \
--max_seq_length 128   --output_dir saved_models/depot-recent-$1 --fp16 \
--type_pair_id $1 

