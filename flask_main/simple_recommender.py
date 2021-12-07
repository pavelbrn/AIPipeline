import random
import json

movies = [
          "The Shawshank Redemption",
          "Star Wars: Episode IV - A New Hope",
          "Pulp Fiction",
          "The Dark Knight",
          "Forrest Gump",
          "Inception",
          "The Matrix",
          "Saving Private Ryan",
          "Casablanca",
          "The Lion King"
]

movies2= json.load(open('movies.json'))


movies3 = list(movies2)

def get_recommendations():
    random.shuffle(movies3)
    return movies3[:3]

#print(get_recommendations())