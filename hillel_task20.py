import json
#import numpy as np

file_object = open('data', 'r')
result = json.loads(file_object.read())

runtime = 0
my_list = []
description = []
season = []
number = []
name = []
summary = []
link = []
for obj in result['_embedded']['episodes']:
    runtime += obj["runtime"]
    description.append('Episode description ')
    season.append(obj['season'])
    number.append(obj['number'])
    name.append(obj['name'])
    summary.append(obj['summary'])
    link.append(obj['url'])

print(f'Total runtime = {runtime} minutes')
general_list = list(zip(description,season,number, name, summary, link))
for description, season,number, name, summary, link in general_list:
    print (description, season,number, name, summary, link)