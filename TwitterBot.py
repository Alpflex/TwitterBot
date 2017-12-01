# !/usr/bin/env python
# -*- coding: utf-8 -*-

#tweepy is the library we will be using to access the Twitter API

import tweepy, time, sys
import random
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

import csv




#argfile = str(sys.argv[1])


#To know that it access to my Bot and not others
CONSUMER_KEY = 'XoeCPoYfBB1qZ2bTXp9DP0mMM'
CONSUMER_SECRET = 'IpMHYmnPRn7WwgHOI53kQlrkkODF7f8YuhThpJaVAh6Z68c2Et'
ACCESS_TOKEN_KEY = '910126134305619968-JQv0GDU4jJTnHiuaKAvfQ34Kf0UOvds'
ACCESS_TOKEN_SECRET = 'vL6TxeI4NT8nhU9Lm1xW9b6hoaSe19fLUpVy5Gf7S9MsD'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#filename=open(argfile, 'r')
#f=filename.readlines()
#filename.close()

#for line in f:
#    api.update_status(line)
#    time.sleep(1)#Tweet every 15 minutes


#api.update_status(status="")d


#def search_tweets(ifnskola, count=100):
#    return bot.search.tweets(ifnskola=ifnskola, result_type='recent', count=count)


    #follow4follow
#for follower in tweepy.Cursor(api.followers).items():
#    follower.follow()
#    print follower.screen_name

"""
for follower in tweepy.Cursor(api.search, q="#skoldag").items():
    api.create_friendship
    print(follower)
    time.sleep(0.5)  # take a sleep for in sec

"""
"""
var = 1
while var == 1:
    for tweet in tweepy.Cursor(api.user_timeline, id=25073877).items(1):
        try:
            var = 1
            while var == 1:
                print(tweet)
                tweet.retweet()
                time.sleep(2)  # take a sleep for in sec

        except tweepy.TweepError as e:
            print(e.reason)  # if cant Retweet tweets, print the reason

        except StopIteration:
            break


"""



for tweet in tweepy.Cursor(api.search, q="#svpol").items():
    try:
        # Add \n escape character to print() to organize tweets
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found
        #tweet.retweet()
        #print('Retweeted the tweet')


        #tweet = api.user_timeline(id=api.user_timeline, count=1)[0]
        #print(tweet.text)

        #Favorite the tweet
        #tweet.favorite()
        #print('Favorited the tweet')

        # Follow the user who tweeted
        #if not tweet.user.following:
        tweet.user.follow()
        print('Followed the user')

        time.sleep(10)  # take a sleep for in sec

    except tweepy.TweepError as e:
        print(e.reason)  # if cant Retweet tweets, print the reason

    except StopIteration:
        break
