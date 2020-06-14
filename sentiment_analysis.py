import tweepy
from textblob import TextBlob

consumerKey="7sHuqUvYP7OXCcvwzmQRsRSfk"
consumerSecret="k105z0UeJw5axPh4yfZYS1xUeN1jQ7jHNv0pKXuKOuEUMXG9AK"
accessToken="1271877339337469952-YrAwzE7om6sO2VTImIDoXXF7f2hYU9"
accessTokenSecret="iZe3F6GUYfRAp3m4Ic3RzDDnmGeSeVqu1Sn7IFNJ7T2jX"

auth=tweepy.OAuthHandler(consumer_key=consumerKey,consumer_secret=consumerSecret)
auth.set_access_token(accessToken,accessTokenSecret)
api=tweepy.API(auth)

numOfTweets= int(input('How many tweets to analyze'))
tweets=tweepy.Cursor(api.search, q='covid19', lang='English').items(numOfTweets)
for tweet in tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
