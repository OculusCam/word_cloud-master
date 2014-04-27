from twython import Twython, TwythonError
import sys
import os
import json


APP_KEY="5D2qAHz3RbrR5xHxgg9nQ"
APP_SECRET="0zg8HTnA4ibhXV4M4i4rJUNy5xdaA0DwVk35atY8o"
OAUTH_TOKEN="2303879557-cQmezLl1sFxOZiEVjLgrERce5ybcB2P1c1qc8q4"
OAUTH_TOKEN_SECRET="ejk5YJBgOtUeMUtMwd9X0opnKAnH8rJHnEYlqoeXafCmM"

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)


usa = twitter.get_place_trends(id=23424977)
trend_array = []

if usa:
    for trend in usa[0].get('trends', []):
        trend_array.append(trend['name'])
        
        
jsobj = {"A": trend_array}
print json.dumps(jsobj)
        #trend = trend['name']
        
        #search_results  = twitter.search(q=str(trend),lang='en',result_type='popular',count=99)
        #search_results.update(twitter.search(q=str(trend),lang='en',result_type='mixed',count=99))
        #search_results.update(twitter.search(q=str(trend),lang='en',result_type='recent',count=99))
        
        #if search_results:
        #    filenaming = trend + ".txt"
        #    filenames = str(filenaming)
        #    f = open(filenames,'wb')
        #    for tweet in search_results['statuses']:
        #            s = tweet['text'].encode('utf-8')
        #            actual = s + "/n"
        #            f.write(actual)





    
    
