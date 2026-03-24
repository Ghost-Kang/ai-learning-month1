"""
测试单元
"""

__author__ = 'wangxukang'
__date__ = '2026-03-23'

import pandas as pd
from data_cleaner.cleaner import DataCleaner

def test_remove_duplicate():
    df = pd.DataFrame({
        "name":["A","A","B"],
        "score":[90,90,80]
    })

    cleaner = DataCleaner(df)
    cleaned_df, summary = cleaner.process(remove_duplicate=True,fill_missing="none")
    assert len(cleaned_df) == 2
    assert summary["duplicates_before"] == 1
    assert summary["duplicates_after"] == 0

def test_fill_missing_mean():
    df = pd.DataFrame({
        "score":[100,None,80],
    })

    cleaner = DataCleaner(df)
    cleaned_df, summary = cleaner.process(remove_duplicate=False,fill_missing="mean")

    assert cleaned_df["score"].isna().sum() == 0
    assert summary["missing_before"] == 1
    assert summary["missing_after"] == 0
