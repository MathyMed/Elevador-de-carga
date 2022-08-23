from dataclasses import dataclass
from signal import raise_signal
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

b = 1 #in
d = 0.75 #in
D = 0.938 #In
r = 0.25 #In
a = 5 #in
l = 6 #in

#Aço SAE 1040
Sut = 80000 #psi

F = 500 #lb
R = 500 #lb
M = R*l - F*(l-a) #lb-in
print("M = ",M," lb*in")
I = (b*d**3)/12
print("I = ",I," in^4")
c = d/2 
sigma_a = M*c/I
print("sigma_a = ",sigma_a," psi")
#Pagina 372
D_d = D/d
r_d = r/d
#Pagina 216
#D_d_k = [3, 2, 1.3, 1.2, 1.1, 1.05, 1.01]
#A_k = [0.90720, 0.93232, 0.95880, 0.99590, 1.01650, 1.02260, 0.96689]
#b_k = [-0.33333, -0.30304, -0.27269, -0.23829, -0.21548, -0.19156, -0.15417]
#Ddk_inter = [2.5, 1.9, 1.5, 1.15, 1.07, 1.04]

D_d_k  = np.array([3, 2, 1.3, 1.2, 1.1, 1.05, 1.01])
A_k = np.array([0.90720, 0.93232, 0.95880, 0.99590, 1.01650, 1.02260, 0.96689])
plt.scatter(D_d_k ,A_k)
plt.plot(D_d_k ,A_k,'o--')
plt.show()

y_f = interpolate.interp1d(D_d_k ,A_k, 'linear')
x = np.linspace(3,1.01,100)
y = y_f(x)
plt.scatter(x,y)
plt.show()