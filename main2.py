import time
import random
from tqdm import tqdm
import os
from twikit import Client

def login_and_save_cookies(username, email, password, cookies_path):
    # Initialize client
    client = Client('en-US')

    # Login using credentials
    client.login(
        auth_info_1=username,
        auth_info_2=email,
        password=password
    )

    # Save cookies to a file
    client.save_cookies(cookies_path)
    print(f"Cookies saved to {cookies_path}")
    return client

def load_cookies_and_use_client(cookies_path):
    # Initialize client
    client = Client('en-US')

    # Load cookies from file
    client.load_cookies(cookies_path)
    print(f"Cookies loaded from {cookies_path}")
    return client

def initialize_client(username, email, password, cookies_path='cookies.json'):
    if os.path.exists(cookies_path):
        print("Trying to access cookies...")
        client = load_cookies_and_use_client(cookies_path)
    else:
        client = login_and_save_cookies(username, email, password, cookies_path)
    
    print(f"Logged in as: {username}")
    return client


def read_interacted_tweet_ids():
    """
    Read tweet IDs from a file and return them as a set.
    """
    with open("interacted_tweet_ids.txt", 'r') as file:
        interacted_ids = {line.strip() for line in file}
    return interacted_ids

def append_tweet_id(tweet_id):
    """
    Append a tweet ID to the interacted tweet IDs file.
    """
    with open("interacted_tweet_ids.txt", 'a') as file:
        file.write(f"{tweet_id}\n")

def filter_interacted_tweets(tweets, interacted_ids):
    """
    Remove tweets that have been interacted with from the list of tweets.
    """
    return [tweet for tweet in tweets if str(tweet.id) not in interacted_ids]

def get_tweets(handles):
    """
    Search for tweets of specific handles and return a list of all tweets.
    """
    all_tweets = []
    for handle in handles:
        try:
            # Get user object
            user = client.get_user_by_screen_name(handle)
            # Get tweets
            tweets = user.get_tweets(tweet_type='Tweets', count=5)
            tweets = tweets[:5]
            all_tweets.extend(tweets)
        except Exception as e:
            print(f"Error fetching tweets for {handle}: {e}")
    return all_tweets


def main():
    all_tweets = get_tweets(handles)
    inter_tweets_ids = read_interacted_tweet_ids()
    new_tweets = filter_interacted_tweets(all_tweets, inter_tweets_ids)
    for t in tqdm(new_tweets):
      count = 0
      print("")
      print(f"Tweet text :", t.text)
      print("#"*50)
      try:
        t.reply(
            text_to_reply,
            #media_ids=media_ids
        )
        print("")
        print("Replied successfully!")
        count+=1
      except Exception as e:
        print("")
        print("Error during replying")
      time.sleep(random.uniform(1.6, 3.3)) 
      try:
          client.favorite_tweet(t.id)
          print("")
          print("Like tweet successfully!")  
          count+=1
      except Exception as e:
        print("")
        print("Error during like")
      time.sleep(random.uniform(1.5, 3.1))  
      try:
          client.retweet(t.id)
          print("")
          print("Retweet successfully!")  
          count+=1
      except Exception as e:
        print("")
        print("Error during Retweet")   
      if count>0:
          append_tweet_id(t.id)
            
      time.sleep(random.uniform(4.5, 10.1))

if __name__ == "__main__":
    # Example usage
    USERNAME = 'xxx'
    EMAIL = 'xxx@gmail.com'
    PASSWORD = 'xxx'
    cookies_path = 'cookies.json'
    handles = ["elonmask", "Cobratate", "Cristiano"]
    text_to_reply = "Great !!!"
    # Initialize the client
    client = initialize_client(USERNAME, EMAIL, PASSWORD, cookies_path)
    main()



