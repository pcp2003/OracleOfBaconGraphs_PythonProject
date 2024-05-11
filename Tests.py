from HollywoodOracle import HollywoodOracle


oracle = HollywoodOracle("DataSets/small_dataset_utf8.txt")

movies = oracle.all_movies()

print("Movies: ")

for movie in movies:
    print(movie)

# actors = oracle.all_actors()
# print("\n")
# print("Actors: ")
#
# for actor in actors:
#     print(actor)

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

# print("\n")
#
# for distance in oracle.bfs_result:
#     print(oracle.bfs_result[distance][0], ":", distance)

oracle.set_center_of_universe("Knez, Bruno")

print("\n")

for distance in oracle.bfs_result:
    print(oracle.bfs_result[distance][0], ":", distance)

print("\n")
print("Number of X: ", oracle.number_of_x("Sullivan, Fiona"))

pathToX = oracle.path_to_x("Akan, Tarik")

print("\n")
print("Path to Knez, Bruno: " )

for path in pathToX:
    print(path)

print("\n")
print("Max number of X: ", oracle.max_number_of_x())

print("\n")
print("Number of numbers X: ", oracle.count_number_of_x(7))

print("\n")
print("Average number of X: ", oracle.avarage_number_of_x())







