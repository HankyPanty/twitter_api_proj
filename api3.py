import json
import time
import os
import fileinput

fileee = open('pr_file.txt','r')
fill = open('fill.txt','w')
fill.write('tweet_number,tweet_date_and_time,is_account_verified,user_country,profile_link');
fill.write('\n');
inn=0;
alpha = json.loads(fileee.read())
while inn< len(alpha["data_all"]):
    data= alpha["data_all"][inn]               
    
    fill.write(str(data['id']))
    fill.write(',')
    fill.write(str(data['created_at']))
    fill.write(',')
    fill.write(str(data['user']['verified']))
    fill.write(',')
    
    fill.write( str(data['place']['country_code']) if data['place'] else "N/A" )
    fill.write(',')
    fill.write(str(data['user']['id_str']))
    fill.write('\n')
    inn= inn+1;

fill.close();
fileee.close();
