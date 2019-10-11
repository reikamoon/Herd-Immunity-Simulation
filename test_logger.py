import unittest
from virus import *
from person import *
from logger import *


class Test(unittest.TestCase):
    def test__init__(self):
        logger = Logger('log.txt')
        assert logger.file_name == 'log.txt'

    def test_write_metadata(self):
        logger = Logger('log.txt')
        open('log.txt', 'w').close()
        assert ('log.txt') == 0
        logger.write_metadata(10, 1, "virus_name", 0.1, 0.1)
        assert ('log.txt') != 0

    def test_log_interaction(self):
        logger = Logger('log.txt')
        virus = Virus("smallpox", 0.1, 0.1)
        person = Person(1, False, virus)
        random_person = Person(2, False)
        logger.log_interaction(person, random_person, random_person_sick=False, random_person_vacc=False, did_infect=True)
        assert ('log.txt')

    def test_log_infection_survival(self):
        logger = Logger('log.txt')
        virus = Virus("smallpoxt", 0.1, 0.1)
        person = Person(1, False, virus)
        logger.log_infection_survival(person, True)
        assert ('log.txt')
