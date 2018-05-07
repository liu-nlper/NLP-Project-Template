# NLP Project Template

NLP 工程模板，updating...

## 1. 文件组织结构

    .
    ├─configs/          # 存放配置文件
    ├─experiments/      # 存放实验数据、模型等
    ├─nlpmodule/        # nlp模块
    ├─README.md         # README.md
    └─requirements.txt  # 依赖库

## 2. 使用流程

 - 定义数据加载类，位于`nlpmodule.data`;
 - 定义网络结构类，位于`nlpmodule.nn`;
 - 定义模型训练类，位于`nlpmodule.train`;
 - 定义样本预测类，位于`nlpmodule.infer`;
 - 定义配置文件，写入相关实验参数，位于`configs`;

## 3. 主要组件

### 3.1 preprocessing

预处理模块，封装了分词、词性标注；预训练词向量、构建词表等模块。

### 3.2 data

`nlpmodule.data.Dataset`，数据迭代器。

### 3.3 nn

`nlpmodule.nn`，封装了网络模型类，根据需求搭建网络。

### 3.4 train

训练模块，`Dataset`与`model`作为参数，控制模型的训练和模型的保存。

### 3.5 infer

预测模块，`Dataset`与`model`作为输入，用于加载预训练模型，并预测。

### 3.6 metrics

评估模块。

## 参考

 - https://pytorchnlp.readthedocs.io
 - https://github.com/MrGemy95/Tensorflow-Project-Template
 - https://github.com/SpikeKing/DL-Project-Template
