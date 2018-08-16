import pymongo
import pprint
from pymongo import MongoClient
client = MongoClient()
db = client.shiyanlou
contests = db.contests
pprint.pprint(contests.find_one({'user_id':3}))
contest_order_by_score = contests.aggregate([{'$group':{'use_id':'$user_id','total_score':{'$sum':'$score'},'total_time':{'$sum':'$submit_time'}}}])
for x in contest_order_by_score:
    print(x)
