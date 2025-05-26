# 📊 FHE Security Parameter Tables

some introduction....

## 🧭 Table of Contents

- 🧠 [Table Notes/Terms](#-notes)
- 🔐 [Security Level: 128 bits](#-security-level-128-bits)
- 🔐 [Security Level: 192 bits](#-security-level-192-bits)
- 🔐 [Security Level: 256 bits](#-security-level-256-bits)
> 📎 **Note**: Tables generated using the official script from [gong-cr/FHE-Security-Guidelines](https://github.com/gong-cr/FHE-Security-Guidelines)
---

## 🧠 Notes and Terms
In our tables, we use the following terms used in each column for clarity:
- **Ternary**: Secrets sampled from the set `{−1, 0, 1}`.
- **Gaussian**: Secrets sampled from a discrete Gaussian distribution.
- **Classical**: Adversary uses classical algorithms.
- **Quantum**: Adversary has access to quantum resources.
---


## 🔐 Security Level: 128 bits



#### 🎯 **Threshold:** 128 bits  **Margin:** 0

|   **_n_**    | **Classical Ternary** | **Classical Gaussian** | **Quantum Ternary** | **Quantum Gaussian** |
|:----------:|:---------------------:|:----------------------:|:-------------------:|:--------------------:|
|   1024     |          26           |           28           |         20          |         22           |
|   2048     |          53           |           55           |         40          |         42           |
|   4096     |         106           |          108           |         80          |         83           |
|   8192     |         214           |          216           |        161          |        163           |

> 🚧 *More values for `n` will be added soon.*
---

## 🔐 Security Level: 192 bits


#### 🎯 **Threshold:** 192 bits  **Margin:** 0
| **_n_** | **Classical Ternary** | **Classical Gaussian** | **Quantum Ternary** | **Quantum Gaussian** |
|:-------:|:---------------------:|:----------------------:|:-------------------:|:--------------------:|
|  2048   |          36           |           38           |         29          |         31           |
|  4096   |          73           |           75           |         59          |         61           |
|  8192   |         147           |          149           |        119          |        122           |

> 🚧 *More values for `n` will be added soon.*


---

## 🔐 Security Level: 256 bits

#### 🎯 **Threshold:** 256 bits  **Margin:** 0
| **_n_** | **Classical Ternary** | **Classical Gaussian** | **Quantum Ternary** | **Quantum Gaussian** |
|:-------:|:---------------------:|:----------------------:|:-------------------:|:--------------------:|
|  2048   |          27           |           30           |         22          |         25           |
|  4096   |          56           |           58           |         47          |         49           |
|  8192   |         114           |          116           |         95          |         98           |
> 🚧 *More values for `n` will be added soon.*






