"""
数据清洗类
功能：
1. 去重
2. 缺失值填充
3. 输出清洗摘要
"""

__author__ = 'wangxukang'
__date__ = '2026-03-23'

import pandas as pd

class DataCleaner:

    def __init__(self, df:pd.DataFrame):
        self.original_df = df.copy()
        self.clean_df = df.copy()
        self.summary = {}


    def remove_duplicate(self):
        self.clean_df = self.clean_df.drop_duplicates()


    def fill_missing_value(self, strategy:str = "none")->None:
        """
          按指定策略填充缺失值
          strategy:
              mean / median / mode / zero / none
          """
        if strategy == "none":
            return

        for column in self.clean_df.columns:
            if self.clean_df[column].isna().sum() == 0:
                continue
            if pd.api.types.is_numeric_dtype(self.clean_df[column]):
                self._fill_numeric_column(column, strategy)
            else:
                self._fill_object_column(column, strategy)



    def _fill_numeric_column(self, col:str, strategy:str):

        if strategy == "mean":
            self.clean_df[col] = self.clean_df[col].fillna(self.clean_df[col].mean())

        elif strategy == "median":
            self.clean_df[col] = self.clean_df[col].fillna(self.clean_df[col].median())

        elif strategy == "mode":
            mode_series = self.clean_df[col].mode()
            if not mode_series.empty:
                self.clean_df[col] = self.clean_df[col].fillna(mode_series.iloc[0])

        elif strategy == "zero":
            self.clean_df[col] = self.clean_df[col].fillna(0)


    def _fill_object_column(self, col:str, strategy:str):
        if strategy in["mean", "median", "mode"]:
            mode_series = self.clean_df[col].mode()
            if not mode_series.empty:
                self.clean_df[col] = self.clean_df[col].fillna(mode_series.iloc[0])
            else:
                self.clean_df[col] = self.clean_df[col].fillna("未知")
        elif strategy == "zero":
            self.clean_df[col] = self.clean_df[col].fillna(0)


    def generate_summary(self)->dict:
        self.summary = {
            "original_rows": self.original_df.shape[0],
            "original_columns": self.original_df.shape[1],
            "clean_rows": self.clean_df.shape[0],
            "clean_columns": self.clean_df.shape[1],
            "missing_before": int(self.original_df.isna().sum().sum()),
            "missing_after": int(self.clean_df.isna().sum().sum()),
            "duplicates_before": int(self.original_df.duplicated().sum()),
            "duplicates_after": int(self.clean_df.duplicated().sum()),

        }
        return self.summary

    def process(self, remove_duplicate:bool=False, fill_missing:str="none"):
        if remove_duplicate:
            self.remove_duplicate()

        self.fill_missing_value(strategy=fill_missing)
        summary = self.generate_summary()
        return self.clean_df, summary