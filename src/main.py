from data_loader import load_data

from analyzer import (
    clean_data,
    basic_analysis,
    top_authors,
    genre_distribution,
    yearly_books
)


def main():

    file_path = "data/amazon_bestsellers.csv"

    books = load_data(file_path)

    if books is not None:

        books = clean_data(books)

        basic_analysis(books)

        top_authors(books)

        genre_distribution(books)

        yearly_books(books)


if __name__ == "__main__":
    main()