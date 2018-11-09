import numpy as np
import pandas as pd

pip.main(['install','twitter'])

import twitter
from twitter import Twitter
from twitter import OAuth
from twitter import TwitterHTTPError
from twitter import TwitterStream

ck = 'CP7fgUIajeNTjx2GWAOw8gJLn'
cs = 'EW8cDRlfKrF3D91n1OdwqZPtWs2AVy3MqFH7Zxm7usx3f9qkJT'
at = '498725176-adTcq6fMyqlzvEINcg8ujCxUT2f4TafNsLJFg2yx'
ats = 'q94CVXaaAmHXuhQqjL4b26Q5Vdl5lx5PJhQT8f4M6nvfm'

oauth = OAuth(at,ats,ck,cs)
twit_api = Twitter(auth=oauth)
t_loc = twit_api.trends.available()
t_loc

ts = TwitterStream(auth=oauth)

iterator = ts.statuses.filter(track="Bitcoin", language="en")

b = []
for t in iterator:
    b.append(t)
    if len(b) == 50:
        break
len(b)    

import json
from pandas.io.json import json_normalize

df = json_normalize(b)

df.head()
list(df.columns)
df.shape

df['text']
df['id']
df['created_at']
df['user.id']
df['user.name']
df['user.screen_name']
df['entities.hashtags']


twit_api = Twitter(auth=oauth)
t_loc = twit_api.trends.available()
t_loc_df = json_normalize(t_loc)

t_loc_df.head()
t_loc_df[t_loc_df['country']=='India']
t_loc_df[t_loc_df['country']=='France']

la_trends = twit_api.trends.place(_id = 2295411)
la_trends
la_df = json_normalize(la_trends,'trends')
la_df.head()

list(la_df['name'].unique())

res = twit_api.search.tweets(q='Marvel', count= 100)
resdf = json_normalize(res, 'statuses')
list(resdf.columns)

resdf['text']

res2 = twit_api.search.tweets(q='Marvel', count= 100, until='2018-02-05')
resdf2= json_normalize(res2, 'statuses')

resdf['created_at'].min()
resdf2['created_at'].max()

mid = resdf['id'].min()
mid = mid -1

res3 = twit_api.search.tweets(q='Marvel', count= 100, max_id=mid)
resdf3= json_normalize(res2, 'statuses')

resdf['created_at'].min()
resdf3['created_at'].max()
resdf['id'].min()
resdf3['id'].max()