import random


class Graph:
    def __init__(self, count_of_vertices):
        self.graph = []
        self.count_of_vertices = count_of_vertices
        for i in range(count_of_vertices):
            self.graph.append(dict())

    def create(self, min_weight, max_weight, seed=0):
        if seed != 0:
            random.seed(seed)

        for i in range(self.count_of_vertices):
            relations = list()
            for j in range(self.count_of_vertices):
                if i == j:
                    continue
                if random.random() > 0.5:
                    relations.append(j)
            for j in relations:
                self.graph[i][j] = random.randint(min_weight, max_weight)
                self.graph[j][i] = self.graph[i][j]

        return self.graph


