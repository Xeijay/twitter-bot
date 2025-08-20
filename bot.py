import os
import tweepy
import schedule
import time
import random
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()
api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_secret = os.getenv("ACCESS_SECRET")
bearer_token = os.getenv("BEARER_TOKEN")

# Authenticate with Twitter (X)
client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_secret,
    bearer_token=bearer_token
)

# 2-day crypto beginner tweets
tweets = [
    # Day 1
    "Welcome to crypto! 🌍💸 Think of it as digital money you can send anywhere in the world. #CryptoForBeginners",
    "Step 1: Get a crypto wallet. It's like a digital bank account for your coins 🏦🔑 #CryptoMadeSimple",
    "Step 2: Understand your private key — this is your password to access your crypto. Never share it! 🔐 #CryptoTips",
    "Fun fact: Losing your private key is like losing your car keys… but for $10,000 worth of Bitcoin 🚗💨 #CryptoHumor",
    "Step 3: Your public key is your crypto address. People can send coins here. Think of it like your email. 📧 #CryptoBasics",
    
    # Day 2
    "Step 4: Start with a trusted exchange to buy your first crypto safely 💰 #CryptoLearning",
    "Bitcoin = digital gold, Ethereum = apps and money. It's like Harry Potter vs Iron Man ⚡🧙‍♂️ #CryptoFun",
    "DYOR = Do Your Own Research. Always check info before buying crypto 📚 #LearnCrypto",
    "Funny tip: Crypto market mood swings faster than your coffee addiction ☕📈📉 #CryptoHumor",
    "Step 5: Keep your crypto safe. Enable 2FA and double-check wallet addresses 🛡️ #CryptoSafety"
]

# Function to post a tweet with random delay
def post_tweet_random(text):
    delay = random.randint(0, 5) * 60  # Random delay 0-5 minutes
    time.sleep(delay)
    try:
        response = client.create_tweet(text=text)
        print(f"Tweeted successfully ✅ after {delay//60} min delay:", response.data)
    except tweepy.TweepyException as e:
        print("Error posting tweet:", e)

# Day 1 adjusted schedule (first two tweets 30 min apart from now)
now = datetime.now()
schedule.every().day.at(now.strftime("%H:%M")).do(lambda: post_tweet_random(tweets[0]))  # Tweet 0 immediately
schedule.every().day.at((now + timedelta(minutes=30)).strftime("%H:%M")).do(lambda: post_tweet_random(tweets[1]))  # Tweet 1 in 30 min

# Continue rest of Day 1 using template times
schedule.every().day.at("15:00").do(lambda: post_tweet_random(tweets[2]))  # Educational
schedule.every().day.at("18:00").do(lambda: post_tweet_random(tweets[3]))  # Fun/Humor
schedule.every().day.at("21:00").do(lambda: post_tweet_random(tweets[4]))  # Recap/Safety

# Day 2 normal schedule
schedule.every().day.at("09:00").do(lambda: post_tweet_random(tweets[5]))
schedule.every().day.at("12:00").do(lambda: post_tweet_random(tweets[6]))
schedule.every().day.at("15:00").do(lambda: post_tweet_random(tweets[7]))
schedule.every().day.at("18:00").do(lambda: post_tweet_random(tweets[8]))
schedule.every().day.at("21:00").do(lambda: post_tweet_random(tweets[9]))

print("Bot is running... Press Ctrl+C to stop.")

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(60)
