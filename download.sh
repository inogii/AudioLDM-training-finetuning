./hfdownloader -d inogii/audiocaps_compressed -c 10 -s /root/AudioLDM-training-finetuning/data/dataset
./hfdownloader -d inogii/audioldm_checkpoints -c 10 -s /root/AudioLDM-training-finetuning/data/checkpoints
python merge_chunks.py
python tests/validate_dataset_checkpoint.py