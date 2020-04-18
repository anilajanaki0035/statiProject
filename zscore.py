
from scipy.integrate import quad
import numpy as np


def normalProbabilityDensity(x):
    constant = 1.0 / np.sqrt(2 * np.pi)
    return (constant * np.exp((-x ** 2) / 2.0))
print("*********************************************")
print(" Calculation of P(z<z0) for given z0 ")
print("*********************************************")
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

repeatAlpha = "y"
print("****************************************************************")
print("Calculation of z0 for given alpha such that P(z<z0)=alpha")
print("****************************************************************")
while repeatAlpha == "y":
    try:
        text = input("enter the value alpha to calculate the  z0 such that P(z<z0)=alpha ")
        number = float(text)
    except ValueError:
        print("Error! This is not a number. Try again.")
    else:
        r = 0
        for z in np.arange(-3.49, 3.5, 0.01):
            result, _ = quad(normalProbabilityDensity, np.NINF, z)
            if round(float(result), 4) == round(number, 4):
                print("the calculated z value is")
                print(z)
                r = 1
                break

        if r == 0:
            print("Sorry !!!! unable to find , try a different value")

    repeatAlpha = input(" press y to continue / any key to exit ")
