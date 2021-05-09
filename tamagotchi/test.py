import unittest
#from main import*


class healthtest(unittest.TestCase):

    def loosehealth(self):
        health = 1
        self.assertEqual(1, health)

    def anomalia(self):
        health = 0
        self.assertEqual(1, health)
    

class hungertest(unittest.TestCase):

    def loosehunger(self):
        hunger = 1
        self.assertEqual(1, hunger)

    def anomalia(self):
        hunger = 0
        self.assertEqual(1, hunger)

class happytest(unittest.TestCase):

    def loosehappy(self):
        happy = 1
        self.assertEqual(1, happy)

    def anomalia(self):
        happy = 0
        self.assertEqual(1, happy)

if __name__ == '__main__':
    unittest.main()