### 复数乘法推导与几何意义

#### 代数推导过程

**步骤 1**：设定复数乘积
$$
\begin{aligned}
z_1 \cdot z_2 &= [r_1(\cos \theta_1 + i \sin \theta_1)] \cdot [r_2(\cos \theta_2 + i \sin \theta_2)] \\
&= r_1 r_2 (\cos \theta_1 + i \sin \theta_1)(\cos \theta_2 + i \sin \theta_2)
\end{aligned}
$$

**步骤 2**：展开括号（分配律）
$$
\begin{aligned}
(\cos \theta_1 + i \sin \theta_1)(\cos \theta_2 + i \sin \theta_2) &= \cos \theta_1 \cos \theta_2 + i \cos \theta_1 \sin \theta_2 \\
&\quad + i \sin \theta_1 \cos \theta_2 + i^2 \sin \theta_1 \sin \theta_2
\end{aligned}
$$

**步骤 3**：使用 $i^2 = -1$
$$
= \cos \theta_1 \cos \theta_2 + i \cos \theta_1 \sin \theta_2 + i \sin \theta_1 \cos \theta_2 - \sin \theta_1 \sin \theta_2
$$

**步骤 4**：整理实部和虚部
$$
= (\cos \theta_1 \cos \theta_2 - \sin \theta_1 \sin \theta_2) + i(\cos \theta_1 \sin \theta_2 + \sin \theta_1 \cos \theta_2)
$$

**步骤 5**：使用三角和角公式
回忆三角恒等式：
- $\cos(A + B) = \cos A \cos B - \sin A \sin B$
- $\sin(A + B) = \sin A \cos B + \cos A \sin B$

所以：
$$
= \cos(\theta_1 + \theta_2) + i \sin(\theta_1 + \theta_2)
$$

**步骤 6**：代回原式
$$
z_1 \cdot z_2 = r_1 r_2 [\cos(\theta_1 + \theta_2) + i \sin(\theta_1 + \theta_2)] \quad \blacksquare
$$

#### 几何意义总结

> **复数乘法 = 模长相乘 + 角度相加**
> - **模长**：新复数的模长 = 原来两个模长的**乘积**
> - **角度**：新复数的角度 = 原来两个角度的**和**

**几何操作**：
1. **缩放**：长度放大 $r_2$ 倍
2. **旋转**：逆时针旋转 $\theta_2$ 角度

#### 简单例子

**例 2**：计算 $(\cos\frac{\pi}{6} + i \sin\frac{\pi}{6}) \cdot (\cos\frac{\pi}{3} + i \sin\frac{\pi}{3})$

- **第一个复数**：角度 = $\frac{\pi}{6}$（30°），模长 = 1
- **第二个复数**：角度 = $\frac{\pi}{3}$（60°），模长 = 1

**乘积**：
- **模长**：$1 \times 1 = 1$
- **角度**：$\frac{\pi}{6} + \frac{\pi}{3} = \frac{\pi}{2}$（90°）

所以：
$$
(\cos\frac{\pi}{6} + i \sin\frac{\pi}{6}) \cdot (\cos\frac{\pi}{3} + i \sin\frac{\pi}{3}) = \cos\frac{\pi}{2} + i \sin\frac{\pi}{2} = i
$$

---

### 数学归纳法详解

#### 直觉解释
数学归纳法用于证明：**"对所有正整数 n，命题 P(n) 都成立"**

**多米诺骨牌类比**：
1. 推倒第一块骨牌（基础步骤）
2. 证明：如果第 k 块倒下，第 k+1 块也会倒下（归纳步骤）

如果这两步都做到了，那么**所有**骨牌都会倒下！

#### 标准步骤
1. **步骤 1 - 基础步骤**：证明 $P(1)$ 成立
2. **步骤 2 - 归纳假设**：假设 $P(k)$ 对某个正整数 $k$ 成立
3. **步骤 3 - 归纳步骤**：在归纳假设的前提下，证明 $P(k+1)$ 也成立

**结论**：由数学归纳法原理，$P(n)$ 对所有正整数 $n$ 成立。

#### 简单例子
**例 3**：证明 $1 + 2 + 3 + \cdots + n = \frac{n(n+1)}{2}$

- **步骤 1 - 基础步骤**（$n=1$）：
    - 左边：$1$
    - 右边：$\frac{1 \cdot 2}{2} = 1$
    - 左边 = 右边 ✓

- **步骤 2 - 归纳假设**：
    假设 $n=k$ 时命题成立，即：
    $$1 + 2 + 3 + \cdots + k = \frac{k(k+1)}{2}$$

- **步骤 3 - 归纳步骤**：
    要证明 $n=k+1$ 时也成立，即要证：
    $$1 + 2 + 3 + \cdots + k + (k+1) = \frac{(k+1)(k+2)}{2}$$

    **证明**：
    $$
    \begin{aligned}
    \text{左边} &= \underbrace{(1 + 2 + \cdots + k)}_{\text{用归纳假设}} + (k+1) \\
    &= \frac{k(k+1)}{2} + (k+1) \\
    &= \frac{k(k+1)}{2} + \frac{2(k+1)}{2} \\
    &= \frac{k(k+1) + 2(k+1)}{2} \\
    &= \frac{(k+1)(k + 2)}{2} \\
    &= \text{右边} \quad \blacksquare
    \end{aligned}
    $$

---

### 小结：现在你知道了什么？

| 概念 | 核心要点 | 对 De Moivre 定理的作用 |
| :--- | :--- | :--- |
| **复数极式** | $z = r(\cos \theta + i \sin \theta)$ | 定理的研究对象 |
| **复数乘法** | 模长相乘，**角度相加** | 定理成立的根本原因 |
| **数学归纳法** | 基础步骤 + 归纳步骤 | 证明定理对所有 n 成立 |

**关键洞察**：
- $\cos \theta + i \sin \theta$ 是单位圆上的复数（模长=1）
- 自乘 2 次：角度相加 2 次 → $2\theta$
- 自乘 3 次：角度相加 3 次 → $3\theta$
- ...
- 自乘 n 次：角度相加 n 次 → $n\theta$

这就是 De Moivre 定理！

---

### 严谨推导（De Moivre 定理的证明）

现在我们来用**数学归纳法**完整证明 De Moivre 定理。

#### 定理陈述
**De Moivre 定理**：对任意实数 $\theta$ 和任意正整数 $n$，有：
$$(\cos \theta + i \sin \theta)^n = \cos(n\theta) + i \sin(n\theta)$$

#### 证明过程

**步骤 1 - 基础步骤（$n = 1$）**
**要证**：$(\cos \theta + i \sin \theta)^1 = \cos(1 \cdot \theta) + i \sin(1 \cdot \theta)$

**证明**：
$$
\begin{aligned}
\text{左边} &= (\cos \theta + i \sin \theta)^1 \\
&= \cos \theta + i \sin \theta \\
&= \cos(1 \cdot \theta) + i \sin(1 \cdot \theta) \\
&= \text{右边} \quad \checkmark
\end{aligned}
$$
基础步骤成立。

**步骤 2 - 归纳假设**
**假设**：当 $n = k$（$k$ 为某个正整数）时定理成立，即：
$$(\cos \theta + i \sin \theta)^k = \cos(k\theta) + i \sin(k\theta)$$
这个假设会在步骤 3 中使用。

**步骤 3 - 归纳步骤（证明 $n = k+1$ 时成立）**
**要证**：$(\cos \theta + i \sin \theta)^{k+1} = \cos((k+1)\theta) + i \sin((k+1)\theta)$

**证明**：
**左边**：
$$
\begin{aligned}
(\cos \theta + i \sin \theta)^{k+1} &= (\cos \theta + i \sin \theta)^k \cdot (\cos \theta + i \sin \theta)^1 \\
\end{aligned}
$$
使用**归纳假设**（替换 $(\cos \theta + i \sin \theta)^k$）：
$$
\begin{aligned}
&= [\cos(k\theta) + i \sin(k\theta)] \cdot (\cos \theta + i \sin \theta)
\end{aligned}
$$
现在使用**复数乘法法则**（模长相乘，角度相加）：
- 第一个复数：模长 = 1，角度 = $k\theta$
- 第二个复数：模长 = 1，角度 = $\theta$

所以乘积为：
$$
\begin{aligned}
&= 1 \cdot 1 \cdot [\cos(k\theta + \theta) + i \sin(k\theta + \theta)] \\
&= \cos((k+1)\theta) + i \sin((k+1)\theta) \\
&= \text{右边} \quad \checkmark
\end{aligned}
$$

**详细展开版**（代数运算）：
$$
\begin{aligned}
&[\cos(k\theta) + i \sin(k\theta)] \cdot (\cos \theta + i \sin \theta) \\
&= \cos(k\theta)\cos\theta + i\cos(k\theta)\sin\theta + i\sin(k\theta)\cos\theta + i^2\sin(k\theta)\sin\theta \\
&= \cos(k\theta)\cos\theta + i\cos(k\theta)\sin\theta + i\sin(k\theta)\cos\theta - \sin(k\theta)\sin\theta \\
&= [\cos(k\theta)\cos\theta - \sin(k\theta)\sin\theta] + i[\cos(k\theta)\sin\theta + \sin(k\theta)\cos\theta]
\end{aligned}
$$
使用和角公式（令 $A = k\theta, B = \theta$）：
$$
\begin{aligned}
&= \cos(k\theta + \theta) + i \sin(k\theta + \theta) \\
&= \cos((k+1)\theta) + i \sin((k+1)\theta) \quad \blacksquare
\end{aligned}
$$

#### 结论
由数学归纳法原理：
1. 基础步骤（$n=1$）成立 ✓
2. 归纳步骤：若 $n=k$ 成立，则 $n=k+1$ 也成立 ✓

因此，**De Moivre 定理对所有正整数 $n$ 都成立**！

---

### 思考问题

在继续之前，我想问你：

> **问题**：我们刚才证明了定理对**正整数** $n$ 成立。那么：
> 1. 如果 $n = 0$，定理会是什么形式？成立吗？
> 2. 如果 $n$ 是**负整数**（如 $n = -1, -2$），定理还成立吗？

你可以先想一想，或者我直接继续讲解负整数的情况？