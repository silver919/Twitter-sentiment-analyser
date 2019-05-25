import tweepy
from textblob import TextBlob

#Authenticate
consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET_KEY'

access_token = 'ACCESS_TOKEN'
access_token_secret = 'ACCESS_TOKEN_SECRET'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret )
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Search, analysis and print the result
print('Enter the keyword to be searched ')
x = input()
public_tweets = api.search(x)

for tweet in public_tweets:
	print(tweet.text)                         	#print the tweets
	analysis = TextBlob(tweet.text)
	print(analysis.sentiment)					#print the sentiment analysis of the tweet

	