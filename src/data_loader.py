import pandas as pd


def load_data(file_path):
    """
    Load the Amazon Bestsellers dataset.

    Args:
        file_path (str): Path to the CSV file.

    Returns:
        pandas.DataFrame: Loaded dataset.
    """
    try:
        df = pd.read_csv(file_path)
        print("✅ Dataset loaded successfully!")
        return df

    except FileNotFoundError:
        print("❌ Error: File not found.")
        return None

    except Exception as e:
        print(f"❌ Unexpected Error: {e}")
        return None