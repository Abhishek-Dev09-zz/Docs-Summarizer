#Text summarizer, a standalone command line tools which produces summary of article on console itself. 

from nltk.corpus import stopwords 
from nltk.tokenize import sent_tokenize, word_tokenize
import heapq
import re

File = input("Enter a News article file: ")
with open(File, 'r') as file:
    text = file.read()

# convert some odd puncations which can't be recognized by NLTK
text = text.replace('“','"')
text = text.replace('”','"')
text = text.replace("’","'")

# Removing Square Brackets and Extra Spaces
text = re.sub(r'\[[0-9]*\]', ' ', text)
text = re.sub(r'\s+', ' ', text)

# Removing special characters and digits
formatted_article_text = re.sub('[^a-zA-Z]', ' ', text )
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)

sentence_list = sent_tokenize(text)

stop_words = set(stopwords.words('english')) 

word_frequencies = {}
for word in word_tokenize(formatted_article_text):
    if word not in stop_words:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1

maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

sentence_scores = {}
for sent in sentence_list:
    for word in word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]

# We use the heapq library and call  nlargest function to get the top 7 sentences with the highest scores.
summary_sentences = heapq.nlargest(5, sentence_scores, key=sentence_scores.get)
3
summary = ' '.join(summary_sentences)
print(summary)