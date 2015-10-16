__author__ = 'Bartosz'

import config
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pymongo import MongoClient
import json


client = MongoClient('localhost', 27017)
tweets = client.twitter_db.twitter_collection


class StdOutListener(StreamListener):

    def on_data(self, raw_data):
        print raw_data
        json_tweet = json.loads(raw_data)
        tweets.insert(json_tweet)
        return True

    def on_error(self, status_code):
        print(status_code)


if __name__ == "__main__":
    l = StdOutListener()
    auth = OAuthHandler(config.api_key, config.api_secret)
    auth.set_access_token(config.access_token, config.access_token_secret)
    stream = Stream(auth, l)

    stream.filter(track=['Christie2016', 'ChrisChristie', 'Elections', 'Elections2016', 'realDonaldTrump',
                         'donaldtrump', 'President', 'headofstate', 'Congress', 'Senate', 'democracy', 'republic',
                         'republicanism', 'leftpolitics', 'rightpolitics', 'politician', 'elections', 'election',
                         'political', 'liberalism', 'conservatism', 'government', 'MittRomney', 'Rommey',
                         'presidential', 'electors', 'democraticparty', 'democrat', 'senator', 'vicepresident',
                         'constitution', 'constitutional', 'nominee', 'Binden', 'JoeBiden', 'LincolnChafee', 'Chafee',
                         'HillaryClinton', 'Clinton', 'Martin O\'Malley', 'O\'Malley', 'BernieSanders', 'Sanders',
                         'JimWebb', 'Webb', 'candidate', 'JebBush', 'Bush', 'Dr.BenCarson', 'Carson', 'TedCruz',
                         'CarlyFiorina', 'Fiorina', 'Jim Gilmore', 'Gilmore', 'LindseyGraham', 'Governor',
                         'Mike Huckabee', 'Huckabee', 'BobbyJindal', 'Jindal', 'JohnKasich', 'Kasich', 'GeorgePataki',
                         'Pataki', 'RandPaul', 'Marco Rubio', 'Rubio', 'RickSantorum', 'Rick Santorum'])