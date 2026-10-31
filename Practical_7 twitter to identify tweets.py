import tweepy
consumer_key = "TmWt5DjyuEPBDPdYyYoTYmUKe"
consumer_secret = "rvLZo6WjrYD1E3cKtbme0fQABRh75x47C3hDzBbjNsvizWh9yx"
access_token = "1098817558361395200-KZ1XL9LcBd3Bu546hFUop8Cp4y9Ghg"
access_token_secret = "m8PPhRpIXd4VK9PXcMUfpD9r9idPDednglPD2wlWhlvGS"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)

# Creating the API object while passing in auth information
api = tweepy.API(auth)

# The Twitter user who we want to get tweets from
name = "TechnicalGuruji"
# Number of tweets to pull
tweetCount = 2

# Calling the user_timeline function with our parameters
results = api.user_timeline(id=name,count=tweetCount)

# foreach through all tweets pulled
for tweet in results:
   # printing the text stored inside the tweet object
   print(tweet.text)

