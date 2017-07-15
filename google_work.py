#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import password_list
doc_id = password_list.doc_id
credential_path = password_list.credential_path
sheet_name = password_list.sheet_name

class SpreadSheet:
    # コンストラクタで変数を定義（通信など不安定な変数はここで定義しない）
    def __init__(self, doc_id, credential_path, sheet_name) -> None:
        self.__scope = ['https://spreadsheets.google.com/feeds']
        self.__doc_id = doc_id
        self.__path = os.path.expanduser(credential_path)
        self.__sheet = sheet_name
        self.__credentials = None
        self.__client = None
        self.__gfile = None
        pass
        
    def get_all_values(self):
        print('get_all_values')
        self.records = self.worksheet.get_all_values()
        for record in self.records:
            print(record)
        pass

    def update_cell(self, row, col, text):
        print('update_cell')
        self.worksheet = self.__gfile.worksheet(self.__sheet)
        self.worksheet.update_cell(row,col,text)
        pass

    def open(self):
        self.__credentials = ServiceAccountCredentials.from_json_keyfile_name(self.__path, self.__scope)
        self.__client = gspread.authorize(self.__credentials)
        self.__gfile   = self.__client.open_by_key(self.__doc_id)
        print('open')
        pass

    # withで最初に呼ばれる
    def __enter__(self):
        print('enter')
        self.open()
        return self

    def __exit__(self, type, value, traceback):
        print('exit')
        pass

if __name__ == "__main__":
    with SpreadSheet(doc_id, credential_path, sheet_name) as sp:
        sp.update_cell(1, 1, 'hogehoge')
        sp.update_cell(1, 2, 'hahaha')
        print(sp.get_all_values())

