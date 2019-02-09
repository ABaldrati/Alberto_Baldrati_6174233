import math
from abc import ABC, abstractmethod
from itertools import product


class BayesianNetwork(ABC):
    def __init__(self, data_path):
        self.data_path = data_path
        self.graph = []
        self.distribution = {}

    @abstractmethod
    def build_graph(self):
        pass

    @abstractmethod
    def build_real_distribution(self):
        pass

    def graph_build_occorrences(self):
        for node in self.graph:
            node.build_occorrences_dictionary()

    def graph_count_occorrences(self, n_occorrenze):
        file = open(self.data_path)
        lines = list(file)
        file.close()
        lines = [x.strip("\n") for x in lines]
        nodi_grafo = lines[0].split(",")

        for i in range(1, n_occorrenze):
            update_values = self.read_update_lines(lines[i])
            dict_update = dict(zip(nodi_grafo, update_values))
            for nodo in self.graph:
                nodo.add_occorences_to_occ_dictionary(dict_update)

    def graph_build_probabilities(self):
        for node in self.graph:
            node.build_probability_dictionary()

    def calculate_Kullback_Leibler_distance(self):
        KL_Distance = 0
        for node in self.graph:
            iterator = product(*node.padri, node)
            lista_nomi_padri = [p.name for p in node.padri]
            lista_nomi_padri.append(node.name)

            for values in iterator:
                lista_valori = list(values)
                dict_key = dict(zip(lista_nomi_padri, lista_valori))
                key = tuple(sorted(dict_key.items()))
                if self.distribution[key] != 0:
                    KL_Distance += self.distribution[key] * math.log2((self.distribution[key] / node.prob[key]))

        return KL_Distance

    @staticmethod
    def read_update_lines(line):
        update_values_beta = line.strip("\"")
        update_values = update_values_beta.split("\",\"")
        return update_values
