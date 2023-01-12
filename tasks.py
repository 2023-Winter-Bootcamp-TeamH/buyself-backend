from celery import Celery
from detect import predict

app = Celery('tasks',
             broker='amqp://buyself:buyself@localhost//',
             backend='rpc://buyself:buyself@localhost//')

@app.task
def prediction():
    return predict()