import graph as graph_class
import genetic
import random
import time

graph = graph_class.Graph(10).create(1, 25, 12)
n = 0
for i in graph:
    print(n, ":", i)
    n += 1

from_elem = 6
to_elem = 9

#random.seed(time.localtime())

chromosomes = list()
for i in range(6):
    chromosomes.append(genetic.create_chromosome(graph, from_elem, to_elem))
    print(chromosomes[i])
    print(genetic.weight_chromosome(graph, chromosomes[i]))
