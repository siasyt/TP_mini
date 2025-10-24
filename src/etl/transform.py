import pandas as pd

from src.utils.logging_conf import logger


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Starting dataframe cleaning...")

    df_cleaned = df.dropna()
    df_cleaned = df_cleaned.drop_duplicates(subset=["product", "amount", "order_date"])

    logger.info(f"Dataframe cleaned: {len(df)} -> {len(df_cleaned)} rows")
    return df_cleaned


def extract_dim_product(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Extracting dim_product from dataframe...")

    dim_product = df[["product"]].drop_duplicates().reset_index(drop=True)
    dim_product["product_id"] = dim_product.index + 1  # 简单生成ID

    logger.info(f"Extracted {len(dim_product)} unique products.")
    return dim_product
