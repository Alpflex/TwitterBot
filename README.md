
# TwitterBot
A Python 2.7 bot that automates several actions on Twitter.

## Disclaimer

I hold no responsibility for what you do with this bot or what happens to you by using this bot. Abusing this bot can get you banned from Twitter, so make sure to read up on proper usage of the Twitter API.

## Getting Started


### Installation

You can install the Twitter Follow Bot using git:
```
git clone https://github.com/Alpflex/TwitterBot.git
```
### Prerequisites

You will also need to create an app account on https://dev.twitter.com/apps

    Sign in with your Twitter account
    Create a new app account
    Modify the settings for that app account to allow read & write
    Generate a new OAuth token with those permissions



## Usage
### Configuring the bot

First you need to open the TwitterBot.py file and start edit some code. 

Before running the bot, you must first set it up so it can connect to the Twitter API. Create a config.txt file and fill in the following information:

    CONSUMER_KEY = ' '
    CONSUMER_SECRET = ' '
    ACCESS_TOKEN_KEY = ' '
    ACCESS_TOKEN_SECRET = 

CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET are your API keys that you received from creating your app account. Is your Twitter name, case-sensitive.

### Edit


    while True:
        for tweet in tweepy.Cursor(api.user_timeline, id=USER_ID).items(1):
            try:
                while True:
                    print(tweet)
                    tweet.retweet()
                    time.sleep(1)  # take a sleep for in sec

            except tweepy.TweepError as e:
                print(e.reason)  # if cant Retweet tweets, print the reason

            except StopIteration:
                break

You can look up a users' Twitter ID [here](http://mytwitterid.com/).
Change "USER_ID" at the first line of code to your desire users id.

### Finished

When you are finished with the code you can start hosting the bot.

    
## Have questions? Need help with the bot Or Want to improve it??

If you're having issues with or have questions about the bot, 
