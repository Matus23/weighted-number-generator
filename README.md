## To run weighted pseudo random number generator
```
python main.py
```
This sets a seed to produce replicable results, generates 10,000 random results 
based on the distribution specified in the handout and plots the generated 
distribution in a simple bar chart. 

To change the distribution/range of numbers to generate - either update them in 
code or update `config.json` and use method `load_config_from_file`.

## To run unit tests
```
python -m unittest tests.tests
```

Ensuring the random number generator works as expected can be hardly 
accomplished through unit testing. I implemented one unit test that checks
`next_num()` works as expected with a specified seed and default configuration.

I added two more unit tests to ensure that the numbers and their probabilities are valid.

## Areas for improvement or How to make it more pythonic
* One of the perks of python is its succinctness. Right now the code contains a bit of fluff (unnecessary comments, robust structure).
* I bypassed handling of the floating-point arithmetic by using round function with precision to 5 decimal points - a more elaborate might could be used.
* Should the algorithm be used for long inputs or in a production environment, the code could be sped up (e.g. by using numpy).
* Unit testing is not sufficient to ensure correct functioning of the number generator. I added a method to display results of 10,000 runs in a simple bar chart but a more systematic approach should be used in production env.