# imports
import numpy as np
import matplotlib.pyplot as plt
from rosen import rosen as rosen
from Jrosen import Jrosen as Jrosen
from Hrosen import Hrosen as Hrosen



tol = 1e-10
maxit = 1500
x1 = np.linspace(-1.5, 1.5, 14)
x2 = np.linspace(-4, 2, 28)

[X, Y] = np.meshgrid(x1,  x2)

z = rosen(X,Y)

fig = plt.figure()
plt.contour(X, Y, z,np.logspace(-2, 3, 20))


#solve with Newton

#start value

x = np.array([1.5, 1.5])

plt.plot(x[0],x[1],'ro')

for k in range(1,maxit):

	#Jacobi-matrix 
	dy = Jrosen(x)
	
	#Hesse-matrix 
	dydy = Hrosen(x)
	
	#Newton Step
	s = np.linalg.solve(dydy,dy)

	#check tolerance
	if (np.linalg.norm(s)<tol):
		break
	#calc next iteration	
	x = x - s

	plt.plot(x[0],x[1],'*k')

plt.show()
print(k)
