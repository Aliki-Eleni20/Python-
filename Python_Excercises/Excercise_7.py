import requests
import json
import datetime

raw_url_1= "https://api.opap.gr/draws/v3.0/{gameId}/draw-date/{fromDate}/{toDate}/draw-id"
raw_url_2 = "https://api.opap.gr/draws/v3.0/{gameId}/{drawId}"
# set the date for each day
date = datetime.datetime.today().strftime('%Y-%m-%d')
# get all the draw ids for each day
list_1= raw_url_1.split("/")
list_1[5] = 1100
list_1[7] = date
list_1[8] = date
modified_url_1 ='/'.join([str(item) for item in list_1 ]) 
response_1 = requests.get(modified_url_1)
# convert the data into a dictionary for editing
draw_ids = response_1.json()
list=[]
# get all the winning numbers from all the draw ids
for data in draw_ids:
  draw_id = data
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
  #insert winning numbers into a list
  list.append(winningNumbers)
# find the most common number
def highest_freq(lst):
   SimpleList = [el for sublist in lst for el in sublist]
   return max( SimpleList, key = SimpleList.count)
# show the user the element with highest frequency
print("Element with highest frequency:",highest_freq(list))