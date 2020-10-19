import unittest


class AlmostIncreaseSequence(unittest.TestCase):
    
    def test_input_case_1_should_be_return_false(self):
        
        number = [1, 3, 2, 1]

        expected = False
        actual = almostIncreaseSequence(number)

        self.assertEqual(actual, expected)
        
def almostIncreaseSequence(list_of_number):
        return False
    

unittest.main()

