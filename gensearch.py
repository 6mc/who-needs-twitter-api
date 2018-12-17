import sys
print(sys.argv[1])

from TwitterSearch import *
try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords([sys.argv[1]]) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see German tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
      Consumer_key = 'GET_IT_FROM_TWITTER',
        consumer_secret = 'GET_IT_FROM_TWITTER',
        access_token = 'GET_IT_FROM_TWITTER-GET_IT_FROM_TWITTER',
        access_token_secret = 'GET_IT_FROM_TWITTER'
     )
     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
           fh = open(sys.argv[1]+"tweets.txt", "a")
           fh.write(tweet['text'] + "\n")
           fh.close()
           print(tweet['text'].split(sys.argv[1]))
           print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
           
except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print('gunaydin')
