import numpy as np
import matplotlib.pyplot as plt

# Define the function y = (x + 3)^2
def func(x):
    return (x + 3)**2

# Define the derivative of the function
def gradient(x):
    return 2 * (x + 3)

# Gradient Descent Algorithm
def gradient_descent(initial_x, learning_rate, epochs):
    x_values = [initial_x]
    y_values = [func(initial_x)]

    for epoch in range(epochs):
        current_x = x_values[-1]
        new_x = current_x - learning_rate * gradient(current_x)

        x_values.append(new_x)
        y_values.append(func(new_x))

    return x_values, y_values

# Initial parameters
initial_x = 2
learning_rate = 0.1
epochs = 50

# Run gradient descent
x_values, y_values = gradient_descent(initial_x, learning_rate, epochs)

# Plot the function and the path of gradient descent
x_range = np.linspace(-10, 5, 100)
plt.plot(x_range, func(x_range), label='y = (x + 3)^2')
plt.scatter(x_values, y_values, color='red', label='Gradient Descent Path')
plt.title('Gradient Descent for y = (x + 3)^2')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
