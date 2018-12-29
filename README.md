# DSFinal
这是数据科学大作业的实现代码。大作业为kaggle上的一个inclass的比赛。赛题链接：https://www.kaggle.com/c/datascience2018

## Highlight
- 单模型 performance比较好

## Requirements
- python3
- pytorch 0.4.0

## Data Distribution
| types | daisy | dandelion | rose | sunflower | tulip |
| :---: | :---: | :-------: | :--: | :-------: | :---: |
| num | 692 | 949 | 714 | 666 | 878 |

测试集一共424张图片。

## Run This Code

### 分割数据集
将数据放在data目录下，运行以下代码

```
python split_train_val.py
```

### 训练
```
CUDA_VISIBLE_DEVICES="0" sh train.sh
```
你可以根据需要使用训练的同时val或不val的代码。

### 测试
```
CUDA_VISIBLE_DEVICES="0" sh test.sh
```

## Improvement
受到[
Few-Example Object Detection with Model Communication](https://arxiv.org/abs/1706.08249)启发，不再区分验证集和训练集，并将测试集中score大于0.9的数据附上fake label，构成新的训练集进行训练。

## Model Zoo
All the files canbe downloaded in [BaiduYun](https://pan.baidu.com/s/1UtdvT4n-F2Pt2feDz2NVig#list/path=%2F), including train.log, test.log, checkpoint, submit file.

| Version | Acc(Pub) | 
| :---: | :---: | 
| model1 | 0.95754 | 
| model2 | 0.96698 | 

