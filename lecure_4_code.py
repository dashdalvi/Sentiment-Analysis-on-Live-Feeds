import numpy as np
import pandas as pd
import json
import pip
pip.main(['install','twitter'])
pip.main(['install','textblob'])

from textblob import TextBlob
!python -m textblob.download_corpora

import twitter
from twitter import Twitter
from twitter import OAuth
from twitter import TwitterHTTPError
from twitter import TwitterStream
from pandas.io.json import json_normalize

ck = 'CP7fgUIajeNTjx2GWAOw8gJLn'
cs = 'EW8cDRlfKrF3D91n1OdwqZPtWs2AVy3MqFH7Zxm7usx3f9qkJT'
at = '498725176-adTcq6fMyqlzvEINcg8ujCxUT2f4TafNsLJFg2yx'
ats = 'q94CVXaaAmHXuhQqjL4b26Q5Vdl5lx5PJhQT8f4M6nvfm'

oauth = OAuth(at,ats,ck,cs)
api = Twitter(auth=oauth)

t_loc = api.trends.available()
loc_df = json_normalize(t_loc)
loc_df[(loc_df['countryCode']=='US') & loc_df['name'].str.contains('New')]
ny_trends = api.trends.place(_id = '2459115')
nydf = json_normalize(ny_trends,'trends')
nydf.head()
nydf.sort_values('tweet_volume',ascending=False).head(5)

q= 'StudentsStandUp'
df = pd.DataFrame()
mid = 0
for i in range(10):
    if i==0:
        search_result = api.search.tweets(q=q, count = 100)
    else:
        search_result = api.search.tweets(q=q, count = 100, max_id=mid)
    
    dftemp =json_normalize(search_result,'statuses')
    mid = dftemp['id'].min()
    mid = mid - 1
    df = df.append(dftemp, ignore_index= True)
    
df.shape

tweettext = df['text']
blob =TextBlob(tweettext[0])
list(blob.noun_phrases)
blob.tags

wordlist = pd.DataFrame()
for t in tweettext:
    tx = TextBlob(t)
    l = list(tx.noun_phrases)
    if len(l)!=0:
        wordlist = wordlist.append(l,ignore_index=True)

allworld = wordlist.groupby(0).size()    
allworld

top20allworld = allworld.sort_values(0,ascending=False).head(20)
top20allworld.plot(kind='bar',title='Top 20 Tweets')

wordlist = pd.DataFrame()
for t in tweettext:
    tx = TextBlob(t)
    ww = []
    for word,tag in tx.tags:
        if tag in ('NN','NNS','NNP','NNPS'):
            ww.append(word.lemmatize())
    if len(ww) != 0:
        wordlist = wordlist.append(ww, ignore_index=True)

allworld = wordlist.groupby(0).size()    
allworld
    
top20allworld = allworld.sort_values(0,ascending=False).head(20)
top20allworld.plot(kind='bar',title='Top 20 Tweets')    


#lab part 3b
pip.main(['install','newspaper3k'])
import newspaper

url = 'https://www.bloomberg.com/news/articles/2018-02-22/airbnb-is-adding-hotels-and-a-loyalty-program'
article = newspaper.Article(url)
article.download()
article.parse()
article.nlp()
article.title
article.summary
blob2 = TextBlob(article.text)

blob2.sentences[1]

wordlist = pd.DataFrame()
ssList=[]
for t in blob2.sentences:
    ww=[]
    for word, tags in t.tags:
        if tag in ('NN','NNS','NNP','NNPS','VB','VBD','VBG','VBN','VBP','VBZ'):
            ww.append(word.lemmatize())
    ss = ' '.join(ww)
    ssList.append(ss.lower())
wordlist = wordlist.append(ssList, ignore_index=True)

wordlist
len(blob2.sentences)