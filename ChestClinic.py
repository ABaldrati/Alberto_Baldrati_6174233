from BayesianNetwork import *
from Node import *


class ChestClinic(BayesianNetwork):
    def build_graph(self):
        positive_xray = Node("Positive_xray", ["yes", "no"])
        bronchitis = Node("Bronchitis", ["yes", "no"])
        dyspnoea = Node("Dyspnoea", ["yes", "no"])
        visit_to_asia = Node("Visit_to_asia", ["yes", "no"])
        smoker = Node("Smoker", ["yes", "no"])
        lung_cancer = Node("Lung_cancer", ["yes", "no"])
        tuberculosis = Node("Tuberculosis", ["yes", "no"])
        tuberculosis_or_cancer = Node("Tubercolosis_or_cancer", ["yes", "no"])

        tuberculosis.add_padre(visit_to_asia)
        lung_cancer.add_padre(smoker)
        bronchitis.add_padre(smoker)
        tuberculosis_or_cancer.add_padre(tuberculosis)
        tuberculosis_or_cancer.add_padre(lung_cancer)
        positive_xray.add_padre(tuberculosis_or_cancer)
        dyspnoea.add_padre(bronchitis)
        dyspnoea.add_padre(tuberculosis_or_cancer)

        self.graph.append(positive_xray)
        self.graph.append(bronchitis)
        self.graph.append(dyspnoea)
        self.graph.append(visit_to_asia)
        self.graph.append(smoker)
        self.graph.append(lung_cancer)
        self.graph.append(tuberculosis)
        self.graph.append(tuberculosis_or_cancer)

    def build_real_distribution(self):
        self.distribution[(('Positive_xray', 'yes'), ('Tubercolosis_or_cancer', 'yes'))] = 0.98
        self.distribution[(('Positive_xray', 'no'), ('Tubercolosis_or_cancer', 'yes'))] = 0.02
        self.distribution[(('Positive_xray', 'yes'), ('Tubercolosis_or_cancer', 'no'))] = 0.05
        self.distribution[(('Positive_xray', 'no'), ('Tubercolosis_or_cancer', 'no'))] = 0.95

        self.distribution[(('Bronchitis', 'yes'), ('Smoker', 'yes'))] = 0.6
        self.distribution[(('Bronchitis', 'no'), ('Smoker', 'yes'))] = 0.4
        self.distribution[(('Bronchitis', 'yes'), ('Smoker', 'no'))] = 0.3
        self.distribution[(('Bronchitis', 'no'), ('Smoker', 'no'))] = 0.7

        self.distribution[(('Bronchitis', 'yes'), ('Dyspnoea', 'yes'), ('Tubercolosis_or_cancer', 'yes'))] = 0.9
        self.distribution[(('Bronchitis', 'yes'), ('Dyspnoea', 'no'), ('Tubercolosis_or_cancer', 'yes'))] = 0.1
        self.distribution[(('Bronchitis', 'yes'), ('Dyspnoea', 'yes'), ('Tubercolosis_or_cancer', 'no'))] = 0.8
        self.distribution[(('Bronchitis', 'yes'), ('Dyspnoea', 'no'), ('Tubercolosis_or_cancer', 'no'))] = 0.2
        self.distribution[(('Bronchitis', 'no'), ('Dyspnoea', 'yes'), ('Tubercolosis_or_cancer', 'yes'))] = 0.7
        self.distribution[(('Bronchitis', 'no'), ('Dyspnoea', 'no'), ('Tubercolosis_or_cancer', 'yes'))] = 0.3
        self.distribution[(('Bronchitis', 'no'), ('Dyspnoea', 'yes'), ('Tubercolosis_or_cancer', 'no'))] = 0.1
        self.distribution[(('Bronchitis', 'no'), ('Dyspnoea', 'no'), ('Tubercolosis_or_cancer', 'no'))] = 0.9

        self.distribution[(('Visit_to_asia', 'yes'),)] = 0.01
        self.distribution[(('Visit_to_asia', 'no'),)] = 0.99

        self.distribution[(('Smoker', 'yes'),)] = 0.5
        self.distribution[(('Smoker', 'no'),)] = 0.5

        self.distribution[(('Lung_cancer', 'yes'), ('Smoker', 'yes'))] = 0.1
        self.distribution[(('Lung_cancer', 'no'), ('Smoker', 'yes'))] = 0.9
        self.distribution[(('Lung_cancer', 'yes'), ('Smoker', 'no'))] = 0.01
        self.distribution[(('Lung_cancer', 'no'), ('Smoker', 'no'))] = 0.99

        self.distribution[(('Tuberculosis', 'yes'), ('Visit_to_asia', 'yes'))] = 0.05
        self.distribution[(('Tuberculosis', 'no'), ('Visit_to_asia', 'yes'))] = 0.95
        self.distribution[(('Tuberculosis', 'yes'), ('Visit_to_asia', 'no'))] = 0.01
        self.distribution[(('Tuberculosis', 'no'), ('Visit_to_asia', 'no'))] = 0.99

        self.distribution[(('Lung_cancer', 'yes'), ('Tubercolosis_or_cancer', 'yes'), ('Tuberculosis', 'yes'))] = 1
        self.distribution[(('Lung_cancer', 'yes'), ('Tubercolosis_or_cancer', 'no'), ('Tuberculosis', 'yes'))] = 0
        self.distribution[(('Lung_cancer', 'no'), ('Tubercolosis_or_cancer', 'yes'), ('Tuberculosis', 'yes'))] = 1
        self.distribution[(('Lung_cancer', 'no'), ('Tubercolosis_or_cancer', 'no'), ('Tuberculosis', 'yes'))] = 0.
        self.distribution[(('Lung_cancer', 'yes'), ('Tubercolosis_or_cancer', 'yes'), ('Tuberculosis', 'no'))] = 1
        self.distribution[(('Lung_cancer', 'yes'), ('Tubercolosis_or_cancer', 'no'), ('Tuberculosis', 'no'))] = 0.
        self.distribution[(('Lung_cancer', 'no'), ('Tubercolosis_or_cancer', 'yes'), ('Tuberculosis', 'no'))] = 0
        self.distribution[(('Lung_cancer', 'no'), ('Tubercolosis_or_cancer', 'no'), ('Tuberculosis', 'no'))] = 1
