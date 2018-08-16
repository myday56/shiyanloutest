import sys
import pprint
from pymongo import MongoClient
client = MongoClient()
db = client.shiyanlou
contests = db.contests
contest_order_by_score = contests.aggregate(
        [
        {'$group':
            {'_id':'$user_id',
            'total_score':{'$sum':'$score'},
            'total_time':{'$sum':'$submit_time'}
            }
        },
        {'$sort':
            {'total_score':-1},
        }
        ])
rank_start = 1
user_rank_rs = {}
user_rank_details = []
for i in contest_order_by_score:
    user_rank_details =[rank_start,i['total_score'],i['total_time']]
    rank_start += 1
    user_rank_rs[i['_id']] = user_rank_details
# print(user_rank_rs[2][0])
rank = user_rank_rs[2][0]
score = user_rank_rs[2][1]
submit_time = user_rank_rs[2][2]
print(rank,score,submit_time)




     