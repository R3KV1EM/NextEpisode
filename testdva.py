import unittest
import Maindva

class TestGame(unittest.TestCase):
    def testinput(self):
        answer = 5
        guess = 5
        result = qeq.run_guess(answer, guess)
        self.assertTrue(result)

    def testinputincorrect(self):

        result = qeq.run_guess(5, 0)
        self.assertFalse(result)

    def testinputincorrect1(self):

        result = qeq.run_guess(5, 11)
        self.assertFalse(result)