__author__ = 'Bartosz'

import config
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


class StdOutListener(StreamListener):

    def on_data(self, raw_data):
        print raw_data
        return True

    def on_error(self, status_code):
        print(status_code)


if __name__ == "__main__":
    l = StdOutListener()
    auth = OAuthHandler(config.api_key, config.api_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['python', 'ruby'])