from Graph import Graph, Vertex
import random as rnd
import string  # Importar para usar string.ascii_letters

from HollywoodOracle import HollywoodOracle

oracle = HollywoodOracle("DataSets/small_dataset_utf8.txt")

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

for distance in oracle._bfs_result:
    print(oracle._bfs_result[distance][0], ":", distance)

oracle.set_center_of_universe("Knez, Bruno")

print("\n")

for distance in oracle._bfs_result:
    print(oracle._bfs_result[distance][0], ":", distance)

print("\n")
print("Number of X: ", oracle.number_of_X("Sullivan, Fiona"))

pathToX = oracle.path_to_X("Grandison, Pippa")

print("\n")
print("Path to X: " )

for path in pathToX:
    print(path)








