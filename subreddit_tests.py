import praw
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

reddit = praw.Reddit(
    client_id="Y3K32EezzVtGPChSR9UI6Q",
    client_secret="vwSfrxe9rKgQ3Iv9eptAYIFzhkh4Ng",
    user_agent="test"
)

punctuations = """'\"<>./?@#$%^&*_~/!()-[]{};:,”‘’“”"""
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    """Preprocess a single text string."""
    text = text.lower()
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = "".join(char for char in text if char not in punctuations)
    words = word_tokenize(text)
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return ' '.join(words)

def preprocess_text_data(df):
    df['text'] = df['text'].apply(preprocess_text)

def fetch_and_save_subreddit_posts(subreddit_name, num_posts=100):
    df = pd.DataFrame(columns=['text'])
    
    subreddit = reddit.subreddit(subreddit_name)

    for submission in subreddit.top(time_filter="year", limit=num_posts):
        post_text = submission.title + "\n" + submission.selftext
        df = pd.concat([df, pd.DataFrame([{'text': post_text}])], ignore_index=True)
    
    preprocess_text_data(df)
    
    output_file = f"{subreddit_name}_top_posts.csv"
    df.to_csv(output_file, index=False)
    print(f"Data for subreddit '{subreddit_name}' saved to {output_file}")

insurance = "Insurance"  
fetch_and_save_subreddit_posts(insurance)

wsbets = "wallstreetbets"
fetch_and_save_subreddit_posts(wsbets)

nonpoltical = "NonPoliticalTwitter"
fetch_and_save_subreddit_posts(nonpoltical)

