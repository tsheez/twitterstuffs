import tweepy
from tweepy.streaming import StreamListener
from tweepy import Stream

class listener (StreamListener):
    def __init__(self, api = None, maxTweets = 10):
        self.numTweets = 0
        self.maxTweets = maxTweets
        self.api = api
        self.tweetList =[]
    def on_status(self, status):
        if not status.text.startswith('RT'):
            self.tweetList.append(status)
            self.numTweets+=1
            print(self.numTweets)
        if self.numTweets >= self.maxTweets:
            return False
        return True
    def on_error(self,status):
        print(status)

def tweetRetriever (api, auth, filter = "test", maxTweets = 2, lang="en"):
    listen = listener(api, maxTweets=maxTweets)
    twitterStream = Stream(auth, listen)
    twitterStream.filter(languages=[lang], track = [filter])
    return listen.tweetList





"""
twitterStream = Stream(auth, listener(api))
twitterStream.filter(languages=["en"],track=["Locked and Loaded"])
print('fart')
"""