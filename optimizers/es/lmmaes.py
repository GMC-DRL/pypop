import numpy as np

from optimizers.es.maes import MAES


class LMMAES(MAES):
    """Limited-Memory Matrix Adaptation Evolution Strategy (LMMAES).

    Reference
    ---------
    Loshchilov, I., Glasmachers, T. and Beyer, H.G., 2019.
    Large scale black-box optimization by limited-memory matrix adaptation.
    IEEE Transactions on Evolutionary Computation, 23(2), pp.353-358.
    https://ieeexplore.ieee.org/abstract/document/8410043
    """
    def __init__(self, problem, options):
        MAES.__init__(self, problem, options)
        n_evolution_paths = 4 + int(np.floor(3 * np.log(self.ndim_problem)))
        self.n_evolution_paths = options.get('n_evolution_paths', n_evolution_paths)  # m in Algorithm 1
        self.c_s = options.get('c_s', 2 * self.n_parents / self.ndim_problem)
        self._s_1 = 1 - self.c_s  # for Line 13 in Algorithm 1
        self._s_2 = np.sqrt(self.mu_eff * self.c_s * (2 - self.c_s))  # for Line 13 in Algorithm 1
        self._c_d = 1 / (self.ndim_problem * np.power(1.5, np.arange(self.n_evolution_paths)))
        self._c_c = self.n_parents / (self.ndim_problem * np.power(4.0, np.arange(self.n_evolution_paths)))

    def initialize(self):
        z = np.empty((self.n_individuals, self.ndim_problem))  # Gaussian noise for mutation
        d = np.empty((self.n_individuals, self.ndim_problem))  # search directions
        mu = self._initialize_mu()  # mean of Gaussian search distribution
        s = np.zeros((self.ndim_problem,))  # evolution path
        tm = np.zeros((self.n_evolution_paths, self.ndim_problem))  # transformation matrix M
        y = np.empty((self.n_individuals,))  # fitness (no evaluation)
        return z, d, mu, s, tm, y

    def iterate(self, z=None, d=None, mu=None, s=None, tm=None, y=None, args=None):
        for k in range(self.n_individuals):
            if self._check_terminations():
                return z, d, y
            z[k] = self.rng_optimization.standard_normal((self.ndim_problem,))
            d[k] = z[k]
            for j in range(np.minimum(self.n_generations, self.n_evolution_paths)):
                d[k] = (1 - self._c_d[j]) * d[k] + self._c_d[j] * tm[j] * np.dot(tm[j], d[k])
            y[k] = self._evaluate_fitness(mu + self.sigma * d[k], args)
        return z, d, y

    def _update_distribution(self, z=None, d=None, mu=None, s=None, tm=None, y=None):
        order = np.argsort(y)
        d_w, z_w = np.zeros((self.ndim_problem,)), np.zeros((self.ndim_problem,))
        for k in range(self.n_parents):
            d_w += self.w[k] * d[order[k]]
            z_w += self.w[k] * z[order[k]]
        # update distribution mean
        mu += (self.sigma * d_w)
        # update evolution path (s) and transformation matrix (M)
        s = self._s_1 * s + self._s_2 * z_w
        for k in range(self.n_evolution_paths):
            tm[k] = (1 - self._c_c[k]) * tm[k] + np.sqrt(self.mu_eff * self._c_c[k] * (2 - self._c_c[k])) * z_w
        # update global step-size
        self.sigma *= np.exp(self.c_s / 2 * (np.sum(np.power(s, 2)) / self.ndim_problem - 1))
        return mu, s, tm
