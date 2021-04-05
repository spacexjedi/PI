import unittest
#from main import*


class healthtest(unittest.TestCase):

    def loosehealth(self):
        health = 1
        self.assertEqual(1, health)

    def anomalia(self):
        health = 0
        self.assertEqual(1, health)
    




if __name__ == '__main__':
    unittest.main()