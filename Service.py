import json
import requests
import random
# get db retrive data
#db den gelen verilerden random 1 tanesi
def get(child):
        listData = ["test"]
        list = requests.get('https://testproject-a5c8d.firebaseio.com/'+child.lower()+'.json')
        json_data = json.loads(list.content)
        for item in json_data:
            listData.append(json_data[item]['name'])
        return  listData[random.randint(0,len(listData)-1)].lower()