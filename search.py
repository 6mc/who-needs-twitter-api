from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(['are']) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        CONSUMER_KEY = 'get urself a new one',
        consumer_secret = 'get urself a new one',
        access_token = 'get urself a new one-get urself a new one',
        access_token_secret = 'get urself a new one'
     )
     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
           fh = open("tweets.txt", "a")
           fh.write("\n" +tweet['text'] + "\n")
           fh.close()
           print(tweet['text'].split("are"))
           print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
           
except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print('gunes')