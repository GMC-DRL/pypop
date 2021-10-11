# pypop

```PyPop``` is a *Pure-PYthon* library of **POPulation-based OPtimization** for real-parameter, black-box problems (**currently actively developed**). Its goal is to provide a *unified* interface and also *elegant* implementations for **Derivative-Free Optimization (DFO)**, *particularly population-based optimizers*, in order to facilitate research repeatability and real-world applications.

<p align="center">
<img src="https://github.com/Evolutionary-Intelligence/pypop/blob/main/docs/logo/PyPop-Logo-Small-0.png" alt="drawing" width="321"/>
</p>

## A (*Growing*) List of Available Gradient-Free Optimizers (GFO)

* **Natural Evolution Strategies (NES)** [See e.g. [Wierstra et al., 2014, JMLR](https://jmlr.org/papers/v15/wierstra14a.html)]

  * Rank-One Natural Evolution Strategy (R1NES) [See [Sun et al., 2013, GECCO](https://dl.acm.org/doi/abs/10.1145/2464576.2464608)]

  * Separable Natural Evolution Strategy (SNES) [See [Schaul et al., 2011, GECCO](https://dl.acm.org/doi/abs/10.1145/2001576.2001692)]

* **Evolution Strategies (ES)** [See e.g. [Beyer and Schwefel, 2002, Natural Computing](https://link.springer.com/article/10.1023/A:1015059928466)]

  * Self-Adaptation Evolution Strategy ((μ/μ_I, λ)-σSA-ES) [See e.g. [Beyer, 2020, GECCO](https://dl.acm.org/doi/abs/10.1145/3377929.3389870)]

* **Random (Stochastic) Search (RS)** [See e.g. [Brooks, 1958, Operations Research](https://pubsonline.informs.org/doi/abs/10.1287/opre.6.2.244)]

  * Pure Random Search (PRS) [See e.g. [Bergstra and Bengio, 2012, JMLR](https://www.jmlr.org/papers/v13/bergstra12a.html)]
  
  * Random Hill Climber (RHC)
  
  * Annealed Random Hill Climber (ARHC)

## Research Support

This open-source Python library for black-box optimization is now supported by **Shenzhen Fundamental Research Program** under Grant No. JCYJ20200109141235597 (￥2,000,000), granted to **Prof. Yuhui Shi** (CSE, SUSTech @ Shenzhen, China), and actively developed (from 2021 to 2023) by his group members (e.g., **Qiqi Duan**, *Chang Shao*, Youkui Zhang).
