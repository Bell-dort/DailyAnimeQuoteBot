import tweepy
import csv

from dataset import Dataset
from tweet import Tweet

BEARER_TOKEN = "D84TK5_PU36OYeYYiT_k7SQ5Z1Cp4q_VDA7JZxK6cxUMeKAEvn"

API_KEY = "sv7EIwJn28AfiQzJ49Rw34T6G"
API_SECRET = "dyoUFLUlcMpmYjPTdCGfdLVPLPW23pqTTfPSCJsc6Z31s6YrJV"

ACCESS_TOKEN = "1573285587041370112-3rPdp9tgA59BllcC3cv2YRjUy9e1sD"
ACCESS_TOKEN_SECRET = "MvrXHnbXBGjilv34deM88wRbLBQmTA7e8amFNF48FFL0C"

filename = "AnimeQuotes.csv"

if __name__ == "__main__":
    dataset = Dataset(filename)
    dataset.load()
    row = dataset.get_random_row()
    print(row)
    tweet = Tweet(row)
    tweet.load()
    client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


    # client.create_tweet(text = "yes")
