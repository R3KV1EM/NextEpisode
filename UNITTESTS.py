import unittest

import UNITTESTSMAIN


class TestMain(unittest.TestCase):
    def setUp(self):
        print("This is a test for Func")
    def test_do_stuff(self):
        testparam = 10
        result = UNITTESTSMAIN.do_stuff(testparam)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        testparam = "shgas"
        result = UNITTESTSMAIN.do_stuff(testparam)
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        testparam = None
        result = UNITTESTSMAIN.do_stuff(testparam)
        self.assertEqual(result, 'Please enter number')

    def test_do_stuff4(self):
        testparam = ""
        result = UNITTESTSMAIN.do_stuff(testparam)
        self.assertEqual(result, 'Please enter number')

    def test_do_stuff5(self):
        testparam = 0
        result = UNITTESTSMAIN.do_stuff(testparam)
        self.assertEqual(result, 'Please enter number')

    def test_do_stuff6(self):
        testparam = (1, 2, 3, 4)
        result = UNITTESTSMAIN.do_stuff(testparam)
        self.assertEqual(result, 'Please enter number')
    def tearDown(self):
        print("cleaning up")