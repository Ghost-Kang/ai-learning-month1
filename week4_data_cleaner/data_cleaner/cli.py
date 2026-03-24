"""
命令行入口类
功能：
1. 解析命令行参数
2. 调用清洗、可视化、报告模块
"""

__author__ = "wangxukang"
__date__ = "2026/03/23"

import argparse
import os
import pandas as pd

from data_cleaner.cleaner import DataCleaner
from data_cleaner.visualizer import Visualizer
from data_cleaner.reporter import HTMLReporter

class DataCleanerCLI:

    def __init__(self):
        self.args = self.parse_args()

    @staticmethod
    def parse_args():
        parser = argparse.ArgumentParser(description="CSV 数据清洗跟分析工具")
        parser.add_argument("input_file", help="输入的csv文件路径")
        parser.add_argument("--output_file", default= "clean.csv", help="输出清洗后的CSV文件路径")
        parser.add_argument("--remove-duplicates", action= "store_true", help="去除重复行")
        parser.add_argument(
            "--fill-missing",
            choices=['mean', 'median','mode','zero','none'],
            default="none",
            help="缺失值填充方式"
        )
        parser.add_argument("--visualize", action="store_true", help="生成图表")
        parser.add_argument("--report", help="生成 html报告文件路径，例如 report.html")
        return parser.parse_args()

    def run(self):

        if not os.path.exists(self.args.input_file):
            print(f"error:no exist file->{self.args.input_file}")
            return

        df = pd.read_csv(self.args.input_file)

        cleaner = DataCleaner(df)

        cleaned_df, summary = cleaner.process(
            remove_duplicate= self.args.remove_duplicates,
            fill_missing= self.args.fill_missing
        )

        cleaned_df.to_csv(self.args.output_file, index=False, encoding="utf-8-sig")
        print(f"清洗完成，输出文件{self.args.output_file}")

        chart_paths = []
        if self.args.visualize:
            visualizer = Visualizer(cleaned_df, output_dir="charts")
            chart_paths = visualizer.generate_histograms()
            print("图表已生成，目录在：charts")

        if self.args.report:
            reporter = HTMLReporter(cleaned_df,summary, chart_paths)
            reporter.generate(self.args.report)
            print(f"html报告已生成：{self.args.report}")