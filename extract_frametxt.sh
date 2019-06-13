python -m sesame.targetid --mode predict \
                            --model_name fn1.7-pretrained-targetid \
                            --raw_input ./txt_data/train.txt

python -m sesame.frameid --mode predict \
                           --model_name fn1.7-pretrained-frameid \
                           --raw_input logs/fn1.7-pretrained-targetid/predicted-targets.conll

python convert_conll_to_txt.py --conll_file ./logs/fn1.7-pretrained-frameid/predicted-frames.conll --out_file ./txt_data/train_frames.txt

python -m sesame.targetid --mode predict \
                            --model_name fn1.7-pretrained-targetid \
                            --raw_input ./txt_data/val.txt

python -m sesame.frameid --mode predict \
                           --model_name fn1.7-pretrained-frameid \
                           --raw_input logs/fn1.7-pretrained-targetid/predicted-targets.conll

python convert_conll_to_txt.py --conll_file ./logs/fn1.7-pretrained-frameid/predicted-frames.conll --out_file ./txt_data/val_frames.txt

python -m sesame.targetid --mode predict \
                            --model_name fn1.7-pretrained-targetid \
                            --raw_input ./txt_data/test.txt

python -m sesame.frameid --mode predict \
                           --model_name fn1.7-pretrained-frameid \
                           --raw_input logs/fn1.7-pretrained-targetid/predicted-targets.conll

python convert_conll_to_txt.py --conll_file ./logs/fn1.7-pretrained-frameid/predicted-frames.conll --out_file ./txt_data/test_frames.txt

python -m sesame.targetid --mode predict \
                            --model_name fn1.7-pretrained-targetid \
                            --raw_input ./txt_data/train_frame_model.txt

python -m sesame.frameid --mode predict \
                           --model_name fn1.7-pretrained-frameid \
                           --raw_input logs/fn1.7-pretrained-targetid/predicted-targets.conll

python convert_conll_to_txt.py --conll_file ./logs/fn1.7-pretrained-frameid/predicted-frames.conll --out_file ./txt_data/train_frame_model_frames.txt