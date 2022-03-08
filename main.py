import tweepy

# Resources to use:
#     -yfinance https://pypi.org/project/yfinance/
#         -https://towardsdatascience.com/the-easiest-way-to-pull-stock-data-into-your-python-program-yfinance-82c304ae35dc
#     -tweepy https://realpython.com/twitter-bot-python-tweepy/
#         -https://www.geeksforgeeks.org/how-to-make-a-twitter-bot-in-python/
        
# Authenticate to Twitter
auth = tweepy.OAuthHandler("CONSUMER_KEY", "CONSUMER_SECRET")
auth.set_access_token("ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello Tweepy")
