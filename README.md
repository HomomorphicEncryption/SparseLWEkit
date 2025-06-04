# Sparse LWE Kit

The sparseLWEkit aims to provide parameter sets for FHE schemes with sparse secrets. 
**Sparse secrets** are defined as those which have a Hamming weight that is sufficiently small. Confusingly, ‘sufficiently small’ is defined differently across the literature.
In order to avoid confusion (hopefully), we consider _sparse secrets to be any fixed hamming weight secrets_ and include the hamming weight, h, as a parameter.
In the literature, a common choice of Hamming weight is h = 64.
However, a variety of Hamming weights h are considered from 32 up to 1024. It is important to consider the value of the dimension n in relation to h in order to measure the sparsity of a secret.
Another aim of the project is to increase transparency in parameter selection and cryptanalysis efforts.
To enable this, we give an overview of where different cryptanalysis work is currently implemented and give justification of how libraries choose parameters with sparse secrets.

## Cryptanalysis disclaimer

Users of the sparseLWEkit, and users of any parameter selection tool, should be aware that cryptanalysis is always a work in progress.
New attacks may be found at any time, and the landscape is constantly evolving.
The costs of known attacks can also be revised (upwards and downwards) thanks to refined analyses.

Attacks we are already aware of need to be incorporated into existing tools for use in parameter selection.
This means that **existing tools may not give a completely accurate estimate of security**.
Existing tools may also take a **long time to run**.
In order to mitigate against confusion caused by long running time, we include running time for the tables we provide.
We hope this should give users an idea of how long they can expect parameter generation to take.

<!-- Extra note: I was also wondering about what parameters there are security reductions for? Perhaps we could write about this somewhere. -->

## What tools are already out there?

Disclaimer: These tools either do not incorporate sparse secrets, or do so to a limited extent (only some attacks).

- [Lattice estimator](https://github.com/malb/lattice-estimator), the most commonly used tool.
  - OpenFHE has an [adapted version](https://github.com/openfheorg/openfhe-lattice-estimator) of the lattice estimator for parameter generation of specific
FHE schemes.
  - [TFHE parameter selection tool](https://eprint.iacr.org/2022/704) which gives optimised parameter sets for TFHE as tables in the paper, and is implemented in the [tfhe-rs library](https://github.com/zama-ai/tfhe-rs).
  - Tool from the TII FHE team which gives [specific formulas](https://eprint.iacr.org/2024/1895.pdf) for estimating security. 
  - Security Guidelines for Implementing Homomorphic Encryption, with [tables](https://eprint.iacr.org/2024/463) and also [code](https://github.com/gong-cr/FHE-Security-Guidelines).
- Benchmarking tool from the Meta AI team [Benchmarking Attacks on Learning with Errors (LWE)](https://github.com/facebookresearch/LWE-benchmarking) implementing the Salsa etc line of attacks as well as hybrid MitM attacks.
- [Sparse LWE-specific tool](https://github.com/yonghaason/SparseLWE-estimator) from Yongha Son which is no longer maintained. It implements two papers from 2019 on the [hybrid-dual attack](https://eprint.iacr.org/2019/1114) and [hybrid-primal attack](https://eprint.iacr.org/2019/1019).
- [PrimalMeetLWE](https://github.com/yonghaason/PrimalMeetLWE/tree/main/estimator) from [this paper](https://eprint.iacr.org/2022/1473).

## Supported Attacks for Each Tool

Here we give a table listing sparse secret attacks and we describe which tool(s) estimate their cost.
Where possible we provide a link to the implementation of the estimate. 

| Attack | [Lattice estimator](https://github.com/malb/lattice-estimator) | [SparseLWE-estimator](https://github.com/yonghaason/SparseLWE-estimator) | [LWE-benchmarking](https://github.com/facebookresearch/LWE-benchmarking)
|:-------------------------------------------------------------------------------:|:--:|:--:|:--:|
| [C:HowgraveGraham07](https://www.iacr.org/archive/crypto2007/46220150/46220150.pdf)        | [✅](https://lattice-estimator.readthedocs.io/en/latest/algorithms/lwe-primal.html) | ❌ | ❌ |
| [EC:Albrecht17](https://eprint.iacr.org/2017/047.pdf)                                      | [✅](https://lattice-estimator.readthedocs.io/en/latest/algorithms/lwe-dual.html) | ❌ | ❌ |
| [IEEEAccess:CHHS19](https://eprint.iacr.org/2019/1114.pdf)                                 | [✅](https://lattice-estimator.readthedocs.io/en/latest/algorithms/lwe-dual.html) | ✅ | ❌ |
| [WAHC:SC19](https://eprint.iacr.org/2019/1019.pdf)                                 | [✅](https://lattice-estimator.readthedocs.io/en/latest/_apidoc/estimator.prob/estimator.prob.mitm_babai_probability.html) | ✅ | ❌ |
| [Eprint:EJK20](https://eprint.iacr.org/2020/515.pdf)                                  | [✅](https://lattice-estimator.readthedocs.io/en/latest/algorithms/lwe-dual.html) | ❌ | ❌ |
| [C:May21](https://eprint.iacr.org/2021/216.pdf)                                  | ❌ | ❌ | ❌ |
| [IMACC:KM21](https://eprint.iacr.org/2021/1255.pdf)                                 | ❌ | ❌ | ❌ |
| [AC:GJ21](https://www.iacr.org/archive/asiacrypt2021/130900114/130900114.pdf) 🔒 | [✅](https://lattice-estimator.readthedocs.io/en/latest/_apidoc/estimator.lwe_dual/estimator.lwe_dual.dual_hybrid.html) ⚠️ | ❌ | ❌ |
| [ACISP:BLLW22](https://eprint.iacr.org/2022/1330.pdf) 🔒                              | ❌ | ❌ | ❌ |
| [Eprint:HKLS22](https://eprint.iacr.org/2022/1473.pdf) [🔗](https://github.com/yonghaason/PrimalMeetLWE/tree/main/estimator)                            | ❌ | ❌ | ❌ |
| [AFRICAC:NMWSYCL24](https://eprint.iacr.org/2024/443.pdf)                                  | ❌ | ❌ | ✅ |
| [Eprint:LLSW24](https://eprint.iacr.org/2024/824)                                      | ❌ | ❌ | ✅ |
| [NeurIPS:WCCL22](https://arxiv.org/abs/2207.04785)                                      | ❌ | ❌ | ✅ |
| [CCS:LSWMGCL23](https://eprint.iacr.org/2023/340)                                      | ❌ | ❌ | ✅ |
| [NeurIPS:YWACL23](https://eprint.iacr.org/2023/968)                                      | ❌ | ❌ | ✅ |
| [Eprint:SWYNSCL24](https://eprint.iacr.org/2024/150)                                      | ❌ | ❌ | ✅ |

#### Notes
- 🔒 means that there is an implementation but it is not publicly available.
- ⚠️ means that the estimator only partially implements this attack (for example only the non-sparse variant is implemented)

## Parameters Sets

In this section we give examples of some parameter sets and their current security levels.
For further information about how the security levels are obtained, please refer the later table comparing the estimation tools.

| ID | Current Estimation | N     | σ   | PQ     | HW  | ... |
|:--:|:------------------:|:-----:|:---:|:------:|:---:|:---:|
| 1  | 166.7 bits         | 2**14 | 3.2 | 2**300 | 192 | ... |
| 2  |  79 bits           | ?     | ?   | ?      | ?   | ... |
| 3  | 114 bits           | ?     | ?   | ?      | ?   | ... |
| 4  | 130 bits           | ?     | ?   | ?      | ?   | ... |

| ID | Current Estimation | N     | σ   | logPQ  | HW  |
|:--:|:------------------:|:-----:|:---:|:------:|:---:|
|    |                    | 17    | 3.2 |   2341 | 128 |
|    |                    | 16    | 3.2 |   1555 | 192 |
|    |                    | 16    | 3.2 |    117 | 32  |
|    |                    | 15    | 3.2 |    777 | 192 |

#### Notations
- N: dimension of the RLWE instance (size of the polynomials)
- σ: standard deviation of the noise at secret key encryption time
- PQ: largest ciphertext modulus (during key switch)
- Q: ciphertext modulus at maximum level
- P: auxiliary ciphertext modulus
- HW: Hamming weight of the secret key

### Security Estimations

The following table provides, for every parameter set and for each tool, the security estimate (on top) and the running time to get it (in the bottom).
The fallowing architecture was used to run the estimations: ...

<!-- todo: fill with the description of the machine used to run the estimations -->

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

