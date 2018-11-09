import numpy as np
import pandas as pd
from pandas.io.json import json_normalize

import pip
pip.main(['install','yelp3'])
from yelp3.client import Client
 
apikey='TYswCSeIquE5yi_vsCV7Jw56SoNPb8_OSpHl7M0GGJTdNvglrIvdqfrXoIPyvaBglPTx4g4El6XbmDZ4q8owYtkZRYE9dZXF8aYImB0GkrAAsWyFfzrFPML6sB2PWnYx'

api = Client(apikey)

val = api.business_search(location="Newark, NJ")
dd = json_normalize(val)
dd.head()

df=json_normalize(val,'businesses')
df.head()

df.columns

df[['name','rating','categories']]
df2 = pd.DataFrame(df['categories'].values.tolist(), columns=['cat1','cat2','cat3'])
df2.head()
dfcat1 = df2['cat1'].apply(pd.Series)
dfcat1

params={'term':'sushi','limit':50}
val2 = api.business_search(location="Newark, NJ",term='sushi',limit=50)
val2 = api.business_search(location="Newark, NJ",**params)

dfs=json_normalize(val2,'businesses')
dfs.head()
dfs[['name','rating','review_count']].sort_values('review_count',ascending=False)

params={'term':'sushi','limit':50,'offset':50}
val3 = api.business_search(location="Newark, NJ",**params)
dfs2 = json_normalize(val3,'businesses')

dfs2[['name','rating','review_count','id']].sort_values('review_count',ascending=False)

fid =dfs.loc[0,'id']
fid

rev = api.review(fid)
rev
dfrev = json_normalize(rev,'reviews')

textlist = dfrev['text'].tolist()

pip.main(['install','textblob'])
from textblob import TextBlob

polarity = []
sub = []
for t in textlist:
    tx = TextBlob(t)
    polarity.append(tx.sentiment.polarity)
    sub.append(tx.sentiment.subjectivity)

pol = np.array(polarity)
pol.mean()
    
dfm = dfs[['name','rating','review_count','id']].append(dfs2[['name','rating','review_count','id']], ignore_index=True)    
dfm.shape
dfs.shape
dfs2.shape

idlist = dfm['id'].tolist()

ps = []
for i in idlist:
    rev = api.review(i)
    dfrev = json_normalize(rev,'reviews')
    textlist = dfrev['text'].tolist()
    polarity = []
    for t in textlist:
        tx = TextBlob(t)
        polarity.append(tx.sentiment.polarity)
    pol = np.array(polarity)
    ps.append(pol.mean())   
        
dfm['pol']=pd.Series(ps)

dfm.sort_values('pol',ascending=False)
dfm2 = dfm[dfm['pol']>=.35]
dfm2.shape        

df['location'][0]