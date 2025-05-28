# 📊 FHE Security Parameter Tables

Introduction ....

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

|        **_n_**        | **Classical Ternary** | **Classical Gaussian** | **Quantum Ternary** | **Quantum Gaussian** |
|:---------------------:|:---------------------:|:----------------------:|:-------------------:|:--------------------:|
|    2<sup>10</sup>     |          26           |           28           |         20          |          22          |
|    2<sup>11</sup>     |          53           |           55           |         40          |          42          |
|    2<sup>12</sup>     |          106          |          108           |         80          |          83          |
|    2<sup>13</sup>     |          214          |          216           |         161         |         163          |
|    2<sup>14</sup>     |          430          |          432           |         322         |         324          |
|    2<sup>15</sup>     |          868          |          870           |         644         |         646          |
|    2<sup>16</sup>     |         1747          |          1749          |        1289         |         1291         |
|    2<sup>17</sup>     |         3523          |          3525          |        2578         |         2580         |
---




## 🔐 Security Level: 192 bits
#### 🎯 **Threshold:** 192 bits  **Margin:** 0

|        **_n_**        | **Classical Ternary** | **Classical Gaussian** | **Quantum Ternary** | **Quantum Gaussian** |
|:---------------------:|:---------------------:|:----------------------:|:-------------------:|:--------------------:|
|    2<sup>11</sup>     |          36           |           38           |         29          |          31          |
|    2<sup>12</sup>     |          73           |           75           |         59          |          61          |
|    2<sup>13</sup>     |          147          |          149           |         119         |         122          |
|    2<sup>14</sup>     |          297          |          299           |         239         |         242          |
|    2<sup>15</sup>     |          597          |          599           |         479         |         482          |
|    2<sup>16</sup>     |         1199          |          1201          |         959         |         962          |
|    2<sup>17</sup>     |         2411          |          2413          |        1920         |         1922         |

---

## 🔐 Security Level: 256 bits
#### 🎯 **Threshold:** 256 bits  **Margin:** 0

|        **_n_**        | **Classical Ternary** | **Classical Gaussian** | **Quantum Ternary** | **Quantum Gaussian** |
|:---------------------:|:---------------------:|:----------------------:|:-------------------:|:--------------------:|
|    2<sup>11</sup>     |          27           |           30           |         22          |          25          |
|    2<sup>12</sup>     |          56           |           58           |         47          |          49          |
|    2<sup>13</sup>     |          114          |          116           |         95          |          98          |
|    2<sup>14</sup>     |          230          |          232           |         192         |         195          |
|    2<sup>15</sup>     |          462          |          464           |         385         |         388          |
|    2<sup>16</sup>     |          929          |          931           |         773         |         775          |

> 🚧 *More values for `n` will be added soon.*
