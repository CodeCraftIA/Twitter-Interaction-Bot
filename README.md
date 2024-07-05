# Twitter-Interaction-Bot
This script initializes a Twikit client to interact with specific Twitter handles by liking, retweeting, and replying to their tweets. It saves login cookies for future sessions, maintains a record of interacted tweets to avoid duplicate interactions, and can handle multiple user handles.

This project is a Python script that automates interactions (likes, retweets, and replies) with tweets from specific Twitter handles. The script uses the Twikit client for Twitter interactions.

# Features
Initializes a Twikit client and handles user login.
Saves and loads cookies to maintain sessions between runs.
Reads interacted tweet IDs to avoid duplicate interactions.
Interacts (likes, retweets, and replies) with tweets from specified Twitter handles.

# Requirements
Python 3.x
tqdm library for progress bars.
twikit library for Twitter API interaction.

# To download the libraries
pip install -r requirements.txt
