export BERT_BASE_DIR=/study/model/chinese_L-12_H-768_A-12
export GLUE_DIR=/study/data
export TRAINED_CLASSIFIER=/study/model/output
export EXP_NAME=kbqa

python run_kbqa.py \
  --task_name=kbqa \
  --do_predict=true \
  --data_dir=$GLUE_DIR/$EXP_NAME \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
  --max_seq_length=128 \
  --output_dir=$TRAINED_CLASSIFIER/$EXP_NAME
