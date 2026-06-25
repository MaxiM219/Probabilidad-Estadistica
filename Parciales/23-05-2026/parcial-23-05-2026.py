import numpy as np
#import sympy as sy
#import matplotlib.pyplot as plt
from scipy.integrate import quad, dblquad
from scipy.optimize import brentq, minimize, minimize_scalar
from scipy.special import comb, factorial, gamma
import scipy.stats as sps

# EXAMEN
print('Ejercicio 1')
print('P(STa | Vi1, 3a2) = P(STa, Vi1, 3a2) / P(Vi1, 3a2)')
num = (0.40**3 * 0.60**2) * 3 #Vi (Ta Ta Vi) Ta
den = num + (0.40**2 * 0.60**3) * 3
p1 = num/den
print(f'{num:.5f}/{den:.5f} = {p1:.5f}')

print('')
print('Ejercicio 2')
print('Hacer dibujos, queda')
print('P(J+A<5) = 1/2 (un triángulo)')
print('P(J<A1, J+A<5)=7/16 (el triángulo menos una esquinita')
print('P(J<A1|J+A<5)=7/8=0.875')

print('')
print('Ejercicio 3')
er = 10
vr = 2
er2 = er**2+vr
ei = 8
vi = 4**2/12
ei2 = ei**2+vi
ei4 = (10**5 - 6**5)/(4*5)
ew = er * ei2
ew2 = er2 * ei4
vw = ew2 - ew**2
print(f'var(W) = {vw:.5f}')

print('')
print('Ejercicio 4')
print('filtrar, queda Veg: 2/7, Bur: 5/7. Segunda V entre 1er y 3er B')
pej4 = (2/7)**2*(5/7)*2 + (2/7)**2*(5/7)**2*3 
print(f'P(BVV U VBV U BBVV U BVBV U VBBV) = {pej4:.5f}') 

print('')
print('Ejercicio 5')
print('P(m-0.5 < Xprom < m+0.5) = 0.95, con Xprom ~ N(m, var/36)')
print('laburar, queda')
print('Phi(0.5 / (sigma/6)) = 0.975')
sigma = 0.5*6 / sps.norm.isf(0.025)
print(f'sigma = {sigma:.5f}')