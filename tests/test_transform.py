import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pandas as pd

from src.etl.transform import clean_dataframe


def test_clean_dataframe_removes_nulls_and_duplicates():
    data = {
        "order_id": [1, 2, 3, 4],
        "product": ["Apple", "Banana", "Apple", "Orange"],
        "amount": [100, 80, 100, None],
        "order_date": ["2023-01-01"] * 4,
    }
    df = pd.DataFrame(data)

    cleaned_df = clean_dataframe(df)

    assert len(cleaned_df) == 2
    assert cleaned_df["product"].tolist() == ["Apple", "Banana"]
