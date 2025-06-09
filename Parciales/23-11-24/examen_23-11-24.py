import numpy as np
#import sympy as sy
import matplotlib.pyplot as plt
from scipy.integrate import quad, dblquad
from scipy.optimize import brentq, minimize
#from scipy.special import comb, factorial, gamma
import scipy.stats as sps

print('Examenes 02-11-2024')
print('Ej 1')
print('Graficar grilla, para el maso bueno hay')
print('pg = 14/25, pp = 6/25, pe = 5/25')
px3b = (6/25)**3
px3m = (14/25)**3
pb = 1/2
pm = 1 - pb
pbx3 = px3b*pb / (px3b*pb + px3m*pm)
print(f'por bayes, P(B|X3)=P(X3|B)*P(B)/P(X3) = {pbx3:.5f}')

print('')
print('Ej 2')
print('X1 ~ bin(4, 1/3)')
print('X2 ~ bin(6, 3/4)')
X1 = sps.binom(4, 1/3)
X2 = sps.binom(6, 3/4)
p = X1.pmf(0)*X2.pmf(0) + X1.pmf(1)*X2.pmf(0) + X1.pmf(0)*X2.pmf(1)
print(f'P(X<=1) = P(00) + P(01) + P(10) = {p:.5f}')
print(f'P(X>1) = {1-p:.5f}')

print('')
print('Ej 3')
print('hacer graficos, las curvas de nivel son dos rectas a 45°')
print('equidistantes de la identidad x=y')
print('F_w(w) = P(W<w) = 2w*4 / 8 = w   para 0<=w<1, area paralelogramo')
print('luego')
print('F_W(w) = w 1{0<=w<1} + 1{1<=w}      W es U(0, 1) ')

print('')
print('Ej 4')
print('E[N|NC=10] E[NA+NC|NC=10] = E[NA|NC=10]+10 = ...')
print('por coloracion o adelgazamiento')
print(f'...= E[NA]+10 = 0.75*30 + 10 = {30*.75+10:.2f}')


print('')
print('Ej 5')
n = 184
mu_x = 40
des_x = 10
mu = n*mu_x
des = n**.5 * des_x
S = sps.norm(mu, des)
print(f'mu_S = {mu:.2f}')
print(f'des_S = {des:.2f}')
print(f's_0.95 = {S.isf(0.05):.1f} min = {S.isf(0.05)/60:.2f} hr')