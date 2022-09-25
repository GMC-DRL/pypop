"""This code only tests whether the corresponding optimizer could run or not.
  In other words, it *cannot* validate the correctness regarding its working procedure.
  For the correctness validation of programming, refer to the following link:
    https://github.com/Evolutionary-Intelligence/pypop/wiki/Correctness-Validation-of-Optimizers.md
"""
import unittest

import time
import numpy as np

from pypop7.benchmarks.base_functions import ellipsoid, rosenbrock
from pypop7.optimizers.ga.genitor import GENITOR as Solver


class TestGENITOR(unittest.TestCase):
    def test_optimize(self):
        start_run = time.time()
        ndim_problem = 100
        for f in [ellipsoid, rosenbrock]:
            print('*' * 7 + ' ' + f.__name__ + ' ' + '*' * 7)
            problem = {'fitness_function': f,
                       'ndim_problem': ndim_problem,
                       'lower_boundary': -5 * np.ones((ndim_problem,)),
                       'upper_boundary': 5 * np.ones((ndim_problem,))}
            options = {'max_function_evaluations': 2e5,
                       'fitness_threshold': 1e-10,
                       'max_runtime': 3600,  # 1 hours
                       'seed_rng': 0,
                       'verbose': 5000,
                       'saving_fitness': 200000}
            solver = Solver(problem, options)
            results = solver.optimize()
            print(results)
            print('*** Runtime: {:7.5e}'.format(time.time() - start_run))


if __name__ == '__main__':
    unittest.main()