python main_without_val.py \
    --arch resnet50 \
    --gpu 0 \
    --resume checkpoint.pth.tar \
    -t \
    data \
    2>&1 | tee test.log
