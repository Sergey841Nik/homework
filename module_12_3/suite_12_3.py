import unittest

from test_module_12_1 import RunnerTest
from test_turnament import TournamentTest

module_12_suite_test = unittest.TestSuite()

# module_12_suite_test.addTest(unittest.makeSuite(RunnerTest))
# module_12_suite_test.addTest(unittest.makeSuite(TournamentTest))

# проверил вариант с addTests
# test_suite_runner = unittest.TestLoader().loadTestsFromTestCase(RunnerTest)
# test_suite_tournament = unittest.TestLoader().loadTestsFromTestCase(TournamentTest)
# all_tests: tuple[unittest.TestSuite] = (test_suite_runner, test_suite_tournament)
# module_12_suite_test.addTests(all_tests)

module_12_suite_test.addTest(unittest.TestLoader().loadTestsFromTestCase(RunnerTest))
module_12_suite_test.addTest(unittest.TestLoader().loadTestsFromTestCase(TournamentTest))




run_test = unittest.TextTestRunner(verbosity=2)
run_test.run(module_12_suite_test)
