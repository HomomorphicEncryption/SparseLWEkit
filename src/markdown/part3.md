

Note: In this table, parameter sets are listed in order of increasing Hamming weight and then increasing log2(ctmod). Where parameter sets have the same Hamming weight we list them in alphabetical order by library.

#### Notations
- skdim: dimension of the secret key of the LWE/RLWE instance (corresponding to the size of the polynomials in RLWE), earlier called n in this page
- σ: standard deviation of the noise at secret key encryption time
- log2(ctmod): log2 of the (maximal) ciphertext modulus (for instance ctmod often corresponds to Q, or to PQ in the CKKS context)
- HW: Hamming weight of the secret key, earlier called h in this page

#### Instantiation with two parameter sets at once

TODO: encapsulation technique and mention the parameter sets that come together, and Lattigo special case and DESILO special case?

### Security Estimations

The following table provides, for every parameter set and for each tool, the security estimate (on top) and the running time to get it (at the bottom).
The following architecture was used to run the estimations: ...

TODO: fill with the description of the machine used to run the estimations.

