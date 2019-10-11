
import unittest
from person import Person
from virus import Virus
from simulation import Simulation
from logger import Logger

class Test(unittest.TestCase):
    def test__init__(self):
        virus = Virus("smallpox", 0.06, 0.15)
        sim = Simulation(100, .9, virus, 1)
   
        assert sim.pop_size == 2500
        assert sim.vacc_percentage == .99
        assert sim.virus.name == "smallpox"
        assert sim.initial_infected == 1

    def test_create_population(self):
        virus = Virus("small pox", 0.06, 0.15)
        simulation = Simulation(2500, 0.99, virus, 1)
        assert simulation.population == 100
        assert simulation.virus.name == 'small pox'
        assert simulation.total_infected == 1
        assert simulation.current_infected == 1
        assert simulation.total_dead == 0
        assert simulation.file_name == 'log.txt'
        assert len(simulation.newly_infected) is 0

    def test_simulation_should_continue(self):
        virus = Virus("small pox", 0.06, 0.15)
        simulation = Simulation(2500, 0.90, virus, 1)
        person1 = Person(1, True)
        person2 = Person(2, False)
        assert simulation.simulation_should_continue() == True

        person1.is_alive != True
        person2.is_alive != True
        assert simulation.simulation_should_continue() == False

    def test_interaction(self):
        virus = Virus("small pox", 0.06, 0.15)
        simulation = Simulation(2500, 0.90, virus, 1)

        person1 = Person(1, None)
        person2 = Person(2, virus)

        simulation.interaction(person1, person2)
        assert person1.infection == virus
        assert person2.infection == None

    def test_infect_newly_infected(self):
        virus = Virus("small pox", 0.06, 0.15)
        simulation = Simulation(2500, 0.90, virus, 1)

        assert simulation.population[1].infection == virus
        assert simulation.population[0.9].infection == virus
