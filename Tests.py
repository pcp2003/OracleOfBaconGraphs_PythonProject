from Graph import Graph, Vertex
import random as rnd
import string  # Importar para usar string.ascii_letters

from HollywoodOracle import HollywoodOracle

oracle = HollywoodOracle("DataSets/testDataSet.txt")

movies = oracle.all_movies()

print("Movies: ")

for movie in movies:
    print(movie)

actors = oracle.all_actors()
print("\n")
print("Actors: ")

for actor in actors:
    print(actor)

ActorXFilms = oracle.movies_from("Steele, Rob (I)")
print("\n")
print("ActorXFilms :")

for actor in ActorXFilms:
    print(actor)

castOfX = oracle.cast_of("'Breaker' Morant (1980)")
print("\n")
print("Cast :")

for cast in castOfX:
    print(cast)

print("\n")

for distance in oracle._distances:
    print(oracle._distances[distance], ":", distance)

oracle.set_center_of_universe("Knez, Bruno")

print("\n")

for distance in oracle._distances:
    print(oracle._distances[distance], ":", distance)





