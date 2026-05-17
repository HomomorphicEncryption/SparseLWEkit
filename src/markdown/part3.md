

Note: In this table, parameter sets are listed in order of increasing Hamming weight and then increasing log2(ctmod). Where parameter sets have the same Hamming weight we list them in alphabetical order by library.

#### Notations
- $n$: dimension of the secret key of the LWE/RLWE instance (corresponding to the size of the polynomials in RLWE), earlier called n in this page
- $\sigma$: standard deviation of the noise at secret key encryption time
- $\log_{2}(\text{q})$: $\log_{2}$ of the (maximal) ciphertext modulus (for instance ctmod often corresponds to $Q$, or to $PQ$ in the CKKS context)
- $h$: Hamming weight of the secret key, earlier called $h$ in this page

#### Instantiation with two parameter sets at once

The [sparse secret encapsulation technique](https://eprint.iacr.org/2022/024) is a CKKS bootstrapping variant that relies on a temporary secret key at some stage in the bootstrapping process, and whose purpose is to increase the bootstrapping performance and to lower the bootstrapping failure probability. Relying on this technique hence leads to two combined parameter sets in some CKKS implementations. For example, in the table above, the HEAAN parameters ID 1 and ID 2 are combined. 

TODO: mention the other parameter sets that come together, and Lattigo special case and DESILO special case?
TODO: mention that a similar technique exists for BGV (used in (older?) Helib) and BFV. 


### Security Estimations

The following table provides, for every parameter set and for each tool, the security estimate (on top) and the running time to get it (at the bottom).
The following architecture was used to run the estimations: ...

TODO: fill with the description of the machine used to run the estimations.

