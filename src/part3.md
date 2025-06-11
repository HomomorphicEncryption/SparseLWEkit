

TODO: come up with a way to sort the lines to avoid an unfair display (current estimation, log2(N), ...).

#### Notations
- log2(N): log2 of the dimension of the RLWE instance (size of the polynomials)
- σ: standard deviation of the noise at secret key encryption time
- log2(ctmod): log2 of the ciphertext modulus (for instance Q corresponds to PQ in the CKKS context)
- HW: Hamming weight of the secret key

### Security Estimations

The following table provides, for every parameter set and for each tool, the security estimate (on top) and the running time to get it (at the bottom).
The following architecture was used to run the estimations: ...

TODO: fill with the description of the machine used to run the estimations.

_(version A: without the best attack)_

| ID  |          Tool A             |            Tool B              |
|:---:|:---------------------------:|:------------------------------:|
| 1   |  180 bits <br> _502 min_    |  __166.7 bits__ <br> _16 min_  |
| 2   |  __79 bits__  <br> _? min_  |  83 bits  <br> _? min_         | 
| 3   |  __114 bits__  <br> _? min_ |  129 bits  <br> _? min_        | 
| 4   |  141 bits  <br> _? min_     |  __130 bits__  <br> _? min_    | 

_(version B: with the best attack)_

| ID  | Best Attack | Tool A |Tool B |
|:---:|:-----------:|:------:|:------:|
| 1   | [C:HowgraveGraham07](https://www.iacr.org/archive/crypto2007/46220150/46220150.pdf) |  180 bits <br> _502 min_ | __166.7 bits__  <br> _16 min_ |
| 2   | [C:May21](https://eprint.iacr.org/2021/216.pdf) |  __79 bits__ <br> _? min_  | 83 bits <br> _? min_  |
| 3   | [Eprint:LLSW24](https://eprint.iacr.org/2024/824) |  __114 bits__ <br> _? min_  | 129 bits <br> _? min_  |
| 4   | [Eprint:SWYNSCL24](https://eprint.iacr.org/2024/150) |  141 bits <br> _? min_  | __130 bits__ <br> _? min_  |


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

