import os


def export_cleaned_data(df):
    """
    Export cleaned dataset.
    """
    os.makedirs("output", exist_ok=True)

    df.to_csv("output/cleaned_data.csv", index=False)

    print("✅ Cleaned dataset exported.")


def export_analysis(df):
    """
    Export analysis results to CSV.
    """

    analysis = {
        "Metric": [
            "Total Books",
            "Unique Authors",
            "Average Rating",
            "Average Price",
            "Highest Rating",
            "Maximum Reviews"
        ],

        "Value": [
            len(df),
            df["author"].nunique(),
            round(df["user_rating"].mean(), 2),
            round(df["price"].mean(), 2),
            df["user_rating"].max(),
            df["reviews"].max()
        ]
    }

    import pandas as pd

    analysis_df = pd.DataFrame(analysis)

    analysis_df.to_csv(
        "output/analysis_results.csv",
        index=False
    )

    print("✅ Analysis results exported.")


def generate_summary_report(df):
    """
    Generate text summary.
    """

    report = f"""
==============================
 AMAZON BESTSELLER ANALYSIS
==============================

Total Books          : {len(df)}

Unique Authors       : {df['author'].nunique()}

Average Rating       : {df['user_rating'].mean():.2f}

Average Price        : ${df['price'].mean():.2f}

Highest Rating       : {df['user_rating'].max()}

Maximum Reviews      : {df['reviews'].max()}

Most Popular Genre   : {df['genre'].mode()[0]}

Top Author           : {df['author'].value_counts().idxmax()}

Report Generated Successfully.
"""

    with open(
        "output/summary_report.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write(report)

    print("✅ Summary report generated.")