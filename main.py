import tweepy
import sys
import jsonpickle
import os


auth = tweepy.AppAuthHandler("cp87wlIepQ8zLOdlmXWe6ns4o","I0GJIpQl4XPmDuqh1TUqKAoMz8x3wHUaoPkILndfaPdlmNZO9A")
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

if (not api):
    print("Can't Authenticate")
    sys.exit(-1)


searchQuery = "#hashtag"
maxTweets = 1000
tweetsPerQry = 100
fName = "/Users/Lykke-AndersenLab/Desktop/tweets.txt"

sinceId = None

max_id = -1

tweetCount = 0
print("Downloading max {0} tweets".format(maxTweets))
with open(fName, 'w') as f:
    while tweetCount < maxTweets:
        try:
            if (max_id <=0):
                if (not sinceId):
                    new_tweets = api.search(q=searchQuery, count = tweetsPerQry)
                else:
                    new_tweets = api.search(q = searchQuery, count = tweetsPerQry, since_id=sinceId)
            else:
                if (not sinceId):
                    new_tweets=api.search(q=searchQuery, count=tweetsPerQry, max_id=str(max_id-1))
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,max_id=str(max_id - 1),since_id=sinceId)
            if not new_tweets:
                print("No more tweets found")
                break
            for tweet in new_tweets:
                f.write(jsonpickle.encode(tweet._json,unpicklable=False)+"/n")
            tweetCount+= len(new_tweets)
            print("Downloaded {0} tweets".format(tweetCount))
            max_id = new_tweets[-1].id
        except tweepy.TweepError as e:
            print ("some error : " + str(e))
            break