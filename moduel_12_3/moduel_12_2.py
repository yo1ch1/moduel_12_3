import unittest

class Runner:
    def __init__(self, name, speed=5):
        self.is_frozen = True
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def add_participant(self, runner):
            self.participants.append(runner)

    def start(self):
        finishers = {}
        place = 1
        finished_participants = []  # Новый список для финишеров
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    finished_participants.append(participant)  # Добавляем участника в новый список
                    place += 1
            for finished in finished_participants:
                self.participants.remove(finished)# Удаляем финишировавших участников после завершения цикла
            finished_participants.clear()  # Очищаем список финишеров для следующей итерации

        return finishers

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Usain", 10)
        self.runner2 = Runner("Andrew", 9)
        self.runner3 = Runner("Nick", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key}: {value}")

    def test_usain_nick(self):
        tournament = Tournament(distance=90)
        tournament.add_participant(self.runner1)
        tournament.add_participant(self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertEqual(results[min(results.keys())], self.runner1)

    def test_andrew_nick(self):
        tournament = Tournament(distance=90)
        tournament.add_participant(self.runner2)
        tournament.add_participant(self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertEqual(results[min(results.keys())], self.runner2)

    def test_all(self):
        tournament = Tournament(distance=90)
        tournament.add_participant(self.runner1)
        tournament.add_participant(self.runner2)
        tournament.add_participant(self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertEqual(results[min(results.keys())], self.runner1)

if __name__ == '__main__':
    unittest.main()