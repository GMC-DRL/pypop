"""This is a simple demo that optimize 6 Global Trajectory Optimization problems provided by `pykep`:
    https://esa.github.io/pykep/
    https://esa.github.io/pykep/examples/ex13.html
"""
import pygmo as pg  # it's better to use conda to install (and it's better to use pygmo==2.18)
import pykep as pk  # it's better to use conda to install
import matplotlib.pyplot as plt

from pypop7.optimizers.pso.spso import SPSO as Solver


fig, axes = plp.subplots(nrows=3, ncols=2, sharex='col', sharey='row', figsize=(15, 15))
problems = [pk.trajopt.gym.cassini2, pk.trajopt.gym.eve_mga1dsm, pk.trajopt.gym.messenger,
            pk.trajopt.gym.rosetta, pk.trajopt.gym.em5imp, pk.trajopt.gym.em7imp]

for prob_number in range(0, 6):
    udp = problems[prob_number]

    def udpfunc(x):
        return udp.fitness(x)[0]

    prob = pg.problem(udp)

    pro = {'fitness_function': udpfunc,
           'ndim_problem': prob.get_nx(),
           'lower_boundary': prob.get_lb(),
           'upper_boundary': prob.get_ub()}
    opt = {'seed_rng': 0,
           'max_function_evaluations': 2e4,
           'saving_fitness': 1}
    solver = Solver(pro, opt)
    res = solver.optimize()
    if prob_number == 0:
        axes[0, 0].semilogy(res['fitness'][:, 0], res['fitness'][:, 1], 'k--', label='SPSO')
        axes[0, 0].set_title('cassini2')
    elif prob_number == 1:
        axes[0, 1].semilogy(res['fitness'][:, 0], res['fitness'][:, 1], 'k--', label='SPSO')
        axes[0, 1].set_title('eve_mga1dsm')
    elif prob_number == 2:
        axes[1, 0].semilogy(res['fitness'][:, 0], res['fitness'][:, 1], 'k--', label='SPSO')
        axes[1, 0].set_title('messenger')
    elif prob_number == 3:
        axes[1, 1].semilogy(res['fitness'][:, 0], res['fitness'][:, 1], 'k--', label='SPSO')
        axes[1, 1].set_title('rosetta')
    elif prob_number == 4:
        axes[2, 0].semilogy(res['fitness'][:, 0], res['fitness'][:, 1], 'k--', label='SPSO')
        axes[2, 0].set_title('em5imp')
    elif prob_number == 5:
        axes[2, 1].semilogy(res['fitness'][:, 0], res['fitness'][:, 1], 'k--', label='SPSO')
        axes[2, 1].set_title('em7imp')
for ax in axes.flat:
    ax.set(xlabel='Function Evaluations', ylabel='Fitness [m/s]')
    ax.grid()
plt.savefig('pykep_optimization.jpg')  # to save locally
