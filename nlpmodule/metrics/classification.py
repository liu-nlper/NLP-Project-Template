#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    分类任务相关的评价指标:
        1. precision_recall_fscore
        2. more ...
"""


def precision_recall_fscore(y_true, y_pred):
    """
    评价p, r, f1值

    Args:
        y_true: list or 1d array, 正确标签
        y_pred: list or 1d array, 预测标签

    Returns:
        f, r, f1: float

    Notes:
        或者根据需求做扩展，例如返回每个类别的p,f,f1等
    """
    print('test import precision_recall_fscore...')
