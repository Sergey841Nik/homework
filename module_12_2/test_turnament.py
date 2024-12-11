import unittest
from collections import OrderedDict

from tpurnament import Runner, Tournament

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.all_results: dict = {}
    
    def setUp(self) -> None:
        self.runner_usein = Runner("Усэйн", 10)
        self.runner_andrey = Runner("Андрей", 9)
        self.runner_nik = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls) -> None:
        all_res_sort = {key: cls.all_results[key] for key in sorted(cls.all_results)}
        for runner in all_res_sort.values():
            print({key: runner[key].name for key in runner})

    def test_tunament_usein_nik(self) -> None:
        tr = Tournament(90, self.runner_usein, self.runner_nik)
        result: dict = tr.start()
        self.all_results[1] = result
        name_last: str = result[len(result)]
        self.assertTrue("Ник" == name_last)

    def test_tunament_andrey_nik(self) -> None:
        tr = Tournament(90, self.runner_andrey, self.runner_nik)
        result: dict = tr.start()
        self.all_results[2] = result
        name_last: str = result[len(result)]
        self.assertTrue(self.runner_nik == name_last)

    def test_tunament_usein_andrey_nik(self) -> None:
        tr = Tournament(90, self.runner_usein, self.runner_andrey, self.runner_nik)
        result: dict = tr.start()
        self.all_results[3] = result
        name_last: str = result[len(result)]
        self.assertTrue(self.runner_nik == name_last)


if __name__ == '__main__':
    unittest.main()