import numpy as np
import pandas as pd
import pip
!pip install python-craigslist
pip.main(['install','python-craigslist'])

from craigslist import CraigslistHousing
from craigslist import CraigslistJobs

CraigslistHousing.show_filters()

#https://newyork.craigslist.org/d/office-commercial/search/mnh/off
# area = mnh(manhattan), last three letters, off (office&commercial) = (category) 
#https://newyork.craigslist.org/d/office-commercial/search/mnh/aap

cl_h = CraigslistHousing(site='newyork',area= 'mnh',category= 'aap',filters={'zip_code':'10011'})

res =[]
for result in cl_h.get_results(sort_by='newest',geotagged=True):
    res.append(result)

from pandas.io.json import json_normalize
df = json_normalize(res)
df.head()

df.area
df['area2']=df['area'].str[:-3]
df['area3']=pd.to_numeric(df['area2'], errors='coerce')

df.area3
df.columns
df.price
df['price2'] = pd.to_numeric(df.price.str[1:],errors='coerce')
#in the above line, we are removing the $ from price column. for that converting to string and taking every lette after the first one

df.price2

df['lps']=df.price2/df.area3
df.bedrooms

df['bedrooms2']=pd.to_numeric(df.bedrooms,errors='coerce')
df['lpb'] = df.price2/df.bedrooms2
df[['lpb','lps']]

df.head()

gkey = 'AIzaSyDfovAnwYwf_PZlXjZdwQgSSL2oPyiT_Xo'

pip.main(['install','googlemaps'])
import googlemaps

gapi = googlemaps.Client(key=gkey)
dr = gapi.directions("40.7421555, -74.173563","40.756961, -73.990275", mode="driving",avoid="ferries")
dr[0]['legs'][0]['distance']
dr[0]['legs'][0]['duration']

df2 = df.geotag.apply(pd.Series)

df['sgeo'] = df2[0].astype(str)+','+df2[1].astype(str)

df['sgeo']


