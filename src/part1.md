# Sparse LWE Kit

## Sparse Secrets

**Sparse secret** is an umbrella term for several related concepts within the FHE literature and among its many implementations.
The idea in common between many of these definitions is a secret key with a ‘sufficiently small’ publicly-known Hamming weight (number of non-zero values contained inside a vector).
This type of secret is chosen to minimize and/or bound the error growth during FHE computation.
Here we will not try to quantify what Hamming weight corresponds to a sparse secret, since this is irrelevant to security estimations.
There are already a few different variations of sparse secrets, and many more could be imagined.

We start by describing traditional (non-sparse) secret keys.
There are four main random distributions used for coefficients of secret keys: uniform binary, uniform ternary, discretized Gaussian and uniform.
It is natural to design a secret key of size n containing h ones (resp. 1 and -1), with the remaining values being zeros, and calling it a sparse binary secret (resp. sparse ternary secret) if h is small enough, or calling it fixed-Hamming-weight binary secret (resp. fixed-Hamming-weight ternary secret).
One could define a similar secret with the uniform distribution instead.
A common choice of Hamming weight in the literature is h = 64, however, a variety of Hamming weights are considered in practice from 32 up to 1024. As mentioned above, there are many variations of sparse secrets, for instance:
- a sparse ternary secret could also publicly provide the number of 1s and -1s it holds;
- a sparse secret could allow any Hamming weight below the threshold h;
- a sparse secret where each element is sampled from a Gaussian with mean 0 and sigma = 0.01.

## Goals

The sparseLWEkit aims to provide parameter sets for FHE schemes with sparse secrets and to increase transparency in parameter selection and in cryptanalysis efforts.
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

