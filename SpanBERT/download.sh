#!/bin/bash

mkdir -p local_model/spanbert-large;
cd local_model/spanbert-large;

echo "==> Downloading glove vectors..."
wget https://huggingface.co/SpanBERT/spanbert-large-cased/blob/main/config.json
wget https://huggingface.co/SpanBERT/spanbert-large-cased/blob/main/vocab.txt
wget https://huggingface.co/SpanBERT/spanbert-large-cased/blob/main/pytorch_model.bin

echo "==> Done."

