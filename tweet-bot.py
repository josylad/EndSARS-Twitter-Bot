import tweepy
import time 
import os
import random
from dotenv import load_dotenv
load_dotenv()

consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

FILE_NAME = 'seen_tweets.txt'

# Authenticate to Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,  wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)

def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id

def store_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return

last_seen_id = str(read_last_seen(FILE_NAME))



def tweet_replies():
    tweets =api.mentions_timeline(since_id=last_seen_id)
    # print(tweets)
    if tweets:
        for tweet in reversed(tweets):
            tweet1 = "@" +tweet.user.screen_name + " #EndSarsNow #ReformPoliceNG #EndSars #ReformPoliceNG #EndSars #ReformPoliceNG  #EndSars  #EndSars  #EndSars #EndSars #EndSars #EndSars #EndSars #EndSars #EndSars #EndSars #EndSars #EndSars"
            tweet2 = "@" +tweet.user.screen_name + " #ReformPoliceNG #EndSars #ReformPoliceNG #EndSars #ReformPoliceNG #ReformPoliceNG #EndSars #ReformPoliceNG #ReformPoliceNG #EndSarsNow #EndSarsNow #EndSarsNow"
            tweet3 = "@" +tweet.user.screen_name + " #EndSars #ReformPoliceNG #EndSars #EndSars #ReformPoliceNG #EndSars #EndSars #EndSarNow #EndSars #EndSars #EndSars #EndSars #ReformPoliceNG #EndSars #EndSars #EndSars #EndSars #EndSars #EndSars #EndSars "
            all_tweets = [tweet1, tweet2, tweet3]
            final_tweet = random.choice(all_tweets)
            # print(final_tweet)
            print(str(tweet.id) + ' - ' + tweet.text)
            try:
                api.update_status(final_tweet, tweet.id)
                api.create_favorite(tweet.id)
                store_last_seen(FILE_NAME, tweet.id)

            except Exception:
                print("an error occured")
    else:
        print('No New Tweets')

while True:
    tweet_replies()
    time.sleep(15)