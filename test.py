import unittest
import main as app
class TestMyRowsApp(unittest.TestCase):
    def setUp(self):
        self.app = app

    def test_transform(self):
        self.assertEqual(app.arifmetic_summ(2), 7)
        self.assertEqual(app.arifmetic_summ(6), 57)
        self.assertRaises(TypeError, self.app.arifmetic_summ, "qwertyuiop")


    def tearDown(self):
        pass
if __name__ == '__main__':
    unittest.main()