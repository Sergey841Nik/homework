from unittest import TestCase, main, skipIf
from module_12 import Runner


class RunnerTest(TestCase):
    is_frozen = False

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = Runner("Bolt")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = Runner("Bolt")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        runner1 = Runner("Bolt")
        runner2 = Runner("Usein")
        for _ in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    main()
