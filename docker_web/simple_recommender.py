import random
import json

api_data = [
          "list1",
          "list2",
          "list3"
]

movies2= json.load(open('main_api.json'))


movies3 = list(movies2)

def get_recommendations():
    random.shuffle(movies3)
    return movies3[:3]

#print(get_recommendations())