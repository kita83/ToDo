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
        """
        self.todos.sort(key=lambda x: x.duedate)

    def __add__(self, item):
        """
        ＋演算子をエミュレートして、ToDo項目を追加する
        :param item:
        """
        self.todos.append(item)
        self.sort()

    def __iadd__(self, item):
        """
        ＋=演算子をエミュレートして、ToDo項目を追加する
        :param item:
        :return: self
        """
        self.__add__(item)
        return self

    def __getitem__(self, idx):
        """
        インデックスアクセスをエミュレートする
        :param idx:
        :return:
        """
        return self.todos[idx]

    def __setitem__(self, idx, item):
        """
        インデックスの代入をエミュレートする
        :param idx:
        :param item:
        """
        self.todos[idx] = item
        self.sort()

    def __delitem__(self, idx):
        """
        インデックスを指定したdelをエミュレートする
        :param idx:
        """
        del self.todos[idx]

    def get_remaining_todos(self):
        """
        終了していないToDo項目をリストとして返す
        :return:
        """
        return [t for t in self.todos if not t.finished]
