from BayesianNetwork import *
from Node import *


class Fire(BayesianNetwork):

    def build_graph(self):
        fire = Node("Fire", ["true", "false"])
        report = Node("Report", ["true", "false"])
        alarm = Node("Alarm", ["true", "false"])
        leaving = Node("Leaving", ["true", "false"])
        smoke = Node("Smoke", ["true", "false"])
        tampering = Node("Tampering", ["true", "false"])

        report.add_padre(leaving)
        leaving.add_padre(alarm)
        alarm.add_padre(tampering)
        alarm.add_padre(fire)
        smoke.add_padre(fire)

        self.graph.append(fire)
        self.graph.append(report)
        self.graph.append(leaving)
        self.graph.append(alarm)
        self.graph.append(smoke)
        self.graph.append(tampering)

    def build_real_distribution(self):
        self.distribution[(('Fire', 'true'),)] = 0.01
        self.distribution[(('Fire', 'false'),)] = 0.99

        self.distribution[(('Leaving', 'true'), ('Report', 'true'))] = 0.75
        self.distribution[(('Leaving', 'true'), ('Report', 'false'))] = 0.25
        self.distribution[(('Leaving', 'false'), ('Report', 'true'))] = 0.01
        self.distribution[(('Leaving', 'false'), ('Report', 'false'))] = 0.99

        self.distribution[(('Alarm', 'true'), ('Leaving', 'true'))] = 0.88
        self.distribution[(('Alarm', 'true'), ('Leaving', 'false'))] = 0.12
        self.distribution[(('Alarm', 'false'), ('Leaving', 'true'))] = 0.001
        self.distribution[(('Alarm', 'false'), ('Leaving', 'false'))] = 0.999

        self.distribution[(('Alarm', 'true'), ('Fire', 'true'), ('Tampering', 'true'))] = 0.5
        self.distribution[(('Alarm', 'false'), ('Fire', 'true'), ('Tampering', 'true'))] = 0.5
        self.distribution[(('Alarm', 'true'), ('Fire', 'false'), ('Tampering', 'true'))] = 0.85
        self.distribution[(('Alarm', 'false'), ('Fire', 'false'), ('Tampering', 'true'))] = 0.15
        self.distribution[(('Alarm', 'true'), ('Fire', 'true'), ('Tampering', 'false'))] = 0.99
        self.distribution[(('Alarm', 'false'), ('Fire', 'true'), ('Tampering', 'false'))] = 0.01
        self.distribution[(('Alarm', 'true'), ('Fire', 'false'), ('Tampering', 'false'))] = 0.0001
        self.distribution[(('Alarm', 'false'), ('Fire', 'false'), ('Tampering', 'false'))] = 0.9999

        self.distribution[(('Fire', 'true'), ('Smoke', 'true'))] = 0.9
        self.distribution[(('Fire', 'true'), ('Smoke', 'false'))] = 0.1
        self.distribution[(('Fire', 'false'), ('Smoke', 'true'))] = 0.01
        self.distribution[(('Fire', 'false'), ('Smoke', 'false'))] = 0.99

        self.distribution[(('Tampering', 'true'),)] = 0.02
        self.distribution[(('Tampering', 'false'),)] = 0.98
