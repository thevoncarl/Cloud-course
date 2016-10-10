import os
import json
import urllib2
import re
from celery import Celery

app = Celery('item ', backend='rpc://', broker='amqp://test:test@192.168.0.246')

@app.task
def parser(url):
    han = 0
    hon = 0
    den = 0
    det = 0
    denna = 0
    denne = 0
    hen = 0
    tweets = 0

    html = urllib2.urlopen(url).read()

    data = []
    for line in html.split('\n'):
        try:
            data.append(json.loads(line))
        except ValueError:
            x = 0


    for i in data:
        if i.get('retweeted_status') == None:
            tweets = tweets + 1
            text = (i) ['text']
            if re.search(' han ', text, re.IGNORECASE):
                han += 1
            if re.search(' hon ', text, re.IGNORECASE):
            	hon += 1
            if re.search(' den ', text, re.IGNORECASE):
                den += 1
            if re.search(' det ', text, re.IGNORECASE):
                det += 1
            if re.search(' denna ', text, re.IGNORECASE):
                denna += 1
            if re.search(' denne ', text, re.IGNORECASE):
                denne += 1
            if re.search(' hen ', text, re.IGNORECASE):
                hen += 1



    return  han,hon,den,det,denna,denne,hen,tweets   
