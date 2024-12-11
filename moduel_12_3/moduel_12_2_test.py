import moduel_12_2
import unittest



class TournamentTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = moduel_12_2.Runner("Usain", 10)
        self.runner2 = moduel_12_2.Runner("Andrew", 9)
        self.runner3 = moduel_12_2.Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_usain_nick(self):
        tournament = moduel_12_2.Tournament(distance=90)
        tournament.add_participant(self.runner1)
        tournament.add_participant(self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertEqual(results[min(results.keys())], self.runner1)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_andrew_nick(self):
        tournament = moduel_12_2.Tournament(distance=90)
        tournament.add_participant(self.runner2)
        tournament.add_participant(self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertEqual(results[min(results.keys())], self.runner2)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_all(self):
        tournament = moduel_12_2.Tournament(distance=90)
        tournament.add_participant(self.runner1)
        tournament.add_participant(self.runner2)
        tournament.add_participant(self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertEqual(results[min(results.keys())], self.runner1)

if __name__ == '__main__':
    unittest.main()
