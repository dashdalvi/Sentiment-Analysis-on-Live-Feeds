pip.main(['install','quandl'])
import quandl
qdl = '8pLifuTyA8yKP7xEdFga'

quandl.ApiConfig.api_key=qdl

mydata = quandl.get('ZILLOW/Z08854_TURNAH')

mydata.head()

mydata2 = quandl.get('ZILLOW/Z07029_TURNAH')

mydata.Value.tail(1).tolist()[0]
mydata2.tail()

mdf['zip_code']
mdf['zid']='ZILLOW/Z'+mdf['zip_code']+'_TURNAH'
mdf['zid']

zzid = mdf['zid'].tolist()
zzid

turnah=[]
for i in zzid:
    try:
        mydata = quandl.get(i)
        v=mydata.Value.tail(1).tolist()[0]
        turnah.append(v)
    except:
        turnah.append(0)

zz = mdf['zip_code'].unique()

bb = []
zz2 = 'ZILLOW/Z'+zz.tolist()+'_TURNAH'
zz3 = zz2.tolist()
zz3

del zz3[26]

for i in zz3:
    mydata = quandl.get(i)
    v=mydata.Value.tail(1).tolist()[0]
    bb.append(i)

len(bb)

mdf[mdf['zip_code']=='08818']

turnah[turnah==0]

aturnah = np.array(turnah)
aturnah[aturnah==0]

azzid = np.array(zzid)

azzid[aturnah==0]

mdf['Score']=turnah

mdf.columns

mdf.info()

mdf['rating'].value_counts()

mdf.describe()

mdf.hist(bins=50,figsize=(20,15))

r,c = mdf.shape
test_ratio = .3

si = np.random.permutation(r)
test_set_size = int(r*test_ratio)
test_set_size



test_indices = si[:test_set_size]
train_indices = si[test_set_size:]

train_indices

train_set = mdf.iloc[train_indices]
test_set = mdf.iloc[test_indices]

train_set.shape
test_set.shape

pip.main(['install','sklearn'])
pip.main(['install','scipy'])
from sklearn.model_selection import train_test_split

train_set2, test_set2 = train_test_split(mdf, test_size=.2, random_state=42)

train_set2.shape
test_set2.shape

from sklearn.model_selection import StratifiedShuffleSplit
mdf.rating.value_counts()

split = StratifiedShuffleSplit(n_splits=1, test_size=.3, random_state=42)

for train_indices, test_indices in split.split(mdf, mdf['rating']):
    strat_train_set = mdf.loc[train_indices]
    strat_test_set = mdf.loc[test_indices]
