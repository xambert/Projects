import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer
import re
def clean(x:str):
    #remove hyperlink
    tweet = re.sub(r'https?://[^\s\n\r]+','',x)
    #remove hashtags
    tweet = re.sub(r'#', '', tweet)
    #tokenize
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                               reduce_len=True)
    tweet_tokens = tokenizer.tokenize(tweet)
    print(tweet_tokens)


clean("abcdef #u https://fuckyou?suchtht:bitchmoan")



