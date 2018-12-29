python main_without_val.py \
    --arch resnet50 \
    --batch-size 64 \
    --lr 0.001 \
    --gpu 0 \
    --pretrained \
    ResNet50/second/data \
    2>&1 | tee train.log
