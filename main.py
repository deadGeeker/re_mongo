# import sys
from pymongo import MongoClient
from bson.son import SON

client = MongoClient(host='localhost')
users = client.test.users


def get_rank(user_id):
    s = users.aggregate([
        {
            '$group': {
                '_id': '$user_id',
                'sum_score': {
                    '$sum': '$score'
                },
                'sum_minutes': {
                    '$sum': '$submit_time'
                }
            }
        },
        {
            '$sort':
                SON([
                    ('sum_score', -1),
                    ('sum_minutes', 1)
                ])
        }
    ])
    for i, j in enumerate(s, 1):
        if j['_id'] == user_id:
            return i, j['sum_score'], j['sum_minutes']


c = get_rank(int(1))
print(c)
