# flam-rd-assignment
Flam R&amp;D assignment — parametric curve fitting (θ, M, X)


This repository contains the solution for the **Flam R&D Assignment** on estimating unknown parameters in a given **parametric curve equation**.  
The task was to determine three parameters — **θ (theta)**, **M**, and **X** — such that the generated curve matches the given dataset as accurately as possible.

---

##  Problem Statement

The given parametric equations are:

\[
x = (t\cos(\theta) - e^{M|t|}\sin(0.3t)\sin(\theta) + X)
\]

\[
y = (42 + t\sin(\theta) + e^{M|t|}\sin(0.3t)\cos(\theta))
\]

Unknowns:  
\(\theta,\; M,\; X\)

Parameter ranges:  
\[
0° < \theta < 50° ,\; -0.05 < M < 0.05 ,\; 0 < X < 100
\]

and  
\[
6 < t < 60
\]

---

##  Approach

1. Imported the provided `(x, y)` points from `xy_data.csv`.
2. Used NumPy to model the same equations in Python.
3. Defined the objective as the mean **L1 distance** between predicted and actual points.
   \[
   L = \frac{1}{N}\sum_i(|x_i - \hat{x_i}| + |y_i - \hat{y_i}|)
   \]
   L1 loss was chosen for robustness against outliers.
4. Used `scipy.optimize.minimize` with proper bounds for each parameter.
5. Visualized actual vs. predicted curves and checked residuals for stability.

---

## Results

| Parameter | Symbol | Estimated Value |
|------------|----------|----------------|
| Rotation Angle | θ | 28.12° |
| Exponential Scaling | M | 0.02138 |
| X Translation | X | 54.90 |

---

##  Interpretation

- **θ** controls the orientation of the curve.  
- **M** introduces a small exponential modulation affecting oscillation amplitude.  
- **X** translates the curve horizontally.  

All parameters are within the valid range and produce a visually accurate fit.

---

##  Final Answer (for Submission)

Below is the final equation of the fitted curve.

### **LaTeX Form**

\[
\left(
t\cos(0.491) - e^{0.02138|t|}\sin(0.3t)\sin(0.491) + 54.90,\;
42 + t\sin(0.491) + e^{0.02138|t|}\sin(0.3t)\cos(0.491)
\right)
\]

### **Desmos Format (copy & paste directly)**

```
(t*cos(0.491) - e^(0.02138*abs(t))*sin(0.3*t)*sin(0.491) + 54.90,
 42 + t*sin(0.491) + e^(0.02138*abs(t))*sin(0.3*t)*cos(0.491))
```

**Domain:**
```
6 ≤ t ≤ 60
```

You can visualize this on [Desmos Calculator](https://www.desmos.com/calculator/rfj91yrxob).


