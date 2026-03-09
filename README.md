# 📊 Netflix Content Analysis

A comprehensive data analysis project exploring Netflix's content library using Python, Pandas, Matplotlib, and Seaborn.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Latest-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Project Overview

This project performs an in-depth exploratory data analysis (EDA) of Netflix's movies and TV shows catalog. The analysis uncovers trends, patterns, and insights about content distribution, genres, ratings, and production across different countries and time periods.

## 📁 Project Structure

```
data-analysis-project/
│
├── data/
│   └── netflix_titles.csv          # Dataset
│
├── notebooks/
│   └── netflix_analysis.ipynb      # Main analysis notebook
│
├── src/
│   └── generate_dataset.py         # Dataset generation script
│
├── visualizations/                 # Generated plots and charts
│
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

## 🔍 Analysis Components

### 1. Data Cleaning
- Handling missing values
- Date parsing and feature engineering
- Data type conversions

### 2. Exploratory Data Analysis
- **Content Type Distribution**: Movies vs TV Shows breakdown
- **Temporal Trends**: Content addition patterns over years
- **Geographic Analysis**: Top content-producing countries
- **Rating Distribution**: Content ratings and audience targeting
- **Genre Analysis**: Most popular genres and categories
- **Duration Patterns**: Movie lengths and TV show seasons
- **Seasonal Trends**: Monthly content addition patterns

### 3. Visualizations
- Bar charts and pie charts for distributions
- Line plots for temporal trends
- Horizontal bar plots for rankings
- Histograms for duration analysis
- Multi-panel comparative visualizations

## 📊 Key Insights

- **Movies dominate** Netflix's library with ~69% of total content
- **Exponential growth** in content additions post-2015
- **United States** leads in content production
- **TV-MA and TV-14** are the most common ratings
- **Dramas and Comedies** are the most prevalent genres
- **Average movie duration**: ~100 minutes
- **Most TV shows** are limited series (1 season)

## 🚀 Getting Started

### Prerequisites

```bash
Python 3.8+
pip
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/data-analysis-project.git
cd data-analysis-project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Generate the dataset:
```bash
python src/generate_dataset.py
```

4. Launch Jupyter Notebook:
```bash
jupyter notebook notebooks/netflix_analysis.ipynb
```

## 📈 Usage

Open the Jupyter notebook in VS Code or Jupyter Lab and run all cells sequentially. The notebook is self-contained with markdown explanations for each analysis step.

## 🛠️ Technologies Used

- **Python 3.8+**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical visualizations
- **Jupyter Notebook**: Interactive analysis environment

## 📸 Sample Visualizations

The project generates multiple high-quality visualizations including:
- Content type distribution charts
- Temporal trend analysis
- Geographic distribution maps
- Rating and genre breakdowns
- Duration pattern analysis

All visualizations are saved in the `visualizations/` directory.

## 🔮 Future Enhancements

- [ ] Sentiment analysis on content descriptions
- [ ] Actor/Director network analysis
- [ ] Machine learning models for content recommendation
- [ ] Comparative analysis with other streaming platforms
- [ ] Interactive dashboards using Plotly or Dash
- [ ] Regional preference pattern analysis
- [ ] Content gap identification for strategic planning

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

## ⭐ Show Your Support

Give a ⭐️ if this project helped you!

## 📚 Acknowledgments

- Dataset inspired by Netflix's public content information
- Analysis techniques from data science best practices
- Visualization design principles from Edward Tufte

---

**Note**: This is a portfolio project for educational and demonstration purposes.
