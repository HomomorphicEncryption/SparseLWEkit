#### Rule of thumb when the estimators do not provide a result

There is a general **rule of thumb** that can be used to have an intuition on the security estimates of a parameter set **when the estimators are not providing a result**: if you fix all the parameters but one, modifying this specific parameter _(only this one)_ has the following impact on security:

- **Fix all the parameters but ctmod**:
    - decreasing ctmod increases the security
    - increasing ctmod decreases the security 
- **Fix all the parameters but N**:
    - increasing N increases the security
    - decreasing N decreases the security
- **Fix all the parameters but HW**:
    - decreasing HW decreases the security
    - increasing HW increases the security

This rule of thumb was used to estimate the security of the parameter set ID 8 (DESILO FHE). The lattice estimator was not able to provide a proper security estimate for this parameter set, however it was able to estimate the parameter set ID 10. In the case of parameter set ID 10, the lattice estimator gave an estimate for security of 237 bits with the attack _bdd_mitm_hybrid_. It is then possible to use the rule of thumb on N to observe that the security of ID 8 is greater or equal to that of ID 10.


### Notes

There are also some pre-existing tables for sparse secrets in particular.
TODO: comment on how we differ from these and why.
- Sparse secret parameter [tables](https://eprint.iacr.org/2021/039.pdf).
- Sparse secret [tables](https://eprint.iacr.org/2019/1148.pdf).


## Running Security Estimation

### Lattice Estimator

#### Installation

1. Install [SageMath](https://doc.sagemath.org/html/en/installation/index.html)
1. Clone the [Lattice Estimator](https://github.com/malb/lattice-estimator) repository: ```git clone git@github.com:malb/lattice-estimator.git```

#### Estimation

1. Open a terminal in the `lattice-estimator` folder and run SageMath: ```sage```
1. On SageMath import useful components:
    ```python
    from estimator import *
    from estimator.lwe_parameters import LWEParameters
    from estimator.nd import NoiseDistribution, stddevf
    ```
1. Define a new parameter set to estimate:
    ```python
    new_parameter_set = LWEParameters(
        n=2**12,
        q = 2**128,
        Xs=ND.SparseTernary(92), # 92 is the number of 1's, same for -1's, so hw = 192 here
        Xe=ND.DiscreteGaussian(stddev=3.19)
    )
    ```
1. Run the estimates:
    ```python
    LWE.estimate(new_parameter_set, red_cost_model = RC.BDGL16, deny_list=["arora-gb"])
    ```

The estimator provides a result that looks like the following:
```python
bkw                  :: rop: ≈2^409.6, m: ≈2^390.9, mem: ≈2^391.9, b: 3, t1: 41, t2: 190, ℓ: 2, #cod: ≈2^11.8, #top: 0, #test: 440, tag: coded-bkw
usvp                 :: rop: ≈2^105.6, red: ≈2^105.6, δ: 1.005443, β: 251, d: 7799, tag: usvp
bdd                  :: rop: ≈2^105.1, red: ≈2^105.1, svp: ≈2^99.6, β: 249, η: 285, d: 7903, tag: bdd
bdd_hybrid           :: rop: ≈2^104.6, red: ≈2^104.6, svp: ≈2^99.4, β: 236, η: 29, ζ: 257, |S|: ≈2^68.0, d: 7767, prob: 0.387, ↻: 10, tag: hybrid
dual                 :: rop: ≈2^106.3, mem: ≈2^60.5, m: ≈2^12.0, β: 253, d: 8077, ↻: 1, tag: dual
dual_hybrid          :: rop: ≈2^104.2, red: ≈2^104.2, guess: ≈2^97.3, β: 246, p: 2, ζ: 0, t: 80, β': 246, N: ≈2^44.7, m: ≈2^12.0
{'bkw': rop: ≈2^409.6, m: ≈2^390.9, mem: ≈2^391.9, b: 3, t1: 41, t2: 190, ℓ: 2, #cod: ≈2^11.8, #top: 0, #test: 440, tag: coded-bkw,
 'usvp': rop: ≈2^105.6, red: ≈2^105.6, δ: 1.005443, β: 251, d: 7799, tag: usvp,
 'bdd': rop: ≈2^105.1, red: ≈2^105.1, svp: ≈2^99.6, β: 249, η: 285, d: 7903, tag: bdd,
 'bdd_hybrid': rop: ≈2^104.6, red: ≈2^104.6, svp: ≈2^99.4, β: 236, η: 29, ζ: 257, |S|: ≈2^68.0, d: 7767, prob: 0.387, ↻: 10, tag: hybrid,
 'bdd_mitm_hybrid': rop: ≈2^106.5, red: ≈2^106.3, svp: ≈2^103.6, β: 233, η: 2, ζ: 511, |S|: ≈2^143.9, d: 7480, prob: 0.072, ↻: 62, tag: hybrid,
 'dual': rop: ≈2^106.3, mem: ≈2^60.5, m: ≈2^12.0, β: 253, d: 8077, ↻: 1, tag: dual,
 'dual_hybrid': rop: ≈2^104.2, red: ≈2^104.2, guess: ≈2^97.3, β: 246, p: 2, ζ: 0, t: 80, β': 246, N: ≈2^44.7, m: ≈2^12.0}
```

The estimated security is the smallest exponent in the `rop` values. As instance, here it estimates `104.2` bits of security (best attack is the `dual_hybrid` attack). This is not enough security: we suggest having at least `128` bits of security at least.

#### Note on Running Time

TODO

### [SparseLWE-estimator](https://github.com/yonghaason/SparseLWE-estimator)

#### Installation

TODO

#### Estimation

```python
# piece of python code

# TODO
```

#### Note on Running Time

TODO: if necessary!

### [LWE-benchmarking](https://github.com/facebookresearch/LWE-benchmarking)

#### Installation

TODO

#### Estimation

```python
# piece of python code

# TODO
```

#### Note on Running Time

TODO: if necessary!

####

## Comments on how non-implemented attacks could affect the estimates

Can we predict how security will change over time?


<!-- more things -->

