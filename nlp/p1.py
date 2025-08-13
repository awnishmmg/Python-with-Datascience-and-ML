## wap in python to Text Processing and Tokenisation

import nltk
#nltk.download('punkt')
#nltk.download('punkt_tab') # open source model w

from nltk.tokenize import sent_tokenize
#corpus :collection of mutliple sentences
# sentences Full stop (.) seperated
corpus = '''
    Mr. Awnish is Hero and Ms. Katrina is Herion.
    Katrina Likes Awnish. Awnish Like Sunny.  
'''
print(corpus)
documents  = sent_tokenize(corpus)
print(documents)

for document in documents:
    print(document)


print(f'No of documents = {len(documents)}')

# word tokenisation 
# No of tokenizer in the NLTP 
# 1. word tokenizer : general or grammer based
# 2. Regex tokenizer : Rules based or Regex Based
# 3. Tweet tokenizer : social media,Ads related,post (intagram,blogs,email,messenger,whatsApp)

from nltk.tokenize import word_tokenize,RegexpTokenizer,TweetTokenizer
words  =  word_tokenize(text=corpus)
print('word tokenizer :',words)

regex_tokenizer = RegexpTokenizer(r'\w+')
words_2 = regex_tokenizer.tokenize(corpus)
print('Regex Tokenizer :',words_2)


# Enable the Emoji in console 
import sys 
sys.stdout.reconfigure(encoding='utf-8')
# Tweet Tokenizer
tweet = "I Love Samosa 😎"
tweet_tokenizer = TweetTokenizer()
words_3 = tweet_tokenizer.tokenize(tweet)
print('Tweet Tokenizer:',words_3)

vocabs1 = set([word.lower() for word in words])
print('vocabs:',vocabs1)
print(f' total words = {len(words)} and vocabs = {len(vocabs1)}')

grammer =  frozenset(vocabs1)
print('Grammer :',grammer)



