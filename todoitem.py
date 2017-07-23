#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta


class ToDoItem(object):
    """
    ToDok項目を保存するクラス
    """

    def __init__(self, title, description, duedate, addeddate=None):
        """
        ToDo項目インスタンスを初期化する
        :param title:
        :param description:
        :param duedate:
        :param addeddate:
        """

        if not addeddate:
            addeddate = datetime.now()
        self.title = title
        self.desciption = description
        self.duedate = duedate
        self.addeddate = addeddate
        self.finished = False
        self.finisheddate = None

    def finish(self, date=None):
        """
        ToDo項目を終了する
        :param date:
        :return:
        """

        self.finished = True
        if not date:
            date = datetime.now()
        self.finisheddate = date

        def __repr__(self):
            """
            ToDo項目の表示形式文字列を作る
            :param self:
            :return:
            """
            return "<ToDoItem {}, {}>".format(self.title, self.duedate.strftime('%Y/%m/%d %H:%M'))
