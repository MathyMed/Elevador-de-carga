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
sigma_a_nom = M*c/I
print("sigma_a_nom = ",sigma_a_nom," psi")
#Pagina 372
D_d = D/d
r_d = r/d
#Pagina 216
D_d_k  = np.array([3, 2, 1.3, 1.2, 1.1, 1.05])
A_k = np.array([0.90720, 0.93232, 0.95880, 0.99590, 1.01650, 1.02260])
b_k = [-0.33333, -0.30304, -0.27269, -0.23829, -0.21548, -0.19156]
Ak_interp = interpolate.interp1d(D_d_k ,A_k, 'linear')
bk_interp = interpolate.interp1d(D_d_k ,b_k, 'linear')
x = D/d
ya = Ak_interp(x)
yb = bk_interp(x)
print("A = ",ya)
print("b = ",yb)
Kt = ya*(r/d)**yb
print("Kt = ",Kt)

Sut_q = [50, 55, 60, 70, 80, 90, 100, 110, 120, 130, 140, 160, 180, 200, 220, 240]
raiz_a = [0.130, 0.118, 0.108, 0.093, 0.080, 0.070, 0.062, 0.055, 0.049, 0.044, 0.039, 0.031, 0.024, 0.018, 0.013, 0.009]
raiza_interp = interpolate.interp1d(Sut_q, raiz_a, 'linear')
x2 = Sut/1000
y2 = raiza_interp(x2)
print("raiz_a = ",y2)
q = 1/(1+(y2/np.sqrt(r)))
print("q = ",q)

Kf = 1 + q*(Kt - 1)
print("Kf = ",Kf)
sigma_a = Kf*sigma_a_nom
print("sigma_a = ",sigma_a)
sigma_x = sigma_a
sigma_y = 0
tau_xy = 0
tau_ab = np.sqrt(((sigma_x+sigma_y)/2)**2 + tau_xy**2)
print("tau_ab = ",tau_ab)
sigma1_a = (sigma_x+sigma_y)/2 + tau_ab
sigma2_a = 0
sigma3_a = (sigma_x+sigma_y)/2 - tau_ab
sigma_vm = np.sqrt(sigma1_a**2 - sigma1_a*sigma2_a + sigma2_a**2)
print("sigma_vm = ",sigma_vm)

Se = 0.5*Sut
A95 = 0.05*d*b
d_equi = np.sqrt(A95/0.0766)
if d < 0.3:
    C_tamanho = 1
if d > 0.3 and d < 10:
    C_tamanho = 0.869*(d_equi)**(-0.097)
print(C_tamanho)
