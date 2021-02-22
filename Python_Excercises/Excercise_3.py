import requests
import json
import datetime
import itertools

raw_url_1= "https://api.opap.gr/draws/v3.0/{gameId}/draw-date/{fromDate}/{toDate}/draw-id"
raw_url_2 = "https://api.opap.gr/draws/v3.0/{gameId}/{drawId}"
raw_url_3 = "https://api.opap.gr/games/v1.0/1100/statistics?drawRange=10"
# set the date for each day 
date = datetime.datetime.today().strftime('%Y-%m-%d')
# get all the draw ids for each day
list_1 = raw_url_1.split("/")
list_1[5] = 1100
list_1[7] = date
list_1[8] = date
modified_url_1 ='/'.join([str(item) for item in list_1 ]) 
response_1 = requests.get(modified_url_1)
# convert the data into a dictionary for editing
r = response_1.json()
# select only the first draw of the day (item 0 from the list of draw ids)
draw_id = r[0]
# get the results for the first draw
list_2 = raw_url_2.split("/")
list_2[5] = 1100
list_2[-1] = draw_id
modified_url_2 = '/'.join([str(item) for item in list_2])
response_2 = requests.get(modified_url_2)
# convert the data into a dictionary for editing
statistics = response_2.json()
results = statistics.get('winningNumbers')
winningNumbers = results.get('list')
# get the statistics for the draws of the day
list_3 = raw_url_3.split("/")
modified_url_3 ='/'.join([str(item) for item in list_3]) 
response_3 = requests.get(modified_url_3)
# convert the data into a dictionary for editing
a = response_3.json()
list = []
# get only the statistics of the winning numbers
# insert them into a list
# return the winning numbers in ascending order
for i,j in itertools.product(a['numbers'],winningNumbers):
  if i['number'] == j:
   list.append(i['occurrences'])
winningNumbers.sort()   
# show the user the winning numbers and their statistics respectively
print("Result of the first draw for "+date+"\nWinning numbers are:")
print(winningNumbers)
print("Occurrences:")
print(list)



