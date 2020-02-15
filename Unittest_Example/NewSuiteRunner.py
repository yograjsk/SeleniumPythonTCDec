import unittest
from Unittest_Example.NewTC1_SearchUser import NewTC1_SearchUser
from Unittest_Example.NewTC2_AddUser import NewTC2_AddUser
from Unittest_Example.NewTC3_EditUser import NewTC3_EditUser
from Unittest_Example.NewTC4_DeleteUser import NewTC4_DeleteUser
from Unittest_Example.Utilities import Utilities

NewTC1 = unittest.TestLoader().loadTestsFromTestCase(NewTC1_SearchUser)
NewTC2 = unittest.TestLoader().loadTestsFromTestCase(NewTC2_AddUser)
NewTC3 = unittest.TestLoader().loadTestsFromTestCase(NewTC3_EditUser)
NewTC4 = unittest.TestLoader().loadTestsFromTestCase(NewTC4_DeleteUser)

smokeTestSuite = unittest.TestSuite([NewTC1, NewTC2, NewTC3, NewTC4])
RegressionTestSuite = unittest.TestSuite([NewTC1, NewTC2, NewTC3])
IntegrationTestSuite = unittest.TestSuite([NewTC2, NewTC2])

u = Utilities()
config = u.readProperties("config.properties")
suiteName = config["suiteName"]

if suiteName == "SMOKE":
    unittest.TextTestRunner().run(smokeTestSuite)
elif suiteName == "REGRESSION":
    unittest.TextTestRunner().run(RegressionTestSuite)
elif suiteName == "INTEGRATION":
    unittest.TextTestRunner().run(IntegrationTestSuite)
