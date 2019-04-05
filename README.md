# pdepy
[![Build Status](https://travis-ci.org/Walden-Shen/pdepy.svg?branch=master)](https://travis-ci.org/Walden-Shen/pdepy)

This framework helps users solve paritial differential equations using finite difference method. Users are allowed to add any differential operators, or change the order of accuracy of the existing operators by modifying their stencils.

## Supported PDEs
### 2D Linear (Constant/Variable Coefficient) PDEs on Regular/Irregular Domains
Default rate of convergence: second-order of accuracy.  
Documentations: https://github.com/Walden-Shen/pdepy/blob/master/docs/2dPDE.ipynb

### Linear (Constant/Variable coefficient) Time-dependent PDEs
#### 1D Problems
Default algorithm: Crank-Nicolson method (fourth-order of accuracy & unconditionally stable).  
Documentations: https://github.com/Walden-Shen/pdepy/blob/master/docs/time_dependent_PDEs.ipynb

#### 2D Problems on Regular Domains
Default algorithm: the explicit method (conditionally stable).  
Documentations: https://github.com/Walden-Shen/pdepy/blob/master/docs/time_dependent_PDEs.ipynb