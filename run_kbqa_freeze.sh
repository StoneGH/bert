export BERT_BASE_DIR=/study/model/chinese_L-12_H-768_A-12
export GLUE_DIR=/study/data
export TRAINED_CLASSIFIER=/study/model/output
export EXP_NAME=kbqa



python freeze_graph.py \
    -bert_model_dir $BERT_BASE_DIR \
    -model_dir $TRAINED_CLASSIFIER/$EXP_NAME \
    -max_seq_len 128 \
    -num_labels 2
