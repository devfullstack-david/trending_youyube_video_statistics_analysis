# Trending YouTube Video Statistics Analysis

Created by **David Santos** — [LinkedIn](https://www.linkedin.com/in/coderdavidgs).

Exploratory analysis and data preparation of YouTube trending videos in the US. The project cleans the data, creates new features, plots some charts and prepares a train/test split for machine learning (predicting `likes`).

## What it does

`main.py` runs the whole pipeline:

1. **Load** `USvideos.csv`.
2. **Process** (`processing_data.py`):
   - Fills missing descriptions with an empty string.
   - Converts `publish_time` and `trending_date` to datetime.
   - Creates new features: `days_to_trend`, `engagement_rate` ((likes + comments) / views), `title_length` and `tags_count`.
3. **Visualize** (`show_data.py`):
   - Correlation matrix of views, likes, dislikes and comment count.
   - Number of trending videos by category.
4. **Encode**: one-hot encodes `category_id` and standardizes `views`, `likes` and `dislikes`.
5. **Split**: splits the data 80/20 (train/test, `likes` as target) and saves it to `train_test_split.pkl`.

## Project structure

- `main.py` - entry point.
- `processing_data.py` - cleaning, feature engineering, encoding and train/test split.
- `show_data.py` - plots.
- `requirements.txt` - dependencies (pandas, numpy, matplotlib, seaborn, scikit-learn).

## How to run

```
pip install -r requirements.txt
python main.py
```

## DATASET

https://www.kaggle.com/datasets/datasnaek/youtube-new?select=USvideos.csv

- This Kaggle's dataset is a database with informations about videos that were in trending on US, meeting as "Trending YouTube Video Statistics".