import json
from bson import json_util
import pymongo
from pymongo import MongoClient

con = MongoClient('localhost:27017')

con.database_names()
db = con.database

with open('pr_file.txt', 'r') as f:
    data=json_util.loads(f.read());

posts=db.posts
posts.insert(data["data_all"])
ppl_all=posts.find()


ppl=posts.find({'created_at':'Tue Feb 20 21:02:59 +0000 2018'})

date_sort=ppl.sort([("created_at", pymongo.ASCENDING), ("user.name", pymongo.ASCENDING)])

for tts in date_sort:
    print(tts,'\n \n')
    
for tts in date_sort:
    date_sort.remove(tts)