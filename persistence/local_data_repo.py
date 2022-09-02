import json
import os
import sys

import pandas as pd
from pandas import DataFrame

from common.exception import StockCommonException

BASE_PATH = os.getcwd()
LOCAL_DATA_PATH = os.path.join(BASE_PATH, "config/datas")


class LocalDataRepo(object):

    @staticmethod
    def read_data(file_name: str, file_type: str = 'json', path=None):
        """
        读取数据
        """
        path = os.path.join(LOCAL_DATA_PATH, file_name)
        if file_type == 'json':
            with open(path, mode='r', encoding='utf-8') as f:
                return json.load(f)
        elif file_type == 'pd':
            return pd.read_excel(path)
        else:
            raise StockCommonException('not support data type')

    @staticmethod
    def write_data(data, file_path, file_type):
        path = os.path.join(LOCAL_DATA_PATH, file_path)
        print(path)
        if file_type == 'json':
            with open(path) as f:
                json.dump(data, f)
        elif file_type == 'pd' and isinstance(data, DataFrame):
            data.to_excel(path)
        else:
            raise StockCommonException('not support data type')

    @staticmethod
    def read_json_2_df(file_name):
        path = os.path.join(LOCAL_DATA_PATH, file_name)
        return pd.read_json(path, encoding='utf-8')
