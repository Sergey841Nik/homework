import unittest

from tpurnament import Runner, Tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls) -> None:
        cls.all_results: dict = {}

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self) -> None:
        self.runner_usein = Runner("Усэйн", 10)
        self.runner_andrey = Runner("Андрей", 9)
        self.runner_nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls) -> None:
        # сортировка словаря
        all_res_sort: dict = {
            key: cls.all_results[key] for key in sorted(cls.all_results)
        }
        for runner in all_res_sort.values():
            print({key: runner[key].name for key in runner})

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tunament_usein_nik(self) -> None:
        tr = Tournament(90, self.runner_usein, self.runner_nik)
        result: dict = tr.start()
        self.all_results[1] = result
        name_last: str = result[len(result)]
        self.assertTrue("Ник" == name_last)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tunament_andrey_nik(self) -> None:
        tr = Tournament(90, self.runner_andrey, self.runner_nik)
        result: dict = tr.start()
        self.all_results[2] = result
        name_last: str = result[len(result)]
        self.assertTrue(self.runner_nik == name_last)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tunament_usein_andrey_nik(self) -> None:
        tr = Tournament(90, self.runner_usein, self.runner_andrey, self.runner_nik)
        result: dict = tr.start()
        self.all_results[3] = result
        name_last: str = result[len(result)]
        self.assertTrue(self.runner_nik == name_last)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_tunament_second(self) -> None:

        tr = Tournament(6, self.runner_usein, self.runner_andrey, self.runner_nik)
        result: dict = tr.start()
        self.all_results[4] = result
        name_second: str = result[2]
        self.assertTrue(self.runner_andrey == name_second)


if __name__ == "__main__":
    unittest.main()
