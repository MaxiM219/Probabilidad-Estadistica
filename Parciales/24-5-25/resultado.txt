import numpy as np
#import sympy as sy
#import matplotlib.pyplot as plt
from scipy.integrate import quad, dblquad
#from scipy.optimize import brentq
#from scipy.special import comb, factorial, gamma
import scipy.stats as sps

# EXAMEN
print('Ejercicio 1')
print('M2: hubo segunda extraccion y salen las dos del mismo')
pM = (5*4 + 0 + 3*2) / (9*8)
pm2bv = (4*3 + 3*2) / (7*6)
pbv = 5*1*2/(9*8)
pva = 1*3*2/(9*8)
pab = 3*5*2/(9*8)
pm2 = (4*3 + 3*2) / (7*6) * pbv + (5*4 + 2*1) / (7*6) * pva + (4*3 + 2*1) / (7*6) * pab
num = pm2bv*pbv
den = pm2
pej1 = num/den
print(f'P(BV|M2) = P(M2|BV) * P(BV) / P(M2) = {num:.3f}/{den:.3f} = {pej1:.5f}')


print('')
print('Ejercicio 2')
print('Y|X=x es Gamma (2, 1/x^2), X es U(2, 4)')
print('E[Y|X=3] = 2*9 = 18')
print(f'P(2X^2< 10) = P(X<sqrt5) = (sqrt5-4)/2 = {(5**.5-2)/2:.5f}')

print('')
print('Ejercicio 3')
print('Hacer graficos y medir áreas, quedan paralelogramos')
print('F_W(w) = 2/3 * w 1{0<=w<1} + (w+1)/3 1{1<=w<2} + 1{w<=2}')


print('')
print('Ejercicio 4 parcial')
X1 = sps.binom(8, 0.1)
X2 = sps.binom(6, 0.1)
pej4 = X1.pmf(0)*X2.pmf(1)+X1.pmf(1)*X2.pmf(0)
print('X1 ~ Bin(8, 1/10); X2 ~ Bin(6, 1/10); independientes')
print(f'P(X1=0,X2=1 U X1=1, X2=0) = {pej4:.5f}')

print('')
print('Ejercicio 5 parcial')
ex = 2000*0.2 + 4000 * 0.3 + 0*0.5
ex2 = 2000**2 * 0.2 + 4000**2 * 0.3 + 0**2 * 0.5
vx = ex2-ex**2
n = 3300
S = sps.norm(n*ex, (n*vx)**.5)
print(f'E[X] = {ex:.5f}')
print(f'var(X) = {vx:.5f}')
print(f'S_0.05 = {S.ppf(0.05):.5f}')