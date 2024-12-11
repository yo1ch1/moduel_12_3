import moduel_12_1
import unittest



class RunTest(unittest.TestCase):
    is_frozen = True

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        runner = moduel_12_1.Runner('Vitek')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_run(self):
        runner = moduel_12_1.Runner('Vitek')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_chalenge(self):
        runner1 = moduel_12_1.Runner('Paul')
        runner2 = moduel_12_1.Runner('Max')
        for i in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    unittest.main()


