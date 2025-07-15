import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv('ML\Study_vs_Score_data.csv')

# Check the data
print(df.head())

# Extract variables
x = df['Attendance_Hours'].values
y = df['Final_Marks'].values

# Compute means
mean_x = np.mean(x)
mean_y = np.mean(y)
n = len(x)

# Calculate slope (b1) and intercept (b0)
numer = 0
denom = 0
for i in range(n):
    numer += (x[i] - mean_x) * (y[i] - mean_y)
    denom += (x[i] - mean_x) ** 2
b1 = numer / denom
b0 = mean_y - (b1 * mean_x)

print(f"b1 (slope): {b1}")
print(f"b0 (intercept): {b0}")

# Generate regression line values
x_line = np.linspace(min(x), max(x), 1000)
y_line = b0 + b1 * x_line

# Plot
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='#ef5423', label='Scatter Plot')
plt.plot(x_line, y_line, color='#58b970', label='Regression Line')
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.title('Linear Regression: Hours Studied vs Score')
plt.legend()
plt.grid(True)
plt.show()

#calculate R-Squared to know model accuracy
ss_t = 0
ss_r = 0
for i in range(n):
    y_pred = b0 + b1 * x[i]
    ss_t += (y[i] - mean_y) ** 2
    ss_r += (y[i] - y_pred) ** 2
r2 = 1 - (ss_r/ss_t)
print(r2)

