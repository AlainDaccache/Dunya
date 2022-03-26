import tweepy
import os
import json
from kafka import KafkaProducer
from dotenv import load_dotenv
from json import dumps
from time import sleep

load_dotenv()

"""
Authentication: To setup a Twitter Stream, we first need to authenticate with
"""
# to set up a Twitter Stream, we need two things: authentication, and a twitter StreamListener

# You need to ask for Elevated access before using Tweepy, in:
# https://developer.twitter.com/en/portal/products/elevated

auth = tweepy.OAuth1UserHandler(
    # consumer key and secret are identifiers for our App in Twitter (i.e. application dependent)
    consumer_key=os.getenv('TWITTER_CONSUMER_KEY'),
    consumer_secret=os.getenv('TWITTER_CONSUMER_SECRET')
)

# access key and secret are user-based identifiers
auth.set_access_token(key=os.getenv('TWITTER_USER_KEY'), secret=os.getenv('TWITTER_USER_SECRET'))

# authenticate with Twitter's API
api = tweepy.API(auth)

# If the authentication was successful, this should print the screen name / username of the account
print(api.verify_credentials().screen_name)


class MyStream(tweepy.Stream):
    """
    Stream listener got merged into Stream in recent tweepy update.
    We override `tweepy.Stream` to add logic for initializing producer and sending data with it
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # initialize producer
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092']
                                      # value_serializer=lambda x: dumps(x).encode('utf-8')
                                      )

    def on_status(self, status):
        print(status.id)

    def on_data(self, data):
        json_ = json.loads(data)
        self.producer.send(topic="Twitter-Kafka", value=json_["text"].encode('utf-8'))
        return True

    def on_error(self, status_code):
        """The default implementation returns False for all codes, but we can override it to allow Tweepy to reconnect
        for some or all codes. In this case, we're returning False in on_error disconnects the stream"""
        print('Status code', status_code)
        if status_code == 420:
            return False


UkrainStreamListener = MyStream(consumer_key=os.getenv('TWITTER_CONSUMER_KEY'),
                                consumer_secret=os.getenv('TWITTER_CONSUMER_SECRET'),
                                access_token=os.getenv('TWITTER_USER_KEY'),
                                access_token_secret=os.getenv('TWITTER_USER_SECRET'))

UkrainStreamListener.filter(track=["Ukraine", "Ukrainian", "UkraineWar"])
