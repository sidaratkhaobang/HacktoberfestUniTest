import unittest


class AlmostIncreaseSequence(unittest.TestCase):
    
    def test_input_case_1_should_be_return_false(self):
        
        number = [1, 3, 2, 1]

        expected = False
        actual = almostIncreaseSequence(number)

        self.assertEqual(actual, expected)
        
def almostIncreaseSequence(number):
        for i, x in enumerate(number):
            s = number[:i]
            s.extend(number[i+1:])
            if s == sorted(set(s)):
                return True
        return False
    

unittest.main()

