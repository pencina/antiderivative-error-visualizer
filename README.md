# 🧮 Antiderivative Error Visualizer

This interactive Python tool demonstrates how **algebraically equivalent** antiderivatives can behave **numerically different**—especially under floating-point arithmetic. It compares two forms of the integral:

\[
\int x \sqrt{a x + b} \, dx
\]

## 📘 Antiderivative Forms

Let \( a, b \in \mathbb{R} \). Two common forms of the antiderivative are:

**Stable Form (F₁):**
\[
F_1(x) = \frac{2}{45a^2}(a x + b)^{5/2} - \frac{2b}{27a^2}(a x + b)^{3/2}
\]

**Unstable Form (F₂):**
\[
F_2(x) = \frac{2}{3a}x(a x + b)^{3/2} - \frac{4}{15a^2}(a x + b)^{5/2}
\]

Although \( F_1'(x) = F_2'(x) = x\sqrt{a x + b} \), their **numerical stability differs greatly** at extreme values of \( x \), especially when large terms cancel in \( F_2 \).

## 🔬 What This Tool Shows

- Plots both \( F_1(x) \), \( F_2(x) \), and a high-precision numerical integral as reference
- Shows absolute error for each expression:  
  \[
  E_i(x) = \left| F_i(x) - I_{\text{ref}}(x) \right|
  \]
- Allows dynamic adjustment of parameters `a` and `b`

## 💻 Usage

### 🐍 Requirements

- Python 3.8+
- `matplotlib`
- `scipy`
- `numpy`
- `tkinter` (included by default in most Python distributions)

### ▶️ Running the App

```bash
python interactive_plot.py
A GUI will open where you can slide a and b values and observe how the error evolves in real time.
📜 License

MIT License
📘 References

    N. J. Higham, Accuracy and Stability of Numerical Algorithms

    W. Rudin, Principles of Mathematical Analysis

    P. C. Encina, Numerical and Asymptotic Consequences of Rewriting Antiderivatives
