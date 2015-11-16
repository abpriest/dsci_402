from twitter_util import *
from sentiment import *
from all_sents import *

codes = get_sentiment_codes("../util-data-files/AFINN-111.txt")

test = read_tweets("twitter_data/twitter_data.json")
infer = infer_tweet_word_sentiments(codes, test)
print(build_word_cloud_list(infer, 15, "paris.txt", 1))
#build_word_cloud_list(infer, 10, "test.txt", 1)
