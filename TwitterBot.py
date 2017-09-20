# !/usr/bin/env python
# -*- coding: utf-8 -*-

#tweepy is the library we will be using to access the Twitter API

import tweepy, time, sys




#argfile = str(sys.argv[1])


#To know that it access to my Bot and not others
CONSUMER_KEY = ''   #your key
CONSUMER_SECRET = ''    #your key
ACCESS_TOKEN_KEY = ''   #your key
ACCESS_TOKEN_SECRET = ''    #your key
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#filename=open(argfile, 'r')
#f=filename.readlines()
#filename.close()

#for line in f:
#    api.update_status(line)
#    time.sleep(1)#Tweet every 15 minutes


#api.update_status(status="")


#def search_tweets(ifnskola, count=100):
#    return bot.search.tweets(ifnskola=ifnskola, result_type='recent', count=count)


for tweet in tweepy.Cursor(api.search, q='#ocean').items():
    try:
        # Add \n escape character to print() to organize tweets
        print('\nTweet by: @' + tweet.user.screen_name)

        # Retweet tweets as they are found
        tweet.retweet()
        print('Retweeted the tweet')

        time.sleep(10)

    except tweepy.TweepError as e:
        print(e.reason)

    except StopIteration:
        break
        
client.login(process.env.BOT_TOKEN);
