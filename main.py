from src.etl.extract import read_csv_file
from src.etl.load import save_dataframe
from src.etl.transform import clean_dataframe, extract_dim_product


def main():
    df = read_csv_file("raw/example.csv")
    df_clean = clean_dataframe(df)

    dim_product = extract_dim_product(df_clean)

    fact_sales = df_clean.merge(dim_product, on="product", how="left")

    save_dataframe(dim_product, "dim/dim_product.csv")

    save_dataframe(fact_sales, "fact/fact_sales.csv")


if __name__ == "__main__":
    main()
