import json
from bson import json_util
import pymongo
from pymongo import MongoClient

con = MongoClient('localhost:27017')

con.list_database_names()
db = con.database

with open('pr_file.txt', 'r') as f:
    data=json_util.loads(f.read());

posts=db.posts
posts.insert_many(data["data_all"])
ppl_all=posts.find()


# ppl=posts.find({'created_at':'Tue Feb 20 21:02:59 +0000 2018'})

##conditions for sorting the data--
date_sort=ppl_all.sort([("user.name", pymongo.ASCENDING), ("created_at", pymongo.ASCENDING)])

##printing the sorted data
for tts in date_sort:
    print('(user): ',tts['user']['name'],',  (time): ',tts['created_at'],'\n(tweet):',tts['text'],'\n \n')

##clearing the collection-posts in the database--
db.posts.drop()
# for tts in date_sort:
#     posts.remove(tts)
# date_sort=None;