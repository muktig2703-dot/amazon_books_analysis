from data_loader import load_data

from analyzer import (
    clean_data,
    basic_analysis,
    top_authors,
    genre_distribution,
    yearly_books
)

from visualization import (
    plot_top_authors,
    plot_genre_distribution,
    plot_rating_distribution,
    plot_price_distribution,
    plot_reviews_vs_rating
)

from report_generator import (
    export_cleaned_data,
    export_analysis,
    generate_summary_report
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

        print("\nGenerating charts...")

        plot_top_authors(books)
        plot_genre_distribution(books)
        plot_rating_distribution(books)
        plot_price_distribution(books)
        plot_reviews_vs_rating(books)

        print("Charts saved successfully in the charts folder.")

        print("\nExporting files...")

        export_cleaned_data(books)
        export_analysis(books)
        generate_summary_report(books)

        print("\n🎉 Project completed successfully!")


if __name__ == "__main__":
    main()