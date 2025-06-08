# Analysis of Algorithms I (MC458) - Test 3

- [Questions](./Enunciado.pdf)
- [Answers](./Resposta.pdf)
- [Turn in](./Entrega.pdf)

## Comparison and Sorting

If $C$ is a finite set of **distinct integers**, a *median element* of $C$ is an element $c \in C$ such that

$$
    \lvert \text{#}(C_{<}) - \text{#}(C_{>}) \rvert \le 1
$$

where $C_{<} = \lbrace x \in C \mid x < c \rbrace$, $C_{>} = \lbrace x \in C \mid x > c \rbrace$, and $\text{#}(C)$ denotes the cardinality of $C$.

---

### Question 1

Let $X$ and $Y$ be two **sorted** arrays, each with $n$ distinct integers, and suppose $X \cap Y = \varnothing$.
Design an algorithm whose **worst-case complexity**, in a comparison-based model, is $o(n)$ to find a median element of $X \cup Y$.
You **must** prove the correctness of your algorithm and give a complexity analysis.

---

### Question 2

With the same assumptions as in Question 1, determine-and prove-the best **lower bound** you can, in a comparison-based model, for finding a median element of $C = X \cup Y$.

*Observation.* You may assume that the output of any algorithm for this problem has the form $(\text{'X'}, i)$ or $(\text{'Y'}, i)$, indicating that a median element of $C$ is at position $i$ of array $X$ or $Y$, respectively.

---

### Question 3

Consider the following problem.

- **Input.** $k$ arrays $V_1, \dots, V_k$ of integers in the range $[1, n]$.
For each $i \in \{1,\dots,k\}$, array $V_i$ has size $n_i$.
Assume $k \in O(n)$ and $\sum_{i=1}^{k} n_i \in O(n)$.

- **Output.** The same $k$ arrays, each individually sorted.
*(The output is **not** a single merged array containing the $\sum_{i=1}^{k} n_i$ elements.)*

Design an algorithm-described in plain language, clearly and objectively-that solves the problem in **$O(n)$ time** while using **$O(n)$ total space**.
No computational model has been fixed; feel free to choose one.

- **Xitoró** proposes simply applying **HeapSort** to each of the $k$ arrays.
- **Chorãozinho** proposes simply applying **CountingSort** to each of the $k$ arrays.

**(a)** Explain why Xitoró's solution **does not** satisfy the requirements.

**(b)** Explain why Chorãozinho's solution **does not** satisfy the requirements.

**(c)** Propose a complete solution that **does** meet the requirements, and carefully justify its correctness as well as its time- and space-complexity bounds.
