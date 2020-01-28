import unittest

class UnitTestFramework(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("SetupClass Method")

    def setUp(self):
        print("Setup method")

    def tearDown(self):
        print("Teardown method")

    def test_Method1(self):
        print("Test Method 1")
        self.assertTrue(1<0,"condition is failed")


    def test_Method2(self):
        print("Test Method 2")
        a=1
        b=2
        self.assertEquals(a,b,"a and b are not equal")

    def test_Method3(self):
        print("Test Method 3")

    def method1(self):
        print("Method1")

    @classmethod
    def tearDownClass(cls):
        print("TeardownClass method")

