#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta


class ToDoContainer(object):
    """
    ToDo項目のリストを保存するクラス
    """

    def __init__(self):
        """
        ToDo項目のリストのインスタンスを初期化する
        """
        self.todos = []

    def __len__(self):
        """
        ToDo項目の数を返す
        :return: Todo項目の数
        """
        return len(self.todos)

    def sort(self):
        """
        ToDoを締切日でソートする
        :return:
        """
        self.todos.sort(key=lambda x: x.duedate)
