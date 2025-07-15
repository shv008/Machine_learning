# 📘 Linear Regression Model Explanation

This document explains the math and logic behind the **Linear Regression** model used in the `Study_vs_Score` project, where we predict students' final marks based on hours studied.

---

## 🔍 Problem Statement

> Given a dataset of students' **Attendance/Study Hours** and their **Final Marks**, predict how well a student will score based on how many hours they studied.

---

## 🧠 What is Linear Regression?

Linear Regression is a **supervised learning algorithm** used for predicting continuous values. It fits a straight line (called the **regression line**) to model the relationship between an independent variable `x` (Hours Studied) and a dependent variable `y` (Final Marks).

### 📈 Equation of the Line:

\[
y = b_0 + b_1 \cdot x
\]

Where:
- \( b_0 \) = Intercept
- \( b_1 \) = Slope (coefficient)
- \( x \) = Hours studied
- \( y \) = Predicted score

---

## 🧮 How the Model Was Built (Without scikit-learn)

1. **Calculate Mean** of `x` and `y`
2. **Compute Slope (b1)**:

\[
b_1 = \frac{\sum (x_i - \bar{x})(y_i - \bar{y})}{\sum (x_i - \bar{x})^2}
\]

3. **Compute Intercept (b0)**:

\[
b_0 = \bar{y} - b_1 \cdot \bar{x}
\]

4. **Generate Predictions** using the formula:
\[
y = b_0 + b_1 \cdot x
\]

---

## ✅ Model Evaluation: R² Score

To measure how well the regression line fits the data, we use **R-squared**:

\[
R^2 = 1 - \frac{SS_{\text{res}}}{SS_{\text{tot}}}
\]

- \( SS_{\text{tot}} \): Total sum of squares
- \( SS_{\text{res}} \): Residual sum of squares

An R² value close to `1` indicates a strong fit.

---

## 📊 Visualization

The plot includes:
- **Scatter plot** of actual data points
- **Regression line** showing predicted trend
- **Grid & legend** for clarity

---

## 🧾 Summary

- 🔹 Simple Linear Regression manually implemented
- 🔹 No ML libraries used
- 🔹 Predicted final marks based on study hours
- 🔹 Interpretable and beginner-friendly

---

> This project lays the foundation for understanding core ML concepts and will be expanded with more models soon.
