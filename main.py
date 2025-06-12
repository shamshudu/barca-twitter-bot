import tweepy
import os
from datetime import date

# === Your API keys ===
consumer_key = '6U91WoB2Ir11lBoazScl7lVLF'
consumer_secret = 'yiHbwRLZTPiO1MaLcD9U5iq76H0tPLvEKRtba52cKxsHmy5F5X'
access_token = '1932318941608869889-TumJVe5F9rdXmpTAfAa9hPwyFgFp3M'
access_token_secret = 'WaGcwQtQCZU7Z45FzULHuWENpVR0B603awpX4xwbZ4gcS'

# === Setup Tweepy Client ===
client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# === Calculate days since Barca won UCL ===
ucl_win_date = date(2015, 6, 6)
today = date.today()
days_since_win = (today - ucl_win_date).days

# === Prepare tweet text (short version) ===
tweet_text = f"{days_since_win}"


# === Post tweet ===
try:
    response = client.create_tweet(text=tweet_text)
    print(f"Tweet posted! Tweet ID: {response.data['id']}")
except Exception as e:
    print("Error posting tweet:", e)
