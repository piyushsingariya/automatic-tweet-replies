ok Guys Here I am explaining you how this stuff has created!! so let's start

First things First
We need to install quite a few modules so do install them
Open your terminal and write these commands
~pip install tweepy
~pip install times

After this stuff let's get to the explaination

I have defined CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET variables
you need to get these on your own from developer.twitter.com

Into the code we have defined api as an object which will be talking to Twitter
and here talking to Twitter means that he will be sending commands(requests actually) to the
Twitter's webserver '. This will be talking to Twitter to read data on Twitter and write data on 
our account or stuff    

Inside the function reply_to_tweets
you may have seen tweet_mode to be declared as Extended this is because to get
all full tweets (with full_text). Without it, long tweets would be cut off.

We have created a file called "last_seen_id.txt" file becuase our bot is gonna be shutting down in
every 15 seconds and when it will restart it will respond again to the same tweets which have been
responded already. What we have done is
We created a txt file and we retrieved the last seen id of the last tweet we responded with 
the fonction called "retrieve_last_seen_id" here code will get the id's which he should not respond now
because he aleady responded to them in the previous session.

then we defined "store_last_seen_id" to store the id's which are being responded now and which should
not be responded after this session.
I think i have explained you all the stuff i could and i thought i should tell you.
Love You. Peace
