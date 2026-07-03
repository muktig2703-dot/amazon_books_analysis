import pandas as pd


def clean_data(df):
    """
    Clean the dataset.

    Returns:
        pandas.DataFrame: Cleaned DataFrame
    """

    print("\n========== DATA CLEANING ==========")

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Remove duplicate rows
    duplicates = df.duplicated().sum()
    print(f"Duplicate rows found: {duplicates}")

    df = df.drop_duplicates()

    # Check missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nData cleaned successfully!")

    return df