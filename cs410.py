import praw
import pandas as pd
# from datetime import datetime

reddit = praw.Reddit(
    client_id = "Y3K32EezzVtGPChSR9UI6Q",
    client_secret = "vwSfrxe9rKgQ3Iv9eptAYIFzhkh4Ng",
    user_agent = "test"
)

df = pd.DataFrame(columns=['text', 'subreddit', 'post_or_comment', 'expected_political_leaning', 'score'])

def political_analysis():
    global df

    def reddit_call(subreddit, political_lean, num_posts, num_comments):
        global df
        sub = reddit.subreddit(subreddit)

        for submission in sub.top("year", limit=num_posts):
            # post_datetime = datetime.utcfromtimestamp(submission.created_utc)
            df = pd.concat([df, pd.DataFrame([{'text': (submission.title + submission.selftext),
                                                    'subreddit': subreddit, 
                                                    'post_or_comment': "post", 
                                                    'expected_political_leaning': political_lean,
                                                    'score': submission.score}])], ignore_index=True)

            submission.comment_sort = 'best'
            submission.comments.replace_more(limit = 0)
            top_comments = submission.comments[:num_comments]
            for comment in top_comments:
                if comment.author == "AutoModerator" or comment.body in ["[deleted]", "[removed]"]:
                    continue
                df = pd.concat([df, pd.DataFrame([{'text': (comment.body),
                                        'subreddit': subreddit, 
                                        'post_or_comment': "comment", 
                                        'expected_political_leaning': political_lean,
                                        'score': comment.score}])], ignore_index=True)

    # liberal subreddits
    reddit_call("Democrats", "lib", 100, 20)
    reddit_call("Liberal", "lib", 100, 20)
    reddit_call("KamalaHarris", "lib", 100, 20)

    # conservative subreddits
    reddit_call("Republicans", "con", 100, 20)
    reddit_call("Conservative", "con", 100, 20)
    reddit_call("Trump", "con", 100, 20)


    

political_analysis()
df.to_csv("political_data.csv", index=False)