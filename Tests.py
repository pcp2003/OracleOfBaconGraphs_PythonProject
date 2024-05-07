from Graph import Graph, Vertex
import random as rnd
import string  # Importar para usar string.ascii_letters

from HollywoodOracle import HollywoodOracle

oracle = HollywoodOracle("DataSets/small_dataset_utf8.txt")

movies = oracle.all_movies()

for movie in movies:
    print(movie)
