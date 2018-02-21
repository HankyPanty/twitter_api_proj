# Twitter API Assignment
### Innovaccer API Engineering Assignment

The code is divided in three parts:

1. api1.py
2. api2.py
3. api3.py

### Working of the code:

1. In this code segement, the twitter api is called using the library **tweepy**. The api request is **Stream** and returns realtime tweets. Each tweet is entered line-by-line in the `pr_file.txt` file and stored in **json** format. As the SteamListener functiion of tweepy is used, the kernal needs to be manully stopped to halt the api1.py file to stop running and storing tweets.

## Note: as te api1.py application runs, the file pr_file.txt keeps adding tweets on its list, after sufficient tweets, you must stop the code.

2. In this, the tweets can be sorted, filtered and displayed according to the requirement. I used **pymongo** a **nosql** library for python of **mongodb**. The tweets can be filtered by changing the values of variable **ppl** and **data_sort**. by changing the paramaters of `ppl=posts.find()` we can get required results.

3. In this segement I extracted the important text from `pr_file.txt` and converted the data to **csv format** and returned in `list.txt` file. 
