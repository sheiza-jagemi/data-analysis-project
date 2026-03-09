# Quick Reference Card

## 🚀 Quick Start Commands

```bash
# Run the analysis
jupyter notebook notebooks/netflix_analysis.ipynb

# Or in VS Code: Open netflix_analysis.ipynb and click "Run All"
```

## 📊 Project Structure
```
data-analysis-project/
├── data/                    # Dataset (8,807 Netflix titles)
├── notebooks/               # Jupyter notebook with analysis
├── src/                     # Python scripts
├── visualizations/          # Generated plots (8 images)
├── README.md               # Project documentation
├── GUIDE.md                # Complete setup guide
└── requirements.txt        # Dependencies
```

## 🔧 Common Commands

### Setup
```bash
pip install -r requirements.txt
python setup.py
```

### Run Analysis
```bash
jupyter notebook notebooks/netflix_analysis.ipynb
```

### Git Workflow
```bash
git init
git add .
git commit -m "Initial commit: Netflix analysis"
git remote add origin https://github.com/USERNAME/REPO.git
git push -u origin main
```

## 📈 Analysis Sections

1. **Data Loading** - Import 8,807 records
2. **Data Cleaning** - Handle missing values, parse dates
3. **Content Distribution** - Movies (69%) vs TV Shows (31%)
4. **Temporal Trends** - Growth patterns 2008-2021
5. **Geographic Analysis** - Top 10 producing countries
6. **Rating Analysis** - TV-MA, TV-14, R, PG-13 distribution
7. **Genre Analysis** - Top 15 genres
8. **Duration Patterns** - Movie lengths & TV seasons

## 🎯 Key Insights

- Movies dominate with 69% of content
- Exponential growth post-2015
- US leads content production
- TV-MA most common rating
- Average movie: ~100 minutes
- Most TV shows: 1 season

## 📝 Customization Points

**README.md** (Lines 95-97):
- Add your name
- Add GitHub username
- Add LinkedIn profile

**Notebook Colors**:
- Netflix Red: `#E50914`
- Netflix Black: `#221f1f`

## 🔗 Useful Links

- [Pandas Docs](https://pandas.pydata.org/docs/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/)
- [Seaborn Tutorial](https://seaborn.pydata.org/tutorial.html)
- [Jupyter Notebook](https://jupyter.org/documentation)

## 💡 Extension Ideas

- Add sentiment analysis
- Create interactive dashboard
- Build recommendation system
- Add statistical tests
- Include ML predictions

## 🆘 Quick Fixes

**Kernel not found:**
```bash
python -m ipykernel install --user
```

**Missing packages:**
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

**Visualizations folder missing:**
```bash
mkdir -p visualizations
```

---

**Ready to impress recruiters? Run the notebook and push to GitHub! 🚀**
