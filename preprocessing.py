import praw
import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk

# Define punctuation and stop words
punctuations = """'\"<>./?@#$%^&*_~/!()-[]{};:,”‘’“”"""
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Create DataFram
df = pd.read_csv("political_data.csv")
def preprocess_text_data(df):
    for index, row in df.iterrows():
        text = row['text']
        
        text = text.lower()
        
        text = re.sub(r'http\S+|www\S+|https\S+', '', text)
        
        text = "".join(char for char in text if char not in punctuations)
        
        words = word_tokenize(text)
        words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
        
        df.at[index, 'text'] = ' '.join(words)

preprocess_text_data(df)



filtered_df = df[df['text'].str.split().str.len() > 10]


#filtered_df.to_csv("pre_processed_data.csv", index=False)
