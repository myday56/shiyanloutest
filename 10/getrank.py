# -*- coding:utf-8 -*-

import sys
from pymongo import MongoClient

def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests
    
    

    return rank,score,submit_time

if __name__ == '__main__':
    
    TODO

    userdata = get_rank(user_id)
    print(userdata)
