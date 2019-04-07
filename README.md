# pdepy
[![Build Status](https://travis-ci.org/Walden-Shen/pdepy.svg?branch=master)](https://travis-ci.org/Walden-Shen/pdepy)

This library helps users solve paritial differential equations using finite difference methods. Users are allowed to add any differential operators, or change the order of accuracy of the existing operators by modifying their stencils.

## Gist of This Library
- User Friendly  
Whatever type of PDE the user wants to solve, all he/she needs to do is to set the boundary condition, plug PDE into the solver, and finally call the function **solve()**. No need to memorize tons of APIs, since the solver will automatically detect the type of the PDE, whether its domain is regular, etc., and select the appropriate algorithm for you.  
     
     
- Extensible & Easy to Extend  
It's impossible that the library will meet all needs from its users, e.g., higher-order differential operators, more accurate approximation, etc. So when I was designing this library, I made it extremely easy to add new operators, or to modify the existing numerical stencil.  


For further introduction to this library, please go to https://github.com/Walden-Shen/pdepy/blob/master/docs/introduction_to_pdepy.ipynb

## Supported PDEs
### 2D Linear (Constant/Variable Coefficient) PDEs on Regular/Irregular Domains with Dirichlet Boundary Condition
Default rate of convergence: second-order of accuracy.  
Documentations: https://github.com/Walden-Shen/pdepy/blob/master/docs/2dPDEs.ipynb

### Linear (Constant/Variable coefficient) Time-dependent PDEs
#### 1D Problems
Default algorithm: Crank-Nicolson method (unconditionally stable).  
Documentations: https://github.com/Walden-Shen/pdepy/blob/master/docs/time_dependent_PDEs.ipynb

#### 2D Problems on Regular Domains
Default algorithm: the explicit method (conditionally stable).  
Documentations: https://github.com/Walden-Shen/pdepy/blob/master/docs/time_dependent_PDEs.ipynb