# Task\_03\_Descriptive\_Stats

## Overview

This project provides descriptive statistical analysis of three real-world datasets related to the 2024 US presidential elections and social media activity. The analysis is performed using three different approaches:

- **Pure Python (Standard Library)**
- **Pandas**
- **Polars**

The goal is to generate identical statistical summaries with all three methods, compare their usability and performance, and discuss the advantages and challenges of each.

---

## Repository Structure

- **pure\_python\_stats.py**\
  Compute descriptive stats using only standard Python libraries.
- **pandas\_stats.py**\
  Perform the same analysis using the Pandas library.
- **polars\_stats.py**\
  Replicate the workflow using the Polars library.
- **analysis.ipynb**\
  (If provided) Optional notebook with visualizations and additional narrative.
- **README.md**\
  Instructions, summary, and key findings (this file).

---

## How to Run

1. **Download the dataset** from the provided [link](https://drive.google.com/file/d/1Jq0fPb-tq76Ee_RtM58fT0_M3o-JDBwe/view?usp=sharing).

2. **Do NOT commit dataset files to the repository**.

3. **Run each script** from the command line, providing your data file:

   ```bash
   python pure_python_stats.py <dataset.csv>
   python pandas_stats.py <dataset.csv>
   python polars_stats.py <dataset.csv>
   ```

   If you do not specify a file, the scripts use a default filename.

---

## What Each Script Does

### 1. **pure\_python\_stats.py**

- Loads CSV using only the Python standard library.
- Calculates count, mean, min, max for numerics; unique counts and most frequent values for categorical fields.
- Aggregates stats by `page_id` and by (`page_id`, `ad_id`).

### 2. **pandas\_stats.py**

- Loads data via Pandas.
- Uses `.describe()`, `.nunique()`, and `.mode()` for stats.
- Aggregates stats by `page_id` and (`page_id`, `ad_id`).

### 3. **polars\_stats.py**

- Uses the Polars DataFrame library.
- Runs `.describe()`, `.n_unique()`, and `.mode()` equivalents.
- Aggregates and summarizes as above.

---

## Visualization (Bonus)

- Additional scripts or notebooks may provide histograms, bar charts, and boxplots using matplotlib, seaborn, or plotly.
- These visualizations help highlight distributions, frequent values, and comparative stats between methods.

---

## Key Findings & Insights

- **Consistency**: All three approaches successfully reproduce basic descriptive statistics (count, mean, min, max, most frequent value) and group-level aggregations.
- **Usability**:
  - **Pure Python**: Offers transparency and control, but is verbose and less performant for large datasets.
  - **Pandas**: The most user-friendly and commonly adopted for quick data analysis. Rich ecosystem and great for tabular data.
  - **Polars**: Much faster than Pandas on large datasets, with intuitive syntax, but ecosystem is still maturing.
- **Recommendations**: For exploratory data analysis and rapid prototyping, Pandas is ideal. For very large datasets or production scenarios, Polars offers significant speed advantages. Pure Python is best for learning internals or in environments with package restrictions.
- **Challenges**: Ensuring identical output across approaches required careful type handling and consistent missing-value treatment.

---

## Example Usage

```bash
python pandas_stats.py 2024_fb_ads_president_scored_anon.csv
```

Outputs summary stats, unique counts, frequent values, and group-level statistics.

---

## Summary

This project demonstrates and compares three approaches to descriptive statistics—showing both the power of third-party data science libraries and the ability to replicate results with base Python. The code is modular and reusable for any CSV-based dataset with similar requirements.

---

## Author

Lakshmi Peram\
[lperam@syr.edu](mailto\:lperam@syr.edu)

---

