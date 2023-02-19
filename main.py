import random
import json
from collections import defaultdict
import matplotlib.pyplot as plt

class RandomGen():

    def __init__(self, seed=None, file_path=None) -> None:
        """
        Initializes numbers range with associated probabilities
        Option to load these from config file if path specified
        Otherwise default values specified by the hw handout are used
        """
        self._nums = [-1, 0, 1, 2, 3]
        self._probs = [0.01, 0.3, 0.58, 0.1, 0.01]
        self.seed(seed)
        if file_path:
            self.load_config_from_file(file_path)

    @property
    def nums(self) -> list:
        return self._nums

    @nums.setter
    def nums(self, numbers: list) -> None:
        self._nums = numbers

    @property
    def probs(self) -> list:
        return self._probs    

    @probs.setter
    def probs (self, probabilities: list[float]) -> None:
        assert round(sum(probabilities), 5) == 1, "Probabilities \
            must sum up to 1."
        self._probs = probabilities

    def seed(self, s: int) -> None:
        """
        Initialize random seed for number generator from provided integer seed
        """
        self._seed = s
        random.seed(s)

    def load_config_from_file(self, file_path: str) -> None:
        """
        Loads numbers and their probabilities from specified config file
        """
        with open(file_path, 'r') as f:
            data = json.load(f)        
        self._nums = data['numbers']
        self._probs = data['probabilities']
        assert len(self._nums) == len(self._probs), "Specified numbers and \
            their associated probabilities lists must have equal length."
        assert round(sum(self._probs), 5) == 1, "Probabilities \
            must sum up to 1."

    def next_num(self) -> int:
        """
        Pseudo-randomly generates number from a weighted range of numbers.
        The range is specified in _nums and weights (probabilities) in _probs
        """
        assert len(self._nums) == len(self._probs), "Specified numbers and \
            their associated probabilities lists must have equal length."
        
        rnd = random.random()
        for (i, prob) in enumerate(self._probs):
            if rnd < prob:
                return self._nums[i]
            rnd -= self._probs[i]
    
    def run_generator(self, num_runs: int, visualize=True) -> dict:
        """
        Runs the generator a specified number of times. Plots the results
        in a simple bar chart
        """
        results = defaultdict(int)
        for i in range(num_runs):
            num = self.next_num()
            results[num] += 1

        if visualize:
            # show the results in a bar chart
            fig, ax = plt.subplots()
            bars = ax.bar(list(results.keys()), list(results.values()))
            ax.bar_label(bars)
            plt.show()

        return results


def main():
    num_gen = RandomGen()
    num_gen.seed(10)
    num_gen.run_generator(10000)

if __name__ == "__main__":
    main()