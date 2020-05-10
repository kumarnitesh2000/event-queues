from rq import Queue
from rq.job import Job
import requests
from worker import conn
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#app=Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
#init db
#db=SQLAlchemy(app)

def count_and_save_words(url):
    r=requests.get(url)
    return {'html-len':len(r.text.split())}




q=Queue(connection=conn)
url="https://realpython.com/flask-by-example-implementing-a-redis-task-queue/"
job=q.enqueue_call(func=count_and_save_words,args=(url,),ttl=5000)
#ttl is the total time hold
print(job.get_id())


