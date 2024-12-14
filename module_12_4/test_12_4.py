import logging
from unittest import TestCase, main

from run_tournament import Runner

logging.basicConfig(
        level=logging.INFO,
        filemode="w",
        filename="./module_12_4/ruuner_test.log",
        encoding="utf-8",
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


class RunnerTest(TestCase):
    is_frozen = False

    def test_walk(self):
        try:
            runner = Runner("Bolt", -5)
            for _ in range(10):
                runner.walk()
            logging.info("'test_walk' выполнен успешно")
            self.assertEqual(runner.distance, 50)
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            runner = Runner(123)
            for _ in range(10):
                runner.run()
            logging.info("'test_run' выполнен успешно")
            self.assertEqual(runner.distance, 100)
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        runner1 = Runner("Bolt")
        runner2 = Runner("Usein")
        for _ in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    
    main()
