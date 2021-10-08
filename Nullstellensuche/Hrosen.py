def Hrosen(x):
	import numpy as np
	dydy =[[1200*pow(x[0],2) - 400*x[1] +2, -400*x[0]],
		  [-400*x[0],	200]]

	return dydy
