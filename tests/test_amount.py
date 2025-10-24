import pandas as pd


def test_amount_non_negative():
    df = pd.read_csv("data/fact/fact_sales.csv")
    assert (df["amount"] >= 0).all()
