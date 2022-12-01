"""This code only tests whether the corresponding optimizer could run or not.
  In other words, it *cannot* validate the correctness regarding its working procedure.
  For the correctness validation of programming, refer to the following link:
    https://github.com/Evolutionary-Intelligence/pypop/wiki/Correctness-Validation-of-Optimizers.md
"""
import unittest
import time
import numpy as np

from pypop7.benchmarks.base_functions import ellipsoid, sphere, cigar
from pypop7.optimizers.cc.cosyne import COSYNE as Solver


class TestSCEM(unittest.TestCase):
    def test_optimize(self):
        start_run = time.time()
        ndim_problem = 10
        for f in [ellipsoid, sphere, cigar]:
            print('*' * 7 + ' ' + f.__name__ + ' ' + '*' * 7)
            problem = {'fitness_function': f,
                       'ndim_problem': ndim_problem,
                       'lower_boundary': -5 * np.ones((ndim_problem,)),
                       'upper_boundary': 5 * np.ones((ndim_problem,))}
            options = {'max_function_evaluations': 3e5,
                       'fitness_threshold': 1e-10,
                       'n_individuals': 20,
                       'n_combine': 2,
                       'prob_mutate': 0.3,
                       'crossover_type': "one_point",
                       'verbose_frequency': 20,
                       'record_fitness': True,
                       'record_fitness_frequency': 1}
            solver = Solver(problem, options)
            results = solver.optimize()
            print(results)
            print('*** Runtime: {:7.5e}'.format(time.time() - start_run))


if __name__ == '__main__':
    unittest.main()