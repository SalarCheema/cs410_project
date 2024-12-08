# cs410_project`

Here's a draft for your `README.md` file based on the details you provided:

---

# Political Leaning Prediction for Subreddits

## Overview

This project aims to predict the political leaning of specific subreddits by analyzing their textual content. Using clearly partisan subreddits such as *liberal*, *democrat*, *kamala*, *conservative*, *republican*, and *trump*, we trained models to classify subreddits based on their political orientation.

## Key Features

- **Text Information Systems**: Leveraged text data for training and testing machine learning models.
- **Training and Testing Pipelines**: Efficient systems for preprocessing, training, and testing data using advanced techniques.
- **Exploratory Modeling**: Tested approaches such as TF-IDF and Random Forest classifiers, as well as vector space implementations.

## Project Structure

### CSV Files
- **`Insurance_top_posts.csv`**: Test data from insurance-related subreddits.
- **`NonPoliticalTwitter_top_posts.csv`**: Test data from non-political Twitter posts.
- **`political_data.csv`**: Training data containing text from politically aligned subreddits.
- **`pre_processed_data.csv`**: Preprocessed text data ready for modeling.
- **`wallstreetbets_top_posts.csv`**: Test data from the WallStreetBets subreddit.

### Python Scripts
- **`predictions.py`**: Initial testing of ideas and approaches for political leaning predictions.
- **`preprocessing.py`**: Scripts for cleaning and preprocessing the data.
- **`subreddit_train.py`**: Script to pull data from subreddits and prepare it for training.
- **`subreddit_tests.py`**: Script to pull test data from subreddits such as Insurance, Non-Political, and WallStreetBets.

### Jupyter Notebooks
- **`TFIDF.ipynb`**: Implements a TF-IDF-based approach combined with Random Forest classifiers for prediction.
- **`VectorSpace.ipynb`**: Implements a vector space modeling approach for analyzing and predicting political leanings.

## Setup and Usage

1. **Data Preparation**:
   - Place training and test datasets in the appropriate `.csv` files (provided in the repository).
   - Use `preprocessing.py` to clean raw text data.

2. **Training and Testing**:
   - Train models using `subreddit_train.py`.
   - Evaluate performance on test data using `subreddit_tests.py`.

3. **Exploratory Modeling**:
   - Open and explore the notebooks `TFIDF.ipynb` and `VectorSpace.ipynb` for advanced modeling approaches.

## Expected Outputs

- Predictions of the political leaning of subreddits in the test datasets.
- Insights into the performance of different models (e.g., TF-IDF + Random Forest vs. Vector Space).