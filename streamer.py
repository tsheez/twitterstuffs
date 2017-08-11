import tweepy
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream

class listener (StreamListener):
    def on_status(self, status):
        print(status.text)
        print(status.created_at)
        return True
    def on_error(self,status):
        print(status)

auth = tweepy.OAuthHandler("cp87wlIepQ8zLOdlmXWe6ns4o", "I0GJIpQl4XPmDuqh1TUqKAoMz8x3wHUaoPkILndfaPdlmNZO9A")
auth.set_access_token("891695227395645442-BtHtN3c7clyoFNO6EM7s7yMqjI5qQpr", "IX4x9GW9dfA7bkHISkEw6BE7TS7f7GTVlImS6EzCcoKzx")

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["#GoT"])

