
# R&D / AI Assignment - Parametric Curve Fitting
# Name: Anushree K C

import pandas as pd
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# load data
data = pd.read_csv("xy_data.csv")

# parametric equation for x and y
def curve(params, t):
    theta, M, X = params
    x = t * np.cos(theta) - np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.sin(theta) + X
    y = 42 + t * np.sin(theta) + np.exp(M * np.abs(t)) * np.sin(0.3 * t) * np.cos(theta)
    return x, y

# loss function (L1 distance)
def objective(params, t_data, x_data, y_data):
    x_pred, y_pred = curve(params, t_data)
    return np.mean(np.abs(x_data - x_pred) + np.abs(y_data - y_pred))

# range for t
t_values = np.linspace(6, 60, len(data))

# initial guess for parameters
initial_guess = [np.deg2rad(25), 0, 50]

# bounds for (theta, M, X)
bounds = [(np.deg2rad(0.1), np.deg2rad(50)), (-0.05, 0.05), (0, 100)]

# run optimization
result = minimize(objective, initial_guess, args=(t_values, data['x'].values, data['y'].values), bounds=bounds)

# get results
theta, M, X = result.x

print("Estimated values:")
print("theta (deg):", np.rad2deg(theta))
print("M:", M)
print("X:", X)

# predicted curve
x_pred, y_pred = curve(result.x, t_values)

# plot actual vs predicted
plt.scatter(data['x'], data['y'], label='Actual', color='blue', s=20)
plt.plot(x_pred, y_pred, label='Predicted', color='red')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Curve Fitting')
plt.grid(True)
plt.show()
