import matplotlib.pyplot as plt


def plot_top_authors(df):
    authors = df['author'].value_counts().head(10)

    plt.figure(figsize=(10, 6))
    authors.sort_values().plot(kind='barh')

    plt.title("Top 10 Authors")
    plt.xlabel("Number of Bestselling Books")
    plt.ylabel("Author")

    plt.tight_layout()
    plt.savefig("charts/top_authors.png")
    plt.close()


def plot_genre_distribution(df):
    genre = df['genre'].value_counts()

    plt.figure(figsize=(6, 6))
    genre.plot(
        kind='pie',
        autopct='%1.1f%%',
        startangle=90
    )

    plt.ylabel("")
    plt.title("Genre Distribution")

    plt.tight_layout()
    plt.savefig("charts/genre_distribution.png")
    plt.close()


def plot_rating_distribution(df):
    plt.figure(figsize=(8, 5))

    plt.hist(
        df['user_rating'],
        bins=10
    )

    plt.title("User Rating Distribution")
    plt.xlabel("Rating")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.savefig("charts/rating_distribution.png")
    plt.close()


def plot_price_distribution(df):
    plt.figure(figsize=(8, 5))

    plt.hist(
        df['price'],
        bins=15
    )

    plt.title("Price Distribution")
    plt.xlabel("Price ($)")
    plt.ylabel("Frequency")

    plt.tight_layout()
    plt.savefig("charts/price_distribution.png")
    plt.close()


def plot_reviews_vs_rating(df):
    plt.figure(figsize=(8, 5))

    plt.scatter(
        df['reviews'],
        df['user_rating']
    )

    plt.title("Reviews vs User Rating")
    plt.xlabel("Reviews")
    plt.ylabel("User Rating")

    plt.tight_layout()
    plt.savefig("charts/reviews_vs_rating.png")
    plt.close()