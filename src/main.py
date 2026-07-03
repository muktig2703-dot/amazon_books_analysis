from data_loader import load_data
from analyzer import clean_data


def main():
    file_path = "data/amazon_bestsellers.csv"

    books = load_data(file_path)

    if books is not None:

        books = clean_data(books)

        print("\n========== FIRST 5 ROWS ==========")
        print(books.head())

        print("\n========== DATASET SHAPE ==========")
        print(books.shape)

        print("\n========== COLUMN NAMES ==========")
        print(books.columns)

        print("\n========== DATA TYPES ==========")
        print(books.dtypes)

        print("\n========== SUMMARY STATISTICS ==========")
        print(books.describe())


if __name__ == "__main__":
    main()