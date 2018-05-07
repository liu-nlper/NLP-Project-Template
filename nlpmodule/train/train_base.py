#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    模型训练类: 用于控制模型的训练

    初始化时推荐的参数设置:

        model: 待训练的模型
        dataiter_train: 训练数据迭代器
        dataiter_train: 开发数据迭代器

        path_model: 模型保存路径

        nb_epoch: int, 最大迭代次数
        max_patience: int, 最大耐心值，开发集连续max_patience没有提升，则提前停止训练

        optimizer: str or optimizer对象，用于模型参数的优化

        use_cuda: bool, 是否利用gpu加速

        其他必要的参数...
"""


class Trainer(object):

    def __init__(self, **kwargs):
        for k in kwargs:
            self.__setattr__(k, kwargs[k])

    def fit(self):
        """
        训练模型
        """
        raise NotImplementedError

    def save_model(self):
        """
        保存模型
        """
        raise NotImplementedError

    def set_batch_size(self, batch_size):
        raise NotImplementedError

    def set_max_patience(self, max_patience):
        self.max_patience = max_patience

    def set_learning_rate(self, learning_rate):
        raise NotImplementedError
