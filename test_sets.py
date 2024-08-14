import unittest
import my_sets 

class TestVariableAssignments(unittest.TestCase):
    
    def test_exercise_1(self):
        # Check if 'x' is defined
        self.assertTrue(hasattr(my_sets, 'length'), "Übung 1 ist fehlgeschlagen: 'Länge' ist nicht definiert.")
        # Check if 'x' has the correct value
        self.assertEqual(my_sets.length, 7, "Übung 1 ist fehlgeschlagen: Der Wert von 'Länge' sollte 7 sein.")
    
    def test_exercise_2(self):
         # Check if 'it_companies' has OpenAI element is defined
         test_set = set(['OpenAI'])
         test_val = my_sets.it_companies.intersection(test_set)
         self.assertEqual(test_set,test_val, "Übung 1 ist fehlgeschlagen: 'OpenAI' wurde nicht gefunden.")
    
    #def test_exercise_3(self):
         # Check if 'z' is defined
    #     self.assertTrue(hasattr(exercises, 'z'), "Exercise 3 failed: 'z' is not defined.")
         # Check if 'z' has the correct value
     #    self.assertEqual(exercises.z, 15, "Exercise 3 failed: The value of 'z' should be 15.")
    
    # def test_exercise_4(self):
    #     # Check if 'a' is defined
    #     self.assertTrue(hasattr(exercises, 'a'), "Exercise 4 failed: 'a' is not defined.")
    #     # Check if 'a' has the correct value
    #     self.assertEqual(exercises.a, 20, "Exercise 4 failed: The value of 'a' should be 20.")
    
    # def test_exercise_5(self):
    #     # Check if 'b' is defined
    #     self.assertTrue(hasattr(exercises, 'b'), "Exercise 5 failed: 'b' is not defined.")
    #     # Check if 'b' has the correct value
    #     self.assertEqual(exercises.b, 25, "Exercise 5 failed: The value of 'b' should be 25.")

if __name__ == '__main__':
    unittest.main()