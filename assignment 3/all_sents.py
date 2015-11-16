# Alexander Priest
from sentiment import *

def infer_word_sentiments(codes, text):
	sents = {}
	for item in text:
		if not item == None:
			score = sentiment_score(codes, item)
			punct = standard_punct_list()
			clean_text = ''.join(map(lambda x: remove_punct(x, punct), item)).lower()
			words = filter(lambda x: x != '', clean_text.split(' '))
			for word in words:
				if not codes.has_key(word):
					if not sents.has_key(word):
						sents[word] = (0,0)
					sents[word] = tuple(map(lambda x, y: x + y, sents[word], (score, 1)))
	for word in sents:
		sents[word] = sents[word][0] /sents[word][1]
	return sents

def infer_tweet_word_sentiments(codes, tweets):
	text_list = []
	for tweet in tweets:
		#print(tweet)
		#print text(tweet)
		text_list.append(text(tweet))
	return infer_word_sentiments(codes, text_list)

def top_n_words(sentiment_score_dict, n, direction=1):
	srt = sorted(sentiment_score_dict.items(),key = lambda x : x[1])
	if direction == 1:
		srt.reverse()
	return srt[:n]
		
def build_word_cloud_list(sentiment_score_dict, n, filename, direction=1):
	sents = top_n_words(sentiment_score_dict, n, direction)
	file = open(filename, 'w')
	for word_score in sents:
		for i in range(int(word_score[1] * 100)):
			file.write(word_score[0])
			file.write('\n')
	file.close()

