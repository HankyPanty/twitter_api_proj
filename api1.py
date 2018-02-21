from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time
import os
import fileinput

ckey = 'Xw35ARp6ft61E9UK2UESi3Uxc'
csecret = 'XCLaTEYZ2OThn1cXtszYMLGo3E4wXsx3wXs7GOZmg2u6KPcdzI'
atoken = '899221581641154560-XNC2WqYSBEazmYD0v5b0TNZLk3EmAOU'
asecret = 'xLNngkHwTcIwSLoznZdF4124OZh2FjWsicLqwdq49U1NO'

class data_listener(StreamListener):
    try:
        def on_data(self, data):
            #live data comes here. One tweet by one
            pr_file = open('pr_file.txt','r+')
            pr_file.seek(0, os.SEEK_END)
            pos = pr_file.tell() - 1
            while (pos > 0 and pr_file.read(1) != "\n"):
                pos -= 1
                pr_file.seek(pos, os.SEEK_SET)
            if pos > 0:
                pr_file.seek(pos, os.SEEK_SET)
                pr_file.truncate()
            pr_file.write(',')
            pr_file.write(data)
            pr_file.write('\n ]}')
            pr_file.close();
            
            f=open('pr_file.txt','r')
            olddata=f.read()
            f.close();
            olddata = olddata.replace('[ ,','[  ');
            f=open('pr_file.txt','w')
            f.write(olddata)
            f.close();
            return True
    except (BaseException,e):
        print('failed on the following data:',str(e));
        time.sleep(5);
    def on_load(self, status):
        print (status);

auth= OAuthHandler(ckey, csecret)
auth.set_access_token(atoken,asecret)

pr_file = open('pr_file.txt','w')
pr_file.write("{ \"data_all\" : [ \n")
pr_file.close();
twitterStream= Stream(auth,data_listener())
start = time.time();
twitterStream.filter(track=['carbon'],filter_level='medium'.encode('utf-8'));
#very big query!!
# print("The query took %f seconds!" % (time.time() - start))