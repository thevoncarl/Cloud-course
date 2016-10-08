from parse_json import parser
import urllib2



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

for line in items.split('\n'):
    fileUrl = url + "/" + str(line)
    result = parser.delay(fileUrl)
    #while(result.ready() == False):
    #	pass

    han,hon,den,det,denna,denne,hen,tweets = result.get()
    total_han += han
    total_hon += hon
    total_den += den
    total_det += det
    total_denna += denna
    total_denne += denne
    total_hen += hen
    total_tweets += tweets
   

print total_han 
print total_hon 
print total_den 
print total_det 
print total_denna
print total_denne 
print total_hen
print total_tweets