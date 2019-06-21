import pandas
from pymongo import MongoClient
df = pandas.read_csv("C:\\Users\\snehabhat\\Desktop\\Data\\movies (1).csv")
#print(df)

d={}
t={}

m=list(df['LICENSE STATUS'])

lcnp=m.count('Not Pass')
lcp=m.count('Pass')
t={'np':lcnp,'p':lcp}


d['no of TITLEs']=len(df['TITLE'])
d['LICENSE STATUS']=t
d.update({'title':'voot'})

f=(list(df['IS CHARGED']).count('Free'))
c=(list(df['IS CHARGED']).count('Charged'))

t={}
t['Free']=f
t['Charged']=c
d.update({'IS CHARGED':t})
t={}
t['null']=df['LANGUAGES'].isnull().sum() 
t['not null']=df['LANGUAGES'].notnull().sum() 
d.update({'languages':t})

n=df['GENRES'].isnull().sum()
nn=df['GENRES'].notnull().sum()

t={}
t['not null']=nn
t['null']=n
d.update({'genres':t})

t['null']=df['PRODUCER'].isnull().sum()
t['not null']=df['PRODUCER'].notnull().sum()
d.update({'producer':t})


t['null']=df['CAST'].isnull().sum()
t['not null']=df['CAST'].notnull().sum()
d.update({'CAST':t})

t['null']=df['YEAR'].isnull().sum()
t['not null']=df['YEAR'].notnull().sum()
d.update({'YEAR':t})


t['null']=df['DIRECTOR'].isnull().sum()
t['not null']=df['DIRECTOR'].notnull().sum()
d.update({'DIRECTOR':t})

t['null']=df['PUBLISHER'].isnull().sum()
t['not null']=df['PUBLISHER'].notnull().sum()
d.update({'PUBLISHER':t})

t['null']=df['PUBLISH STATUS'].isnull().sum()
t['not null']=df['PUBLISH STATUS'].notnull().sum()
d.update({'PUBLISH STATUS':t})


t['null']=df['CATEGORY'].isnull().sum()
t['not null']=df['CATEGORY'].notnull().sum()
d.update({'CATEGORY':t})

try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB") 
    
client = MongoClient('localhost',27017)
db = client['all_cps']
col = db['cms_voot']
#
#col.insert(d)

print(d)


 
