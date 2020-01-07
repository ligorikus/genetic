import graph as graph_class
import genetic
import random
import time

graph = graph_class.Graph(1000).create(1, 25, seed=12)
n = 0
for i in graph:
    print(n, ":", i)
    n += 1

from_elem = 321
to_elem = 882

# random.seed(time.localtime())

chromosomes = list()
i = 0
while i < 12:
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