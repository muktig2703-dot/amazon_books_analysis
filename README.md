# 📚 Amazon Bestselling Books Analyzer

A Python data analysis project that explores Amazon's bestselling books dataset using **Pandas** and **Matplotlib**.

The project cleans the dataset, performs exploratory data analysis (EDA), generates insightful visualizations, exports analysis results, and automatically creates a summary report.

---

## 🚀 Features

- Load dataset from CSV
- Clean and preprocess data
- Perform exploratory data analysis
- Analyze:
  - Total books
  - Unique authors
  - Average ratings
  - Average prices
  - Most reviewed book
  - Highest-rated book
  - Genre distribution
  - Top authors
- Generate charts automatically
- Export cleaned dataset
- Export analysis results to CSV
- Generate summary report automatically

---

## 📂 Project Structure

amazon-books-analysis/

├── charts/

├── data/

├── output/

├── src/

├── README.md

├── requirements.txt

└── .gitignore

---

## 📊 Visualizations

The project automatically generates:

- Top 10 Authors
- Genre Distribution
- Rating Distribution
- Price Distribution
- Reviews vs Rating

All charts are saved inside the `charts/` folder.

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/amazon-books-analysis.git
```

Go into the project

```bash
cd amazon-books-analysis
```

Create virtual environment

```bash
python -m venv venv
```

Activate it

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python src/main.py
```

---

## 📁 Output

Running the project generates:

### Charts

- charts/top_authors.png
- charts/genre_distribution.png
- charts/rating_distribution.png
- charts/price_distribution.png
- charts/reviews_vs_rating.png

### CSV Files

- output/cleaned_data.csv
- output/analysis_results.csv

### Report

- output/summary_report.txt

---

## 📈 Dataset

Amazon Top 50 Bestselling Books (2009–2019)

Columns:

- Name
- Author
- User Rating
- Reviews
- Price
- Year
- Genre

---

## 🌟 Future Improvements

- Interactive dashboard using Streamlit
- Advanced statistical analysis
- Machine Learning predictions
- Interactive charts with Plotly
- Unit tests

---

## 👨‍💻 Author

Mukti