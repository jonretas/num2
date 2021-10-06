# imports
import numpy as np

from AitkenNeville import AitkenNeville as aitken


#Aitken-Neville-Algorithmus
#Zum Auswerten an einer gewählten Stelle x0
x = [0,1,3]
y = [1,6,12]
x0 = 2
m = aitken(x, y, x0)

print("Interpolationswert an der Stelle x0 = "+ str(x0) +  ": y =  " + str(m))
