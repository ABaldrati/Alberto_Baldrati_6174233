from ChestClinic import *
from Fire import *


def calculate_KLdistance_from_a_network(type_of_network, file_path, n_occorrences):
    network = type_of_network(file_path)
    network.build_graph()
    network.graph_build_occorrences()
    network.graph_count_occorrences(n_occorrences)
    network.graph_build_probabilities()
    network.build_real_distribution()
    return network.calculate_Kullback_Leibler_distance()


def test_FireNetwork_changing_n_occorences():
    n_occorences = 100
    result = []
    occ = []

    while n_occorences <= 1000000:
        result.append(calculate_KLdistance_from_a_network(Fire, "fire.dat", n_occorences))
        occ.append(n_occorences)
        n_occorences *= 10
    print("I risultati dell'apprendimento della FireNetwork valutati mediante la divergenza di Kullback-Leibler sono:")
    for i in range(len(result)):
        print('L\'apprendimento con un dataset di dimensione {}  ha una divergenza pari a  {}'.format(occ[i],
                                                                                                      "{0:.5f}".format(
                                                                                                          result[i])))


def test_ChestClinicNetwork_changing_n_occorences():
    n_occorences = 100
    result = []
    occ = []

    while n_occorences <= 1000000:
        result.append(calculate_KLdistance_from_a_network(ChestClinic, "chestclinic.dat", n_occorences))
        occ.append(n_occorences)
        n_occorences *= 10
    print(
        "I risultati dell'apprendimento della ChestClinicNetwork valutati mediante la divergenza di Kullback-Leibler sono:")
    for i in range(len(result)):
        print('L\'apprendimento con un dataset di dimensione {}  ha una divergenza pari a  {}'.format(occ[i],
                                                                                                      "{0:.5f}".format(
                                                                                                          result[i])))


test_FireNetwork_changing_n_occorences()
test_ChestClinicNetwork_changing_n_occorences()
