import unittest

class upload_download_scenario(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setupClass - identify and launch the browser")

    def setUp(self):
        print("setup - Login into the application")

    def tearDown(self):
        print("teardown - Logout of the application")

    #     test methods below
    def test_scenario1_checkWelcomeTextAppearing(self):
        print("test method1 - Execute scenario 1")

    def test_scenario2_uploadFile(self):
        print("test method 2 - Execute scenario 2")

    def test_scenario3_downloadFile(self):
        print("test method 3 - Execute scenario 3")

    @classmethod
    def tearDownClass(cls):
        print("teardownClass - Closing the browser windows/session")

if __name__ == "__main__":
    unittest.main()

    '''
    setUp
    tearDown
    @classmethod
    setUpClass

    @classmethod
    tearDownClass

    Execution order
    setup
    test_scenarioname1
    teardown
    setup
    test_scenarioname2
    teardown
    setup
    test_scenarioname3
    teardown
    
    
    '''


