print("Script started... loading keys")
import os
import tweepy
from dotenv import load_dotenv

# Load .env only when running locally. In GitHub Actions, secrets come from the environment.
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_SECRET = os.getenv("ACCESS_SECRET")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# The text to post. In GitHub Actions we’ll pass this via an env var called TWEET_TEXT.
TWEET_TEXT = os.getenv("TWEET_TEXT")

if not TWEET_TEXT:
    # Fallback for local testing so it doesn’t fail if you forget to set TWEET_TEXT.
    TWEET_TEXT = "Hello world from my GitHub-powered Twitter bot! 🚀"

# Authenticate
client = tweepy.Client(
    consumer_key=API_KEY,
    consumer_secret=API_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_SECRET,
    bearer_token=BEARER_TOKEN
)

# Post the tweet
try:
    response = client.create_tweet(text=TWEET_TEXT)
    print("Tweeted ✅:", response.data)
except tweepy.TweepyException as e:
    print("Failed to tweet ❌:", e)
    raise
