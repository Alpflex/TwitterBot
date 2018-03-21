
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

Before running the bot, you must first set it up so it can connect to the Twitter API. Create a config.txt file and fill in the following information:

    OAUTH_TOKEN:
    OAUTH_SECRET:
    CONSUMER_KEY:
    CONSUMER_SECRET:
    TWITTER_HANDLE:
    ALREADY_FOLLOWED_FILE:already-followed.txt
    FOLLOWERS_FILE:followers.txt
    FOLLOWS_FILE:following.txt
    USERS_KEEP_FOLLOWING:
    USERS_KEEP_UNMUTED:
    USERS_KEEP_MUTED:
    FOLLOW_BACKOFF_MIN_SECONDS:10
    FOLLOW_BACKOFF_MAX_SECONDS:60

OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET are your API keys that you received from creating your app account. TWITTER_HANDLE is your Twitter name, case-sensitive.

You can change the FILE entries if you want to store that information in a specific location on your computer. By default, the files will be created in your current directory.

Add comma-separated Twitter user IDs to the USERS_KEEP entries to:

    USERS_KEEP_FOLLOWING: Keep following these users even if they don't follow you back.

    USERS_KEEP_UNMUTED: Keep these users unmuted (i.e., you receive a mobile notification when they tweet)

    USERS_KEEP_MUTED: Keep these users muted (i.e., you don't receive a mobile notification when they tweet)

For example:

    ...
    FOLLOWS_FILE:following.txt
    USERS_KEEP_FOLLOWING:1234,1235,1236
    USERS_KEEP_UNMUTED:
    ...

