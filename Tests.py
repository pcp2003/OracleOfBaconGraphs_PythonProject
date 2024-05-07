from Graph import Graph, Vertex
import random as rnd
import string  # Importar para usar string.ascii_letters

from HollywoodOracle import HollywoodOracle

oracle = HollywoodOracle("DataSets/testDataSet.txt")

movies = oracle.all_movies()

actors = oracle.all_actors()

ActorXFilms = oracle.movies_from("Steele, Rob (I)")

castOfX = oracle.cast_of("'Breaker' Morant (1980)")

oracle.set_center_of_universe("Senga, Ken")

for distance in oracle._distances:
    print(distance)




