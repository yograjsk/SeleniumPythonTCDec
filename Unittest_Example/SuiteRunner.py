import unittest
from Unittest_Example.TC1_SearchUserRoles import TC1_searchUser
from Unittest_Example.TC2_AddUsername import TC2_AddUser
from Unittest_Example.TC3_EditUser import TC3_EditUser
from Unittest_Example.TC4_DeleteUser import TC4_DeleteUser
from Unittest_Example.Utilities import Utilities

tc1 = unittest.TestLoader().loadTestsFromTestCase(TC1_searchUser)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TC2_AddUser)
tc3 = unittest.TestLoader().loadTestsFromTestCase(TC3_EditUser)
tc4 = unittest.TestLoader().loadTestsFromTestCase(TC4_DeleteUser)

smokeTestSuite = unittest.TestSuite([tc1,tc2])
regressionTestSuite = unittest.TestSuite([tc1,tc2,tc3])
integrationTestSuite = unittest.TestSuite([tc1,tc2,tc3,tc4])

u = Utilities()
config = u.readProperties("config.properties")
suiteName = config["suiteName"].upper()

if suiteName == "REGRESSION":
    print("running regression suite")
    unittest.TextTestRunner().run(regressionTestSuite)
elif suiteName == "SMOKE":
    print("running Smoke suite")
    unittest.TextTestRunner().run(smokeTestSuite)
elif suiteName == "INTEGRATION":
    print("running Integration suite")
    unittest.TextTestRunner().run(integrationTestSuite)
