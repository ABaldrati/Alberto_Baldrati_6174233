from itertools import product


class Node:
    def __init__(self, name, domain_values):
        self.name = name
        self.range_of_values = domain_values
        self.padri = []
        self.occ = {}
        self.prob = {}

    def __iter__(self):
        return iter(self.range_of_values)

    def add_padre(self, nodo):
        self.padri.append(nodo)

    def build_occorrences_dictionary(self):
        iterator = product(*self.padri, self)
        lista_nomi_padri = [p.name for p in self.padri]
        lista_nomi_padri.append(self.name)
        keys = []

        for values in iterator:
            lista_valori = list(values)
            key_dict = dict(zip(lista_nomi_padri, lista_valori))
            keys += [tuple(sorted(key_dict.items()))]
        self.occ = dict.fromkeys(keys, 1)

    def add_occorences_to_occ_dictionary(self, update_values):
        nomi_padri = [p.name for p in self.padri]
        dict_key = {}

        for itemname, itemvalue in update_values.items():
            if itemname == self.name or itemname in nomi_padri:
                dict_key[itemname] = itemvalue
        key = tuple(sorted(dict_key.items()))
        self.occ[key] = self.occ[key] + 1

    def build_probability_dictionary(self):
        iterator_padri = product(*self.padri)
        for values in iterator_padri:
            lista_valori = list(values)
            lista_nomi_padri = [p.name for p in self.padri]
            lista_nomi_padri.append(self.name)
            counter = 0

            for self_value in self.range_of_values:
                lista_valori.append(self_value)
                dict_key = dict(zip(lista_nomi_padri, lista_valori))
                key = tuple(sorted(dict_key.items()))
                counter += self.occ[key]
                del lista_valori[-1]

            for self_value in self.range_of_values:
                lista_valori.append(self_value)
                dict_key = dict(zip(lista_nomi_padri, lista_valori))
                key = tuple(sorted(dict_key.items()))
                self.prob[key] = self.occ[key] / counter
                del lista_valori[-1]
