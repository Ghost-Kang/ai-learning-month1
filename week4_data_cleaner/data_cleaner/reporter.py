"""
HTML 报告生成类
功能：
1. 输出数据预览
2. 输出统计摘要
3. 输出图表
4. 输出清洗摘要
"""

__autor__ = "wangxukang"
__date__ = "2026/03/23"

import pandas as pd

class HTMLReporter(object):

    def __init__(self,df:pd.DataFrame,summary:dict,chart_paths:list| None=None):
        self.df = df
        self.summary = summary
        self.chart_paths = chart_paths or []

    def generate(self, output_path:str):
        preview_html = self.df.head(10).to_html(index=False, border=1)
        description_html = self.df.describe(include="all").fillna("").to_html(border=1)
        charts_html = self._build_charts_html()

        html = f"""
        <html>
        <head>
            <meta charset="utf-8">
            <title>数据清洗报告</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 40px;
                    line-height: 1.6;
                }}
                h1, h2, h3 {{
                    color: #333;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    margin-bottom: 20px;
                }}
                th, td {{
                    border: 1px solid #ccc;
                    padding: 8px;
                    text-align: left;
                }}
                th {{
                    background-color: #f5f5f5;
                }}
                img {{
                    max-width: 800px;
                    margin-bottom: 20px;
                }}
            </style>
        </head>
        <body>
            <h1>数据清洗分析报告</h1>

            <h2>一、清洗摘要</h2>
            <ul>
                <li>原始行数：{self.summary['original_rows']}</li>
                <li>原始列数：{self.summary['original_columns']}</li>
                <li>清洗后行数：{self.summary['clean_rows']}</li>
                <li>清洗后列数：{self.summary['clean_columns']}</li>
                <li>清洗前缺失值数量：{self.summary['missing_before']}</li>
                <li>清洗后缺失值数量：{self.summary['missing_after']}</li>
                <li>清洗前重复行数量：{self.summary['duplicates_before']}</li>
                <li>清洗后重复行数量：{self.summary['duplicates_after']}</li>
            </ul>

            <h2>二、数据预览（前10行）</h2>
            {preview_html}

            <h2>三、统计摘要</h2>
            {description_html}

            <h2>四、可视化图表</h2>
            {charts_html}
        </body>
        </html>
        """
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(html)

    def _build_charts_html(self):
        if not self.chart_paths:
            return "<p>no charts</p>"

        html_parts = []
        for chart_path in self.chart_paths:
            html_parts.append(f"<h3>{chart_path}</h3><img src=\"{chart_path}\">")
        return "".join(html_parts)