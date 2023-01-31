from celery import Celery
from detect import predict

app = Celery('tasks',
             broker='amqp://buyselfback:buyselfback@rabbit:5672/',
             backend='rpc://buyselfback:buyselfback@rabbit:5672/',
             include=["tasks"])

@app.task
def prediction(img_name):
    return predict(img_name)