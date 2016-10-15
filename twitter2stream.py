## default setting is 'track' for keywords
## switch 'track' to follow to stream tweets based on user ID instead

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
 
access_token = ""
access_secret = ""
consumer_secret = ""
consumer_key = ""

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
class MyListener(StreamListener):

    def on_error(self, status):
        print(status)
        return True
    
    def on_data(self, data):
        try:
            with open('/home/ubuntu/dep-panel.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("&quot;Error on_data: %s&quot; % str(e)")
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['keyword1','keyword2'])
