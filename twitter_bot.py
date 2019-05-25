# Dev Notes---
# This is a bot created for automatic replies and answers to the tweets where user has 
# been tagged or questioned. So I am starting this project right now so let's see how
# it will go. This is the Day01

import tweepy
import time
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

# Dev Notes---
# You need to paste your own Keys on the right places as defined
# I have left this clear so that this can be used by anyone

print('Welc0me to Aut0matic Tw33t R3pli3s', flush=True)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# Dev Notes---
# We have set this api object
# This object has been set and this will be talking to Twitter
# Well talking to Twitter means that he will be sending commands(requests actually) to the
# Twitter. This will be talking to Twitter to read data on Twitter and write data on 

FILE_NAME = 'last_seen_id.txt'


def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close
    return

# Dev Notes----



def reply_to_tweets():
    print(" Retrieving and Replying back to the tweets... Hola!!! Enjoy.")

    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mentions(id)) + ' ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#helloworld' in mention.text.lower():
            print('Found Hello World!')
            print('Responding Back...')
            api.update_status('@' + mention.user.screen_name +'#HelloWorld I am writing a piece of code. Love You. HaHa!!!', mention.id)
    
# Dev Notes----
# Below Code was written previously. After then this code was replaced with above one.
# Explaination will in Explainantion.pdf
# Do check that out if you want to know why I did this. Thank You. Peace

#for mention in mentions:
#    print(str(mention.id) + ' ' mention.text)
#   if '#helloworld' in mention.text.lower():
#        print('Found Hello World!')
#       print('Responding Back...')

while True:
    reply_to_tweets()
    time.sleep(15)