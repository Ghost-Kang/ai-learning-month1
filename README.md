# AI 学习第一个月作品集

这是我在第一个月进行 Python、数据采集、数据处理、数据分析和工具开发学习时整理的 GitHub 作品集。

## 项目简介

这个仓库整合了我四周的学习成果，按照“基础练习 → 数据采集 → 数据分析 → 工具项目”的路径进行归档与展示。

主要内容包括：

- 第一周：20 个 Python 基础练习题
- 第二周：数据采集与清洗项目
- 第三周：数据分析与可视化项目
- 第四周：data-cleaner 命令行工具项目
- 最终整理：阶段性总结与作品集展示

这个仓库不仅用于保存代码，也用于展示我的阶段性学习成果、项目整理能力以及 GitHub 规范化管理能力。

## 仓库结构

```text
ai-learning-month1/
├── README.md
├── .gitignore
├── requirements.txt
├── LICENSE
├── week1_basic_practice/
├── week2_data_collection/
├── week3_data_analysis/
├── week4_data_cleaner/
└── final_portfolio/

```

## 环境要求

为了正常运行本项目中的脚本、Notebook 和第四周命令行工具，建议使用以下环境：

| 项目 | 版本要求 |
|------|----------|
| Python | 3.10 及以上 |
| pip | 23.0 及以上 |
| Git | 2.30 及以上 |
| Jupyter Notebook | 建议安装 |
| pytest | 建议安装（用于运行第四周测试） |
| 操作系统 | macOS / Windows / Linux |

## 依赖库

本项目主要使用以下 Python 第三方库：

- requests
- beautifulsoup4
- lxml
- pandas
- matplotlib
- openpyxl
- jupyter
- wordcloud
- numpy
- pytest

安装依赖前，请确保本地已经正确安装 Python 和 pip。

## 环境说明

- **第一周** 主要使用 Python 标准库，部分练习会涉及文件读写和正则表达式。
- **第二周** 主要依赖 `requests`、`beautifulsoup4`、`pandas` 等库进行数据采集和清洗。
- **第三周** 主要依赖 `pandas`、`matplotlib`、`wordcloud`、`jupyter` 进行数据分析和可视化。
- **第四周** 的 `data-cleaner` 工具主要依赖 `pandas`、`matplotlib`，测试部分建议安装 `pytest`。

## 推荐环境准备方式

建议使用虚拟环境运行本项目，以避免不同项目之间的依赖冲突。

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

```bash

ai-learning-month1/
├── README.md
├── .gitignore
├── requirements.txt
├── LICENSE
├── week1_basic_practice/
│   ├── README.md
│   ├── warmup/
│   │   ├── info_card.py
│   │   ├── bmi_calculator.py
│   │   ├── shopping_list.py
│   │   ├── temperature_converter.py
│   │   └── password_checker.py
│   ├── file_ops/
│   │   ├── diary_app.py
│   │   ├── score_analyzer.py
│   │   ├── text_deduplicator.py
│   │   ├── config_parser.py
│   │   └── markdown_toc.py
│   ├── data_processing/
│   │   ├── csv_merge.py
│   │   ├── sales_analysis.py
│   │   ├── email_extractor.py
│   │   ├── json_to_csv.py
│   │   └── duplicate_file_checker.py
│   ├── comprehensive/
│   │   ├── weather_fetcher.py
│   │   ├── batch_renamer.py
│   │   ├── word_frequency.py
│   │   ├── countdown_timer.py
│   │   └── expense_tracker.py
│   └── assets/
├── week2_data_collection/
│   ├── README.md
│   ├── main.py
│   ├── scraper.py
│   ├── cleaner.py
│   ├── utils.py
│   ├── config.py
│   ├── requirements.txt
│   └── data/
│       └── douban_top250.csv
├── week3_data_analysis/
│   ├── README.md
│   ├── analysis.ipynb
│   ├── data/
│   │   └── douban_top250.csv
│   └── images/
│       ├── 01_rating_distribution.png
│       ├── 02_year_trend.png
│       ├── 03_director_top10.png
│       └── ...
├── week4_data_cleaner/
│   ├── README.md
│   ├── requirements.txt
│   ├── setup.py
│   ├── data_cleaner.py
│   ├── data_cleaner/
│   │   ├── __init__.py
│   │   ├── cleaner.py
│   │   ├── visualizer.py
│   │   └── reporter.py
│   ├── tests/
│   │   └── test_cleaner.py
│   └── examples/
│       ├── dirty_data.csv
│       └── clean_data.csv
└── final_portfolio/
    ├── README.md
    ├── final_report.md
    └── showcase_images/
