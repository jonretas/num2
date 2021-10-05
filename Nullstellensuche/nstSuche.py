# imports
import numpy as np
from Bisektionsmethode import Bisektionsmethode as bisec
from RegulaFalsi import RegulaFalsi as regula
from Sekantenmethode import Sekantenmethode as sekant
from NewtonSimple import NewtonSimple as newton

# vars
a = 0
b = 10
# f(x) = x^2 - 1
func = lambda x: pow(x, 2)-1
epsilon = 10e-7
# Df(x) = 2*x
Df = lambda x: 2*x
maxit = 10 ^ 7

# function calls
m = bisec(a, b, func, epsilon)
print("Bisektionsmethode \t\tNullstelle: m = " + str(m))

m = regula(a, b, func, epsilon)
print("RegulaFalsi \t\t\tNullstelle: m =  " + str(m))

m = sekant(a, b, func, epsilon)
print("Sekantenmethode \t\tNullstelle: m =  " + str(m))

# vars Newton numpy
# f(x) = x^2 - 1
f = np.array([1,0,-1])
# Df(x) = 2x -1
Df = np.array([2,0])

m = newton(b, f, Df, epsilon, maxit)[0]
nit = newton(b, f, Df, epsilon, maxit)[1]
print("Newton(simple)verfahren \tNullstelle: m =  " + str(m) +
        "\n\t\t\t\tIterationen: nit = " + str(nit))
