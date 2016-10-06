
import os
import swiftclient.client
import json

from celery import Celery

#app = Celery('tasks', broker='amqp://guest@localhost//')

app = Celery('item ', backend='rpc://', broker='amqp://')

@app.task
def parser():
    config = {'user':os.environ['OS_USERNAME'], 
              'key':os.environ['OS_PASSWORD'],
              'tenant_name':os.environ['OS_TENANT_NAME'],
              'authurl':os.environ['OS_AUTH_URL']}

    
    
    conn = swiftclient.client.Connection(auth_version=3, **config)
    
    container_name = 'tweets'
    
    #obj_tuple = conn.get_object('tweets', 'file.txt')
   
    
    han = 0
    hon = 0
    den = 0
    det = 0
    denna = 0
    denne = 0
    hen = 0
    tweets = 0

    for data in conn.get_container(container_name)[1]:
        #obj_tuple = conn.get_object(container_name,'05cb5036-2170-401b-947d-68f9191b21c6') #  data['name'])
        
        #down_res = conn.download(container=container,objects=data);
        print "Retrieving item: " + data['name']
        
        obj_tuple = conn.get_object(container_name, data['name'])
        with open('item.txt', 'w') as item:
            item.write(obj_tuple[1])

            data1 = []
        with open('item.txt') as f:
            for line in f:
                try:
                    data1.append(json.loads(line))
                except ValueError:
                    x = 0
                
                

        for i in data1:
            if i.get('retweeted_status') == None:  #Better than to check: (if not retweeted_status in i)
                tweets = tweets + 1
                text = (i) ['text']
                if " han " in text:
                    han += 1
                if " hon " in text:
                    hon += 1
                if " den " in text:
                    den += 1
                if " det " in text:
                    det += 1
                if " denna " in text:
                    denna += 1
                if " denne " in text:
                    denne += 1
                if " hen " in text:
                    hen += 1
                
    
                    #print '{0}\t{1}\t{2}'.format(data['name'], data['bytes'], data['last_modified'])
                    
                    

    os.remove('item.txt')
    #return  han,hon,den,det,denna,denne,hen,tweets             

    print "Han: " + str(han)
    print "Hon: " + str(hon)
    print "Den: " + str(den)
    print "Det: " + str(det)
    print "Denna: " + str(denna)
    print "Denne: " + str(denne)
    print "Hen: " + str(hen)
    print "Total nr of unique tweets: " + str(tweets)

parser()
