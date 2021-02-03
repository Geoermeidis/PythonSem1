import tweepy
import re
from tweepy import API

api_key = ""
secret_key = ""
bearer_token = ""

auth = tweepy.OAuthHandler(api_key, secret_key)  # authenticate the user

api = tweepy.API(auth)

user = input("Give me a user name: ")
user_tweets = api.user_timeline(user, tweet_mode="extended")  # get tweets from a user

tweets = []
i = 0

for tweet in user_tweets:
    tweets.append(tweet.full_text)  # get last 10 tweets of the user specified
    i += 1
    if i == 10:
        break

# print(tweets)
final_tweets = []

for tweet in tweets:
    tweet_list = tweet.split(" ")
    i = 0

    while i < len(tweet_list):  # delete @ and links
        if "@" in tweet_list[i] or "https" in tweet_list[i]:
            del tweet_list[i]
            i -= 1
        else:
            i += 1
    temp_tweet = " ".join(tweet_list)

    i = 0
    new_tweet = ""
    for char in temp_tweet:  # keep only letters and spaces
        if char.isalpha() or char == " ":
            new_tweet += char
    final_tweets.append(new_tweet)

words = []

for tweet in final_tweets:  # make one list for every word in the last ten tweets
    temp_tweet = tweet.split(" ")
    for temp in temp_tweet:
        if temp != "":
            words.append(temp)

my_dict = {}

for word in words:
    my_dict[word] = len(word)

sorted_keys = sorted(my_dict, key=my_dict.get, reverse=False)

short = ",".join(sorted_keys[0:5])
long = ",".join(sorted_keys[-5::])
print(f"Five shortest words are {short}, and the five longest words are {long}")
