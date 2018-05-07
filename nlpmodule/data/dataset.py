#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    数据加载类
"""


class Dataset():

    def __init__(self):
        """
        数据集迭代器对象

        推荐参数设置:
            1. data_ids: list, 数据编号list
            2. 数据对象，可以根据数据编号索引，可以是:
                (1) 数据索引目录，即根据数据编号可以索引到具体数据
                (2) 整个数据集，即存放在内存中的数据对象，例如np.array类型的数据；
                (3) hdf5格式的文件，同样可以根据数据编号进行索引
                注: 若有多个特征，该对象也可以是dict类型.
            3. batch_size: int, batch size
            4. max_len_limit: 该值并不是返回值中的句子最大长度，而是若一个batch中的句子
                有大于此长度，则将长度限制为max_len_limit；否则以batch中的最大长度为max_len
            5. seed: int, shuffle数据时的随机数种子(只需要对data_ids进行shuffle)
        """
        print('test import Dataset...')

    def __iter__(self):
        # TODO reset iter variable
        return self

    def __next__(self):
        pass
