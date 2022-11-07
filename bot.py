import os
import tweepy
import time
from medium import *
from dotenv import load_dotenv

load_dotenv(".env", override=True)

# Tokens
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_KEY_SECRET = os.environ['CONSUMER_KEY_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['ACCESS_TOKEN_SECRET']
BEARER_TOKEN = os.environ['BEARER_TOKEN']

client = tweepy.Client( bearer_token=BEARER_TOKEN, 
                        consumer_key=CONSUMER_KEY, 
                        consumer_secret=CONSUMER_KEY_SECRET, 
                        access_token=ACCESS_TOKEN, 
                        access_token_secret=ACCESS_TOKEN_SECRET, 
                        wait_on_rate_limit=True)


post = Title_Link_Post(URL)
newPost = ""
# Check for new posts
while True:
    if(newPost != post): 
        try:
            client.create_tweet(text=Title_Link_Post(URL))
            print("Successfully posted new tweet!")
        except tweepy.Forbidden:
            print("Tweet is a duplicate error, skipping")
        newPost = Title_Link_Post(URL)
    else: 
        print("Post is a duplicate (non-error), skipping")
        post = Title_Link_Post(URL)
    time.sleep(30)
