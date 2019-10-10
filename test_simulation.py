import unittest
from person import Person
from virus import Virus
from simulation import Simulation
from logger import Logger
import random, sys

class Test(unittest.TestCase):
    def test_create_population(self):
        virus = Virus("small pox", 0.06, 0.15)
        virus.set_virus_small_pox()
        simulation = Simulation(100, 0.90, virus, 1)

    def test_simulation_should_continue(self):
        virus = Virus("small pox", 0.06, 0.15)
        simulation = Simulation(100, 0.90, virus, 1)

    def test_interaction(self):
        virus = Virus("small pox", 0.06, 0.15)
        simulation = Simulation(100, 0.90, virus, 1)
    
    def test_time_step():
        virus = Virus("small pox", 0.06, 0.15)
        simulation = Simulation(100, 0.90, virus, 1)

        person1
        person2

    def test_infect_newly_infected(self):
        virus = Virus("small pox", 0.06, 0.15)
        simulation = Simulation(100, 0.90, virus, 1)

        person1
        person2
