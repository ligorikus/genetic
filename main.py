import graph as graph_class
import genetic
import random
import time

graph = graph_class.Graph(100).create(1, 25, seed=12)
n = 0
for i in graph:
    print(n, ":", i)
    n += 1

from_elem = 9
to_elem = 7

# random.seed(time.localtime())

chromosomes = list()
i = 0
while i < 5:
    new_chromosome = genetic.create_chromosome(graph, from_elem, to_elem)
    is_new = True
    for chromosome in chromosomes:
        is_eq = True
        for j in range(len(chromosome)):
            if new_chromosome[j] != chromosome[j]:
                is_eq = False
                break
        if is_eq:
            is_new = False
    if is_new:
        chromosomes.append(new_chromosome)
        i += 1

genetic.evolution(graph, chromosomes)