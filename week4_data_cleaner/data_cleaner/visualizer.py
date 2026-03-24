"""
数据可视化类
功能：
1. 为数值列生成分布图
"""
__author__ = "wangxukang"
__date__ = "2026/03/23"

import os
import pandas as pd
import matplotlib.pyplot as plt

class Visualizer:
    def __init__(self,df:pd.DataFrame,output_dir:str="charts"):
        self.df=df
        self.output_dir=output_dir
        self.chart_path = []


    def generate_histograms(self,max_cols:int = 3)-> list:

        os.makedirs(self.output_dir,exist_ok=True)
        numeric_cols = self.df.select_dtypes(include="number").columns.tolist()
        if not numeric_cols:
            return []

        for col in numeric_cols[:max_cols]:
            output_path = self._save_histogram(col)
            self.chart_path.append(output_path)

        return self.chart_path

    def _save_histogram(self,col:str)->str:
        plt.figure(figsize=(8,5))
        self.df[col].dropna().hist(bins=20)
        plt.title(f"histogram{col}")
        plt.xlabel(col)
        plt.ylabel("count")

        out_path = os.path.join(self.output_dir,f"{col}_hist.png")
        plt.tight_layout()
        plt.savefig(out_path)
        plt.close()
        return out_path