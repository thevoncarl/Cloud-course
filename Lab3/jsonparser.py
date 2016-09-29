
import json


#fp = open("Jsonfiles/05cb5036-2170-401b-947d-68f9191b21c6")
#json_string = fp.readline()
#tweets.append(json.loads(json_string))
#fp.close()

#f = open( "Jsonfiles/05cb5036-2170-401b-947d-68f9191b21c6", "r" )

#for line in f:
#    tweets.append(json.loads(line))

#with open("Jsonfiles/05cb5036-2170-401b-947d-68f9191b21c6", "r") as fp:
#    for line in fp:
#	json_string = line
#    	tweets.append(json.loads(json_string))

#EAFP
data = []
with open("Jsonfiles/05cb5036-2170-401b-947d-68f9191b21c6") as f:
    for line in f:
        try:
            data.append(json.loads(line))
        except ValueError:
            x = 0
        
           
han = 0
hon = 0
den = 0
det = 0
denna = 0
denne = 0
hen = 0
tweets = 0

for i in data:
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
    
    


print "Han: " + str(han)
print "Hon: " + str(hon)
print "Den: " + str(den)
print "Det: " + str(det)
print "Denna: " + str(denna)
print "Denne: " + str(denne)
print "Hen: " + str(hen)
print "Total nr of unique tweets: " + str(tweets)

#da[0]['in_reply_to_screen_name'])
