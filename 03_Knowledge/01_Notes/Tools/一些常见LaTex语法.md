#### 上下标

- **上标**：使用 `^`
    - 语法：`x^2`
- **下标**：使用 `_`
    - 语法：`x_1`
- **多字符**：如果上标或下标包含多个字符，请用花括号 `{}` 包裹。
    - 语法：`x^{10}`
#### 分数

- 使用 `\frac{分子}{分母}`
    - 语法：`\frac{1}{2}` 

#### 根号

- 使用 `\sqrt{}`
    - 语法：`\sqrt{x}`
    - n次根号：`\sqrt[n]{x}`

#### 运算符号
| 运算类型      | LaTeX 语法                   | 渲染效果       |
| :-------- | :------------------------- | :--------- |
| 加减乘除      | `+`, `-`, `\times`, `\div` | +, −, ×, ÷ |
| 点乘        | `\cdot`                    | ⋅          |
| 不等于       | `\neq`                     | ≠          |
| 大于等于/小于等于 | `\geq`, `\leq`             | ≥ , ≤      |
| 正负号       | `\pm`                      | ±          |
#### 希腊字母

直接使用反斜杠加字母名称。

| 英文名称        | 小写符号  | 小写代码                       | 大写符号 | 大写代码         |
| ----------- | ----- | -------------------------- | ---- | ------------ |
| **Alpha**   | α     | `\alpha`                   | A    | `A` (直接用英文A) |
| **Beta**    | β     | `\beta`                    | B    | `B`          |
| **Gamma**   | γ     | `\gamma`                   | Γ    | `\Gamma`     |
| **Delta**   | δ     | `\delta`                   | Δ    | `\Delta`     |
| **Epsilon** | ε / ϵ | `\varepsilon` / `\epsilon` | E    | `E`          |
| **Zeta**    | ζ     | `\zeta`                    | Z    | `Z`          |
| **Eta**     | η     | `\eta`                     | H    | `H`          |
| **Theta**   | θ / ϑ | `\theta` / `\vartheta`     | Θ    | `\Theta`     |
| **Iota**    | ι     | `\iota`                    | I    | `I`          |
| **Kappa**   | κ / ϰ | `\kappa` / `\varkappa`     | K    | `K`          |
| **Lambda**  | λ     | `\lambda`                  | Λ    | `\Lambda`    |
| **Mu**      | μ     | `\mu`                      | M    | `M`          |
| **Nu**      | ν     | `\nu`                      | N    | `N`          |
| **Xi**      | ξ     | `\xi`                      | Ξ    | `\Xi`        |
| **Omicron** | ο     | `o` (直接用英文o)               | O    | `O`          |
| **Pi**      | π / ϖ | `\pi` / `\varpi`           | Π    | `\Pi`        |
| **Rho**     | ρ / ϱ | `\rho` / `\varrho`         | P    | `P`          |
| **Sigma**   | σ / ς | `\sigma` / `\varsigma`     | Σ    | `\Sigma`     |
| **Tau**     | τ     | `\tau`                     | T    | `T`          |
| **Upsilon** | υ     | `\upsilon`                 | Υ    | `\Upsilon`   |
| **Phi**     | φ / ϕ | `\varphi` / `\phi`         | Φ    | `\Phi`       |
| **Chi**     | χ     | `\chi`                     | X    | `X`          |
| **Psi**     | ψ     | `\psi`                     | Ψ    | `\Psi`       |
| **Omega**   | ω     | `\omega`                   | Ω    | `\Omega`     |

#### 求和与积分

- **求和**：使用 `\sum`
    - 语法：`\sum_{i=1}^{n} i` （i从1到n对i求和）
- **积分**：使用 `\int`
    - 语法：`\int_{a}^{b} f(x) dx` （从a到b对函数f(x)积分）

#### 括号

普通括号 `()` 大小固定。若需括号随内容自动调整大小，请使用 `\left(` 和 `\right)`。    
- `\left( \frac{a}{b} \right)`

#### 三角函数
| 函数名称 | LaTeX 语法 | 渲染效果 |
| :--- | :------- | :--- |
| 正弦   | `\sin`   | sin  |
| 余弦   | `\cos`   | cos  |
| 正切   | `\tan`   | tan  |
| 余切   | `\cot`   | cot  |
| 正割   | `\sec`   | sec  |
| 余割   | `\csc`   | csc  |

**角度与符号**
**角度符号 (°)**：使用 `^\circ`
**角度符号 (∠)**：使用 `\angle`

#### 换行等于
```LaTex
\begin{align}
  f(x) &= (x+1)^2 + 2x \nonumber \\  % \nonumber 表示该行不编号
       &= x^2 + 2x + 1 + 2x \nonumber \\
       &= x^2 + 4x + 1
\end{align}
```
