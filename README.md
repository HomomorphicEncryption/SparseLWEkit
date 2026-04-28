# Sparse LWE Kit

## Remaining TODOs

Collating TODOs here to make it easier for people to see.

0. h vs HW to refer to hamming weight -- disambiguation.
1. Parameter set 10 origin?
2. Security estimations section has some gaps -- fill in.
3. Indicate when the estimator didn't estimate all attacks.
4. Estimator has some updates (thanks Tabby!) and now estimates a wider range of attacks -- check the current parameters in the latest estimator update
5. Rule of thumb: where it is applied? Why does the estimator not work in these cases?
6. Comment on differences from pre-existing sparse secret tables.
7. Fill in gaps on additional estimators (similarly to LWE estimator).
8. Check in and synchronise with other groups (esp. benchmarking) who may wish to make use of sparse secrets.
9. Use Tabby's attack estimator update to check existing parameters.
10. Decide what to do about this.
11. Automated pipeline for running the estimator (subject to changes on the estimator)

## Sparse Secrets

**Sparse secret** is an umbrella term for several related concepts within the FHE literature and among its many implementations.
The idea in common between many of these definitions is a secret key with a ‘sufficiently small’ publicly-known Hamming weight (number of non-zero values contained inside a vector).
This type of secret can be chosen for several reasons, including minimizing and/or bounding the error growth during FHE computation, and improving bootstrapping (lower failure probability and/or smaller modulus consumption).
In this webpage we will not try to quantify what specific Hamming weight corresponds to a sparse secret, but rather we will consider concrete values of the Hamming Weight.

We start by describing traditional (non-sparse) secret keys.
There are four main random distributions used for coefficients of secret keys: 
- uniform binary;
- uniform ternary;
- discretized Gaussian;
- uniform modulo an integer q.

There are variants of each of these distributions described as follows:
- a secret key of dimension n is sparse if it contains h < n/2 non-zero entries;
- a secret key  is a fixed-Hamming-weight secret if it has a set value of h.

Common choices of Hamming weight in the literature and implementations are h = 64 and h = 92, however, a variety of Hamming weights are considered in practice from 32 up to 1024. 

There are several variations of sparse secrets.
We do not yet consider these, but some possible distributions include:
- a sparse ternary secret could also publicly provide the number of 1's and -1's it holds;
- a sparse secret could allow any Hamming weight below the threshold h;
- a secret where each element is sampled from an integer Gaussian with mean 0 and sigma = 0.01 could be defined as a sparse secret, even though the Hamming weight becomes a random variable.


## Goals

The sparseLWEkit aims to provide parameter sets for FHE schemes with sparse secrets and to increase transparency in parameter selection and in cryptanalysis efforts.
To enable this, we give an overview of where different cryptanalysis work is currently implemented and give justification of how libraries choose parameters with sparse secrets.

## Cryptanalysis disclaimer

Users of the sparseLWEkit, and users of any parameter selection tool, should be aware that cryptanalysis is always a work in progress.
New attacks may be found at any time, and the landscape is always susceptible to evolve.
The costs of known attacks can also be revised (upwards and downwards) thanks to refined analyses.

Attacks we are already aware of and may be competitive either need to be better studied and discarded, or incorporated into existing tools for use in parameter selection.
This means that **existing tools may not give a completely accurate estimate of security**.
Existing tools may also take a **long time to run**.
In order to mitigate against confusion caused by long running time, we report running time for the tables we provide.
We hope this gives users an idea of how long they can expect parameter generation to take.

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
- [Cool + Cruel = Dual](https://gitlab.com/fvirdia/cool-plus-cruel-equals-dual#running-dropsolve-experiments) from [this paper](https://eprint.iacr.org/2025/1002.pdf).

## Supported Attacks for Each Tool

Here we give a table listing attacks which may be among the most competitive for sparse secret LWE instances, and we describe which tool(s) estimates their cost.
Where possible we provide a link to the implementation of the estimate. 

| Attack                                                                              | [Lattice estimator](https://github.com/malb/lattice-estimator)                                                            | [LWE-benchmarking](https://github.com/facebookresearch/LWE-benchmarking)   | [SparseLWE-estimator](https://github.com/yonghaason/SparseLWE-estimator)   | [PrimalMeetLWE](https://github.com/yonghaason/PrimalMeetLWE/tree/main/estimator)   |
|:------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------|:---------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
| [C:HowgraveGraham07](https://www.iacr.org/archive/crypto2007/46220150/46220150.pdf) | [✅](https://lattice-estimator.readthedocs.io/en/latest/algorithms/lwe-primal.html)                                        | ❌                                                                          | ❌                                                                          | ❌                                                                                  |
| [EC:Albrecht17](https://eprint.iacr.org/2017/047.pdf)                               | [✅](https://lattice-estimator.readthedocs.io/en/latest/algorithms/lwe-dual.html)                                          | ❌                                                                          | ❌                                                                          | ❌                                                                                  |
| [IEEEAccess:CHHS19](https://eprint.iacr.org/2019/1114.pdf)                          | [✅](https://lattice-estimator.readthedocs.io/en/latest/algorithms/lwe-dual.html)                                          | ❌                                                                          | ✅                                                                          | ❌                                                                                  |
| [WAHC:SC19](https://eprint.iacr.org/2019/1019.pdf)                                  | [✅](https://lattice-estimator.readthedocs.io/en/latest/_apidoc/estimator.prob/estimator.prob.mitm_babai_probability.html) | ❌                                                                          | ✅                                                                          | ❌                                                                                  |
| [Eprint:EJK20](https://eprint.iacr.org/2020/515.pdf)                                | [✅](https://lattice-estimator.readthedocs.io/en/latest/algorithms/lwe-dual.html)                                          | ❌                                                                          | ❌                                                                          | ❌                                                                                  |
| [AC:GJ21](https://www.iacr.org/archive/asiacrypt2021/130900114/130900114.pdf)🔒      | [✅](https://lattice-estimator.readthedocs.io/en/latest/_apidoc/estimator.lwe_dual/estimator.lwe_dual.dual_hybrid.html) ⚠️ | ❌                                                                          | ❌                                                                          | ❌                                                                                  |
| [IMACC:KM21](https://eprint.iacr.org/2021/1255.pdf)                                 | ❌                                                                                                                         | ❌                                                                          | ❌                                                                          | ❌                                                                                  |
| [C:May21](https://eprint.iacr.org/2021/216.pdf)                                     | ❌                                                                                                                         | ❌                                                                          | ❌                                                                          | ❌                                                                                  |
| [ACISP:BLLW22](https://eprint.iacr.org/2022/1330.pdf)🔒                              | ❌                                                                                                                         | ❌                                                                          | ❌                                                                          | ❌                                                                                  |
| [Eprint:HKLS22](https://eprint.iacr.org/2022/1473.pdf)                              | ❌                                                                                                                         | ❌                                                                          | ❌                                                                          | ✅                                                                                  |
| [NeurIPS:WCCL22](https://arxiv.org/abs/2207.04785)                                  | ❌                                                                                                                         | ✅                                                                          | ❌                                                                          | ❌                                                                                  |
| [CCS:LSWMGCL23](https://eprint.iacr.org/2023/340)                                   | ❌                                                                                                                         | ✅                                                                          | ❌                                                                          | ❌                                                                                  |
| [NeurIPS:YWACL23](https://eprint.iacr.org/2023/968)                                 | ❌                                                                                                                         | ✅                                                                          | ❌                                                                          | ❌                                                                                  |
| [Eprint:LLSW24](https://eprint.iacr.org/2024/824)                                   | ❌                                                                                                                         | ✅                                                                          | ❌                                                                          | ❌                                                                                  |
| [AFRICAC:NMWSYCL24](https://eprint.iacr.org/2024/443.pdf)                           | ❌                                                                                                                         | ✅                                                                          | ❌                                                                          | ❌                                                                                  |
| [Eprint:SWYNSCL24](https://eprint.iacr.org/2024/150)                                | ❌                                                                                                                         | ✅                                                                          | ❌                                                                          | ❌                                                                                  |

#### Notes
- The tools in this table are listed in order of the number of attacks they implement, i.e. the number of check marks. Where the numbers of attacks supported are the same, tools are listed alphabetically.
- 🔒 means that there is an implementation but it is not publicly available.
- ⚠️ means that the tool only partially implements this attack (for example only the non-sparse variant is implemented).

## Parameter Sets

In this section we give examples of some parameter sets and their current security levels.
For further information about how the security levels are obtained, please refer the later table comparing the estimation tools.

|   ID |   log2(skdim) |    σ |   log2(ctmod) |   HW | Origin                                                                                                                                                 |
|-----:|--------------:|-----:|--------------:|-----:|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
|    3 |            16 | 3.2  |           117 |   32 | [HEaaN](https://heaan.it/)                                                                                                                             |
|    8 |            16 | 3.2  |           300 |  128 | [DESILO FHE](https://fhe.desilo.dev/latest/)                                                                                                           |
|   10 |            15 | 3.2  |           300 |  128 |                                                                                                                                                        |
|    1 |            17 | 3.2  |          2341 |  128 | [HEaaN](https://heaan.it/)                                                                                                                             |
|    9 |            16 | 3.2  |            61 |  192 | [Lattigo](https://github.com/tuneinsight/lattigo/blob/84f6bc33cb5bd086f595ea3cc2b63f4dd74b2662/circuits/ckks/bootstrapping/parameters_literal.go#L125) |
|    5 |            15 | 3.19 |           767 |  192 | [OpenFHE](https://openfhe.org/)                                                                                                                        |
|    4 |            15 | 3.2  |           777 |  192 | [HEaaN](https://heaan.it/)                                                                                                                             |
|    6 |            16 | 3.19 |          1553 |  192 | [OpenFHE](https://openfhe.org/) [Lattigo](https://pkg.go.dev/github.com/tuneinsight/lattigo/v6)                                                        |
|    2 |            16 | 3.2  |          1555 |  192 | [HEaaN](https://heaan.it/)                                                                                                                             |
|    7 |            17 | 3.19 |          3104 |  192 | [OpenFHE](https://openfhe.org/)                                                                                                                        |


Note: In this table, parameter sets are listed in order of increasing Hamming weight and then increasing log2(ctmod). Where parameter sets have the same Hamming weight we list them in alphabetical order by library.

#### Notations
- skdim: dimension of the secret key of the LWE/RLWE instance (corresponding to the size of the polynomials in RLWE), earlier called n in this page
- σ: standard deviation of the noise at secret key encryption time
- log2(ctmod): log2 of the (maximal) ciphertext modulus (for instance ctmod often corresponds to Q, or to PQ in the CKKS context)
- HW: Hamming weight of the secret key, earlier called h in this page

#### Instantiation with two parameter sets at once

The [sparse secret encapsulation technique](https://eprint.iacr.org/2022/024) is a CKKS bootstrapping variant that relies on a temporary secret key at some stage in the bootstrapping process, and whose purpose is to increase the bootstrapping performance and to lower the bootstrapping failure probability. Relying on this technique hence leads to two combined parameter sets in some CKKS implementations. For example, in the table above, the HEAAN parameters ID 1 and ID 2 are combined. 

TODO: mention the other parameter sets that come together, and Lattigo special case and DESILO special case?
TODO: mention that a similar technique exists for BGV (used in (older?) Helib) and BFV. 


### Security Estimations

The following table provides, for every parameter set and for each tool, the security estimate (on top) and the running time to get it (at the bottom).
The following architecture was used to run the estimations: ...

TODO: fill with the description of the machine used to run the estimations.

|   ID | [Lattice estimator](https://github.com/malb/lattice-estimator)   |
|-----:|:-----------------------------------------------------------------|
|    1 | 157.19 bits (CHHS19_mitm) 1h47m0.5s                              |
|    2 | 133.84 bits (bdd_mitm_hybrid) 49m46.5s                           |
|    3 | 164.58 bits (CHHS19_mitm) 30m14.7s                               |
|    4 | 132.12 bits (CHHS19_mitm) 36m47.2s                               |
|    5 | 134.3 bits (bdd_mitm_hybrid) 34m25.6s                            |
|    6 | 133.99 bits (bdd_mitm_hybrid) 51m9.1s                            |
|    7 | 135.28 bits (CHHS19_mitm) 1h40m23.0s                             |
|    8 | 321.96 bits (CHHS19_mitm) 1h24m21.5s                             |
|    9 | 734.16 bits (CHHS19_mitm) ???                                    |
|   10 | 232.52 bits (CHHS19_mitm) ???                                    |

TODO: need to indicate in the table when the lattice estimator did not estimate all the attacks.

#### Rule of thumb when the estimators do not provide a result

There is a general **rule of thumb** that can be used to have an intuition on the security estimates of a parameter set **when the estimators are not providing a result**: if you fix all the parameters but one, modifying this specific parameter _(only this one)_ has the following impact on security:

- **Fix all the parameters but ctmod**:
    - decreasing ctmod increases security,
    - increasing ctmod decreases security. 
- **Fix all the parameters but skdim**:
    - decreasing skdim decreases security,
    - increasing skdim increases security.
- **Fix all the parameters but HW**:
    - decreasing HW decreases security,
    - increasing HW increases security.

This rule of thumb was used to estimate the security of the parameter set ID 8 (DESILO FHE). The lattice estimator was not able to provide a proper security estimate for this parameter set, however it was able to estimate the parameter set ID 10. In the case of parameter set ID 10, the lattice estimator gave an estimate for security of 232.52 bits with the attack _bdd_mitm_hybrid_. It is then possible to use the rule of thumb on N to observe that the security of ID 8 is greater or equal to that of ID 10.


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
        Xs=ND.SparseTernary(92), # 92 is the number of 1's, same for -1's, so hw = 184 here
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

The estimated security is the smallest exponent in the `rop` values. As instance, here it estimates `104.2` bits of security (best attack is the `dual_hybrid` attack). This is not enough security: we suggest having `128` bits of security at least.

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

