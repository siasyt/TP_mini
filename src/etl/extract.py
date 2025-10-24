import os

import pandas as pd
from dotenv import load_dotenv

from src.utils.logging_conf import logger

load_dotenv()

DATA_DIR = os.getenv("DATA_DIR", "./data")


def read_csv_file(relative_path: str) -> pd.DataFrame:
    full_path = os.path.join(DATA_DIR, relative_path)
    logger.info(f"Reading CSV file from: {full_path}")
    try:
        df = pd.read_csv(full_path)
        logger.info(f"Loaded {len(df)} rows.")
        return df
    except FileNotFoundError:
        logger.error(f"File not found: {full_path}")
        raise
    except Exception as e:
        logger.error(f"Error reading file {full_path}: {e}")
        raise
