# 第四周：data-cleaner 命令行工具

本周主要完成了一个 CSV 数据清洗工具项目，并使用面向对象方式进行了重构，主要包括：

- `DataCleaner`：数据清洗逻辑
- `DataVisualizer`：图表生成
- `HTMLReporter`：报告生成
- `DataCleanerCLI`：命令行流程控制

该项目支持：

- 去重
- 缺失值填充
- 清洗结果导出
- 自动生成图表
- 自动生成 HTML 报告
- 命令行调用
- 基础单元测试

## 基础用法

```bash
python data_cleaner.py input.csv --output clean.csv

python data_cleaner.py input.csv \
  --output clean.csv \
  --remove-duplicates \
  --fill-missing mean \
  --visualize \
  --report report.html

```
- input.csv：输入的原始 CSV 文件
- --output：输出清洗后的 CSV 文件名
- --remove-duplicates：去除重复行
- --fill-missing：缺失值填充策略，可选 mean / median / mode / zero / none
- --visualize：生成数值列图表
- --report：生成 HTML 报告

``` bash

week4_data_cleaner/
├── README.md
├── requirements.txt
├── setup.py
├── main.py
├── data_cleaner/
│   ├── __init__.py
│   ├── cleaner.py
│   ├── visualizer.py
│   ├── reporter.py
│   └── cli.py
├── tests/
│   └── test_cleaner.py
└── examples/
    ├── dirty_data.csv
    └── clean_data.csv

``` 

这是一个更贴近真实开发场景的小型工具型项目，也是本月作品集中完成度较高的项目之一