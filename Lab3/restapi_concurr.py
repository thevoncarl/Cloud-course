from parse_json import parser
import urllib2
from flask import Flask, jsonify
import subprocess
import sys
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def fun():
    url = 'http://130.238.29.253:8080/swift/v1/tweets'
    items = urllib2.urlopen(url).read()
    
    total_han = 0
    total_hon = 0
    total_den = 0
    total_det = 0
    total_denna = 0
    total_denne = 0
    total_hen = 0
    total_tweets = 0
    workers = []
    for line in items.split('\n'):
        fileUrl = url + "/" + str(line)
        result = parser.delay(fileUrl)
        workers.append(result)



    while (len(workers) != 0):
        for task in workers:
	    han,hon,den,det,denna,denne,hen,tweets = task.get()
	    total_han += han
	    total_hon += hon
	    total_den += den
	    total_det += det
	    total_denna += denna
	    total_denne += denne
	    total_hen += hen
	    total_tweets += tweets
            workers.remove(task)

   jsonString = {'han': han, 'hon': hon, "den": den, "det": det, "denna": denna, "denne": denne, "hen": hen, "tweets": tweets}
   return (json.dumps(jsonString))


if __name__ == '__main__':
    
app.run(host='0.0.0.0',debug=True)
