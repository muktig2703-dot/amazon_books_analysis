import pandas as pd


def clean_data(df):
    """
    Clean the dataset.
    """

    print("\n========== DATA CLEANING ==========")

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    duplicates = df.duplicated().sum()
    print(f"Duplicate rows found: {duplicates}")

    df = df.drop_duplicates()

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nData cleaned successfully!")

    return df


def basic_analysis(df):
    """
    Display basic statistics about the dataset.
    """

    print("\n========== BASIC ANALYSIS ==========\n")

    print(f"Total Books           : {len(df)}")
    print(f"Unique Authors        : {df['author'].nunique()}")
    print(f"Average Rating        : {df['user_rating'].mean():.2f}")
    print(f"Average Price         : ${df['price'].mean():.2f}")
    print(f"Highest Rating        : {df['user_rating'].max()}")
    print(f"Maximum Reviews       : {df['reviews'].max()}")

    print("\nMost Reviewed Book")
    print(df.loc[df['reviews'].idxmax()][['name', 'author', 'reviews']])

    print("\nHighest Rated Book")
    print(df.loc[df['user_rating'].idxmax()][['name', 'author', 'user_rating']])


def top_authors(df, n=10):
    """
    Display top authors with the most bestselling books.
    """

    print("\n========== TOP AUTHORS ==========\n")

    authors = df['author'].value_counts().head(n)

    print(authors)


def genre_distribution(df):
    """
    Display genre distribution.
    """

    print("\n========== GENRE DISTRIBUTION ==========\n")

    print(df['genre'].value_counts())


def yearly_books(df):
    """
    Display number of books per year.
    """

    print("\n========== BOOKS PER YEAR ==========\n")

    print(df['year'].value_counts().sort_index())