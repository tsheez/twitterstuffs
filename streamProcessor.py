import tweepy
from streamer import tweetRetriever








if __name__ == "__main__":
    auth = tweepy.OAuthHandler("cp87wlIepQ8zLOdlmXWe6ns4o", "I0GJIpQl4XPmDuqh1TUqKAoMz8x3wHUaoPkILndfaPdlmNZO9A")
    auth.set_access_token("891695227395645442-BtHtN3c7clyoFNO6EM7s7yMqjI5qQpr",
                          "IX4x9GW9dfA7bkHISkEw6BE7TS7f7GTVlImS6EzCcoKzx")
    api = tweepy.API(auth)

    filter = "#GoogleDoodle"
    maxTweets = 10


    collected = tweetRetriever(api, auth, maxTweets=maxTweets, filter = filter)
    for dude in collected:
        print (dude.text)
        print (dude.created_at)
        print (dude.id)