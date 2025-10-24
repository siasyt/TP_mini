import os

import pandas as pd
from dotenv import load_dotenv

from src.utils.logging_conf import logger

load_dotenv()

DATA_DIR = os.getenv("DATA_DIR", "./data")


def save_dataframe(df: pd.DataFrame, relative_path: str) -> None:
    full_path = os.path.join(DATA_DIR, relative_path)
    try:
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        df.to_csv(full_path, index=False)
        logger.info(f"Saved dataframe to: {full_path}")
    except Exception as e:
        logger.error(f"Failed to save dataframe to {full_path}: {e}")
        raise
