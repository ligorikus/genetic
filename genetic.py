import random


def create_chromosome(graph, from_elem, to_elem):
    chromosome = []
    elem = from_elem
    while to_elem not in chromosome:
        chromosome.append(elem)
        elem = random.choice(list(graph[elem].keys()))
    return normalize(chromosome)


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
    found = False
    counter = 0
    first_end = -1
    second_start = 0
    while not found:
        counter += 1
        r = random.randint(0, len(chromosome1) - 1)
        if chromosome1[r] in chromosome2:
            for i in range(len(chromosome2)-1):
                if chromosome1[r] == chromosome2[i]:
                    first_end = r
                    second_start = i
                    found = True
        if counter > 5:
            return False
    return normalize(chromosome1[:first_end]+chromosome2[second_start:])


def mutation(graph, chromosome, start=1):
    r = random.randint(start, len(chromosome) - 1)
    new_sequence = create_chromosome(graph, chromosome[r], chromosome[-1])
    return normalize(chromosome[:r]+new_sequence)


def mutation2(graph, chromosome, start=0):
    r1 = random.randint(start, len(chromosome)-1)
    r2 = random.randint(start, len(chromosome)-1)
    if r1 > r2:
        first = r2
        second = r1
    elif r1 < r2:
        first = r1
        second = r2
    else:
        return chromosome
    if chromosome[first] == chromosome[second]:
        chromosome = chromosome[:first]+chromosome[second:]
        return chromosome
    new_sequence = create_chromosome(graph, chromosome[first], chromosome[second])
    return normalize(chromosome[:first] + new_sequence + chromosome[second:])


def normalize(chromosome):
    for i in range(len(chromosome)):
        if i == 0:
            continue
        if chromosome[i] == chromosome[i-1]:
            chromosome.pop(i)
    return chromosome


def evolution(graph, init_generation):
    generation = init_generation
    generation_index = 1
    while True:
        print("\n")
        print("Generation index:", generation_index)
        for chromosome in generation:
            print(weight_chromosome(graph, chromosome), chromosome)
        generation = next_generation(graph, generation, 5, len(generation))
        generation_index += 1
        input()


def next_generation(graph, generation, survival_size, offspring_size):
    survivors = list()
    weights = [weight_chromosome(graph, generation[i]) for i in range(len(generation))]

    if survival_size >= len(generation):
        survival_size = len(generation)-1

    if offspring_size < survival_size:
        offspring_size = survival_size

    for i in range(survival_size):
        max_elem = max(weights)
        min_index = weights.index(min(weights))
        survivors.append(generation[min_index])
        weights[min_index] = max_elem+1

    new_generation = list()

    if len(survivors) == 2:
        new_generation.append(survivors[0])
        new_generation.append(survivors[1])
        if offspring_size >= 3:
            new_chromosome = crossbreeding(graph, survivors[0], survivors[1])
            if new_chromosome is False:
                new_generation.append(mutation(graph, survivors[0]))
            else:
                new_generation.append(new_chromosome)
        elif offspring_size >= 4:
            new_chromosome = crossbreeding(graph, survivors[1], survivors[0])
            if new_chromosome is False:
                new_generation.append(mutation(graph, survivors[1]))
            else:
                new_generation.append(new_chromosome)
        for i in range(offspring_size-len(new_generation)):
            rand = random.random()
            if rand <= 0.25:
                new_generation.append(mutation(graph, survivors[0]))
            elif rand <= 0.5:
                new_generation.append(mutation(graph, survivors[1]))
            elif rand <= 0.75:
                chromosome = crossbreeding(graph, survivors[0], survivors[1])
                new_generation.append(mutation(graph, chromosome))
            else:
                chromosome = crossbreeding(graph, survivors[1], survivors[0])
                new_generation.append(mutation(graph, chromosome))
    elif len(survivors) == 1:
        new_generation.append(survivors[0])
        for i in range(offspring_size-1):
            new_generation.append(mutation(graph, survivors[0]))
    else:
        for i in range(survival_size):
            new_generation.append(survivors[i])

        for i in range(offspring_size-len(new_generation)):
            rand = random.random()
            rand_item = random.randint(0, survival_size-1)
            if rand <= 0.25:
                new_generation.append(mutation(graph, survivors[rand_item]))
            elif rand <= 0.66:
                if rand_item == survival_size-1:
                    next_item = 0
                else:
                    next_item = rand_item+1

                chromosome = crossbreeding(graph, survivors[rand_item], survivors[next_item])
                if chromosome is False:
                    chromosome = survivors[rand_item]
                new_generation.append(mutation(graph, chromosome))
            else:
                if rand_item == 0:
                    next_item = survival_size-1
                else:
                    next_item = rand_item-1

                chromosome = crossbreeding(graph, survivors[rand_item], survivors[next_item])
                if chromosome is False:
                    chromosome = survivors[rand_item]
                new_generation.append(mutation(graph, chromosome))

    return new_generation
