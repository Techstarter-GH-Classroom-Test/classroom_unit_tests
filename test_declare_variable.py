import unittest
import main

class TestNameVariable(unittest.TestCase):
    def test_name_variable(self):
        # Überprüfen, ob die Variable 'name' deklariert wurde
        self.assertTrue('name' in globals(), "Die Variable 'name' wurde nicht deklariert.")
        # Überprüfen, ob 'name' ein String ist
        self.assertIsInstance(main.name, str, "Die Variable 'name' muss ein String sein.")

if __name__ == '__main__':
    unittest.main()
