import tweepy, time
from streamer import tweetRetriever

def friendCleanup(api):
    """Removes friends who don't follow you back"""
    friends = api.friends_ids(api.me().id)
    followers = api.followers_ids(api.me().id)
    for friend in friends:
        if friend not in followers:
            api.destroy_friendship(friend)

def reAndFriend (status):
    api.retweet(status.id)
    api.create_friendship(status.author.id)

auth = tweepy.OAuthHandler("cp87wlIepQ8zLOdlmXWe6ns4o", "I0GJIpQl4XPmDuqh1TUqKAoMz8x3wHUaoPkILndfaPdlmNZO9A")
auth.set_access_token("891695227395645442-BtHtN3c7clyoFNO6EM7s7yMqjI5qQpr",
                      "IX4x9GW9dfA7bkHISkEw6BE7TS7f7GTVlImS6EzCcoKzx")
api = tweepy.API(auth)
filt = "#FridayFeeling"
while True:
    collection = tweetRetriever(api, auth, filter=filt, maxTweets=2)
    print("dope")
    time.sleep(300)
    reAndFriend(collection[0])
