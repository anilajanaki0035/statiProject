import inline as inline
import matplotlib
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

x = np.linspace(-4, 4, num=100)
constant = 1.0 / np.sqrt(2 * np.pi)
pdf_normal_distribution = constant * np.exp((-x ** 2) / 2.0)
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, pdf_normal_distribution)
ax.set_ylim(0)
ax.set_title('Normal Distribution', size=20)
ax.set_ylabel('Probability Density', size=20)
plt.show()


def normalProbabilityDensity(x):
    constant = 1.0 / np.sqrt(2 * np.pi)
    return (constant * np.exp((-x ** 2) / 2.0))

repeat = "y"
while repeat == "y":
    try:
        text = input("enter the value z0 to calculate the P(z<z0) ")
        number = float(text)
    except ValueError:
        print("Error! This is not a number. Try again.")
    else:
        result, _ = quad(normalProbabilityDensity, np.NINF, number)
        print(result)

    repeat = input(" press y to continue / any key to exit ")
