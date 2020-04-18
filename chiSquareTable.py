
from scipy.integrate import quad
import numpy as np

print("****************************************************************")
print("Calculation of chi square value from given p value and DOF")
print("****************************************************************")

repeat = "y"
while repeat == "y":
    try:
        text = input("enter the P value   ")
        value = float(text)
    except ValueError:
        print("Error! This is not a number. Try again.")
    else:
        try:
            text = input("enter the degrees of freedom ")
            number = int(text) / 2
        except ValueError:
            print("Error! This is not a number. Try again.")
        else:
            gamma = np.math.gamma(number)
            constant = 1 / (pow(2, number) * gamma)
            r = 0
            for chi in np.arange(0, 90, 0.001):
                ProbabilityDensity = lambda x: constant * np.exp(-x / 2) * pow(x, number - 1)
                result, _ = quad(ProbabilityDensity, 0, chi)
                p = round(1 - float(result), 4)
                if p == value:
                    r = 1
                    print("the chi square value is ", chi)
                    break
            if r == 0:
                print("unable to find !!!! plz try again !!!!")

    repeat = input(" press y to continue / any key to exit ")

print("****************************************************************")
print("Calculation of P from given chi square value and DOF")
print("****************************************************************")
repeat = "y"
while repeat == "y":
    try:
        text = input("enter the chi square value   ")
        value = float(text)
    except ValueError:
        print("Error! This is not a number. Try again.")
    else:
        try:
            text = input("enter the degrees of freedom ")
            number = int(text) / 2
        except ValueError:
            print("Error! This is not a number. Try again.")
        else:
            gamma = np.math.gamma(number)

        constant = 1 / (pow(2, number) * gamma)

        ProbabilityDensity = lambda x: constant * np.exp(-x / 2) * pow(x, number - 1)
        result, _ = quad(ProbabilityDensity, 0, value)
        print("the P value is ", round(1 - float(result), 2))

    repeat = input(" press y to continue / any key to exit ")
