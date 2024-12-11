import unittest
import moduel_12_2_test
import moduel_12_1_test

suite = unittest.TestSuite()
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(moduel_12_1_test.RunTest))
suite.addTest(unittest.TestLoader().loadTestsFromTestCase(moduel_12_2_test.TournamentTest))

testRunner = unittest.TextTestRunner(verbosity=2)
testRunner.run(suite)