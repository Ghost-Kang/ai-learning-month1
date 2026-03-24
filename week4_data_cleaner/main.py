"""
主入口函数
"""

__author__ = "wangxukang"
__date__ = "2026/03/26"

from data_cleaner.cli import DataCleanerCLI

def main():
    cli = DataCleanerCLI()
    cli.run()


if __name__ == "__main__":
    main()