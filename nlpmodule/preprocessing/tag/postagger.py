#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
    词性标注
"""


class POSTagger(object):

    def __init__(self):
        """
        初始化模型
        """
        print('test import POSTagger...')

    def pos_tag(self, tokens):
        """
        词性标注

        Args:
            tokens: list of str

        Returns:
            token_pos: list(tuple(str, str)), 即(token, pos)
        """
        pass

    def pos_tag_sents(self, sentences):
        """
        对句子进行批量词性标注

        Args:
            sentences: list(list(str)), tokens list

        Returns:
            list(list(tuple(str, str)))
        """
        pass
