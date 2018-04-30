import json
import requests
import random
# get db retrive data
#db den gelen verilerden random 1 tanesi
def get(child):
        listData = ["test"]
        try:
            list = requests.get('https://testproject-a5c8d.firebaseio.com/'+child.lower()+'.json')
            json_data = json.loads(list.content)
            for item in json_data:
                listData.append(json_data[item]['name'])  
            # verilen gelirse test datasını silmek için
            del listData[0]    
        except requests.exceptions.RequestException:
            print("İnternet bağlantınızda sorun bulunmakta test datalar ile oynayacaksınız \n")
        return  listData[random.randint(0,len(listData)-1)].lower()