import inline as inline
import matplotlib
from scipy.integrate import quad
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

repeat = "y"
while repeat == "y":
    try:
        text = input("enter the t value  to calculate  P   ")
        value = float(text)
    except ValueError:
        print("Error! This is not a number. Try again.")
    else:
        try:
            text = input("enter the degrees of freedom ")
            dof = int(text)
        except ValueError:
            print("Error! This is not a number. Try again.")
        else:
            gammaUp = np.math.gamma((dof + 1) / 2)
            gammaL = np.math.gamma(dof / 2)

        constant = gammaUp / (np.sqrt(dof * np.pi) * gammaL)

        ProbabilityDensity = lambda x: constant * 1 / (pow((x * x / dof) + 1, (dof + 1) / 2))
        result, _ = quad(ProbabilityDensity, np.NINF, value)
        print("the P value is ", round(1 - float(result), 3))

    repeat = input(" press y to continue / any key to exit ")

print("******************* calculate the chi square value from given p value and DOF***************")

repeat = "y"
while repeat == "y":
    try:
        text = input("enter the P value  to calculate  t value   ")
        value = float(text)
    except ValueError:
        print("Error! This is not a number. Try again.")
    else:
        try:
            text = input("enter the degrees of freedom ")
            dof = int(text)
        except ValueError:
            print("Error! This is not a number. Try again.")
        else:
            gammaUp = np.math.gamma((dof + 1) / 2)
            gammaL = np.math.gamma(dof / 2)
            constant = gammaUp / (np.sqrt(dof * np.pi) * gammaL)
            r = 0
            if dof == 1:
                for t in np.arange(0, 640, 0.001):
                    ProbabilityDensity = lambda x: constant * 1 / (pow((x * x / dof) + 1, (dof + 1) / 2))
                    result, _ = quad(ProbabilityDensity, np.NINF, t)
                    p = round(1 - float(result), 4)
                    if p == value:
                        r = 1
                        print("the t value is ", t)
                        break
            else:
                for t in np.arange(0, 32, 0.001):
                    ProbabilityDensity = lambda x: constant * 1 / (pow((x * x / dof) + 1, (dof + 1) / 2))
                    result, _ = quad(ProbabilityDensity, np.NINF, t)
                    p = round(1 - float(result), 4)
                    if p == value:
                        r = 1
                        print("the t value is ", t)
                        break
            if r == 0:
                print("unable to find !!!! plz try again !!!!")

    repeat = input(" press y to continue / any key to exit ")
