import tweepy

auth = tweepy.OAuthHandler("cp87wlIepQ8zLOdlmXWe6ns4o", "I0GJIpQl4XPmDuqh1TUqKAoMz8x3wHUaoPkILndfaPdlmNZO9A")
auth.set_access_token("891695227395645442-BtHtN3c7clyoFNO6EM7s7yMqjI5qQpr", "IX4x9GW9dfA7bkHISkEw6BE7TS7f7GTVlImS6EzCcoKzx")

api = tweepy.API(auth)

#vernTweets= api.user_timeline(screen_name="VernonShaw
n=0
for dude in api.search("farts", count=1000):
    print(dude.created_at)
    n+=1
print(n)