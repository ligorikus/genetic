import random


def create_chromosome(graph, from_elem, to_elem):
    chromosome = []
    elem = from_elem
    while to_elem not in chromosome:
        chromosome.append(elem)
        elem = random.choice(list(graph[elem].keys()))
    return chromosome


def weight_chromosome(graph, chromosome):
    result = 0
    previous = chromosome[0]
    for elem in chromosome:
        if elem == previous:
            continue
        result += graph[previous][elem]
        previous = elem
    return result


def crossbreeding(graph, chromosome1, chromosome2):
    pass


def mutation(graph, chromosome):
    pass
