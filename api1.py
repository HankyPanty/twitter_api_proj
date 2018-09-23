from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import time
import os
import fileinput
count =0;

ckey = 'DLJALiegzKXuQQQprO0e1Gmwz'
csecret = 'zjXT44wJ9CTFuqcaHOFwKGwQoHE8GLpu3tb4zWi6U2AZ2iacf2'
atoken = '899221581641154560-blDens6h7KSOTqFxjggcFK3Liuav07f'
asecret = 'hRRW7LWHBDkBY5QDpqrtTzEc29ofDuS5ulfgXnjdI7s8w'

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
            global count;
            olddata=f.read()
            f.close();
            olddata = olddata.replace('[ ,','[  ');
            f=open('pr_file.txt','w')
            f.write(olddata)
            f.close();
            count=count + 1;
            ##Change value of count to limit the input tweets...
            if count==50:
                return False
            print(count);
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
twitterStream= Stream(auth,data_listener(count))
start = time.time();
twitterStream.filter(track=["Modi"]);

print("The query took %f seconds! \n" % (time.time() - start));
count=0;