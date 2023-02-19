import unittest
import main

class TestRandomGen(unittest.TestCase):

    def setUp(self):
        config_path = 'config.json'
        seed = 10
        self.num_gen = main.RandomGen(seed, config_path)
        
    def test_next_num(self):
        """
        Tests that using the default configuration and seed 10, the first
        number generated is 1
        """
        num = self.num_gen.next_num()
        self.assertEqual(num, 1, "Wrong number generated.")

    def test_invalid_probabilities(self):
        """
        Tests attempting to use weights that do not sum to 1
        """
        probs = [0.5, 0.3, 0.2, 0.1, 0.1]
        with self.assertRaises(Exception) as context:
            self.num_gen.probs = probs
        self.assertTrue("Probabilities \
            must sum up to 1." in str(context.exception))
        
    def test_unequal_list_len(self):
        """
        Tests using numbers and their probabilities where the lengths of the
        two lists do not match
        """
        probs = [0.5, 0.3, 0.2]
        nums = [1,2,3,4]
        self.num_gen.probs = probs
        self.num_gen.nums = nums
        with self.assertRaises(Exception) as context:
            self.num_gen.next_num()
        
        self.assertTrue("Specified numbers and \
            their associated probabilities lists must have equal length."
            in str(context.exception))
        

if __name__ == '__main__':
    unittest.main()