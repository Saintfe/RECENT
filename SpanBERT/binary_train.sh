mkdir saved_models
python code/run_tacred_binary.py --do_train --do_eval --eval_test  \
--data_dir ./dataset/tacred   --model local_model/spanbert-large  \
--train_batch_size 32   --eval_batch_size 32   --num_train_epochs 10  \
--max_seq_length 128   --output_dir saved_models/depot-binary --fp16 

