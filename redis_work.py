"""Basic connection example.
"""

import redis
import datetime

r = redis.Redis(
    host='redis-12333.crce175.eu-north-1-1.ec2.redns.redis-cloud.com',
    port=12333,
    decode_responses=True,
    username="default",
    password="wTCup7gCbimw8BtOgAIJy4evBNDb1iO1",
)

# create new key

# string
# r.set('myKey', 'secret data')
# r.set('myKeyTTL23', 'secret dataTTL32', ex=15)
# r.set('myKeyTTL236666666666', 'secret dataTTL32', exat=datetime.datetime(year=2025, month=5, day=15, hour=3))

# lists
# r.lpush('myList', 'elem1left0')
# r.rpush('myList', 'elem right', 565)
#
# r.expire('myList', 3500)

# read list
# data = r.lrange('myList', 0, -1)
# print(data)


# dicts
# r.hset('user:1235654', mapping={'name': 'Alise', 'age': 56})
# r.hset('user:1235654', mapping={'city': 'Lviv'})
# r.hset('user:1235654', mapping={'age': 15})
# r.expire('user:1235654', 3500)
# data = r.hgetall('user:1235654')
# print(data)


# get data
# data = r.get('myKey')
# print(data)

# delete data
# r.delete('myList')

# r.incr('views', 6)
# print(r.get('views'))


# pub/sub
r.publish('weather', 'from pycharm')


# pubsub = r.pubsub()
# pubsub.subscribe('news')
# pubsub.subscribe('weather')
# for message in pubsub.listen():
#     print(message)









