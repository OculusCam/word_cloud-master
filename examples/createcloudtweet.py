#!/usr/bin/env python2

from os import path
import sys
import wordcloud
from twython import Twython, TwythonError
import glob
import os as globby

APP_KEY="5D2qAHz3RbrR5xHxgg9nQ"
APP_SECRET="0zg8HTnA4ibhXV4M4i4rJUNy5xdaA0DwVk35atY8o"
OAUTH_TOKEN="2303879557-cQmezLl1sFxOZiEVjLgrERce5ybcB2P1c1qc8q4"
OAUTH_TOKEN_SECRET="ejk5YJBgOtUeMUtMwd9X0opnKAnH8rJHnEYlqoeXafCmM"

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


newest = max(glob.iglob('*.png'), key=globby.path.getctime)

newesttext = max(glob.iglob('*.txt'), key=globby.path.getctime)


d = path.dirname(__file__)


# Read the whole text.
text = open(path.join(d, newesttext)).read()
# Separate into a list of (word, frequency).
words = wordcloud.process_text(text)
#for tweet in words:
#    print(tweet)
# Compute the position of the words.
elements = wordcloud.fit_words(words)
# Draw the positioned words to a PNG file.
newesttext=newesttext[:-4]
trend = "#"+ newesttext
newesttext = newesttext + ".png"
wordcloud.draw(elements, path.join(d, newesttext))


#photo = open(str(newest), 'rb')
#twitter.update_status_with_media(status=trend, media=photo)