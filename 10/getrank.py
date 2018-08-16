# -*- coding:utf-8 -*-
import sys
from pymongo import MongoClient

def get_rank(user_id):
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
    
    # print(len(user_rank_rs))
    rank = user_rank_rs[user_id][0]
    score = user_rank_rs[user_id][1]
    submit_time = user_rank_rs[user_id][2]
    return rank,score,submit_time

if __name__ == '__main__':
    try:
        user_id = int(sys.argv[1])
    except ValueError:
        print("Parameter Error")
    else:
        userdata = get_rank(user_id)
        print(userdata)
