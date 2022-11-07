import os
import tweepy
import time
from dotenv import load_dotenv
from medium import *

load_dotenv(".env", override=True)

# Tokens
API_KEY = os.environ['CONSUMER_KEY']
API_SECRET_KEY = os.environ['CONSUMER_KEY_SECRET']
API_ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
API_ACCESS_SECRET = os.environ['ACCESS_TOKEN_SECRET']
BEARER_TOKEN = os.environ['BEARER_TOKEN']

client = tweepy.Client( bearer_token=BEARER_TOKEN, 
                        consumer_key=API_KEY, 
                        consumer_secret=API_SECRET_KEY, 
                        access_token=API_ACCESS_TOKEN, 
                        access_token_secret=API_ACCESS_SECRET, 
                        wait_on_rate_limit=True)

post = Title_Link_Post(URL)
newPost = ""
# Check if the post is new
while True:
    if(newPost != post): 
        print("Post is old, creating new post")
        client.create_tweet(text=Title_Link_Post(URL))
        newPost = Title_Link_Post(URL)
    else: 
        print("Post is new, skipping")
        post = Title_Link_Post(URL)
    time.sleep(30)
# print(Title_Link_Post(URL))
# client.create_tweet(text=Title_Link_Post(URL))
