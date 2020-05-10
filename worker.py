#this is my worker listening for the atsk Queues .
import redis
import os
from rq import Worker,Queue,Connection
#listen is the queue named default .
listen=['default']

#redis_url=os.getenv(varname='REDISTOGO_URL',value='redis://localhost:6379')
redis_url='redis://localhost:6379'
conn=redis.from_url(redis_url)

if __name__=='main':
    with Connection(conn):
        worker=Worker(list(map(Queue,listen)))
        worker.work()