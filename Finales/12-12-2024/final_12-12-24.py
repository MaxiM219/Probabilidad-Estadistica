import numpy as np
#import sympy as sy
#import matplotlib.pyplot as plt
from scipy.integrate import quad, dblquad
#from scipy.optimize import brentq
#from scipy.special import comb, factorial, gamma
import scipy.stats as sps

# EXAMEN
print('Ejercicio 1')
pC2 = 4/8*3/7 + 4/8*3/7
pC3 = 1-pC2
pB = 7/10 * pC2 + 3/9 * pC3
pRR = 4/8*3/7
pBdRR = 7/10
pRRdB = (pBdRR * pRR) / pB
print(f'P(R1R2|B) = P(B|R1R2) * P(R1R2) / P(B) = {pRRdB:.5f}')

print('')
print('Ejercicio 2')
print('Solucion numerica haciendo cuentas')
def f(x, y): 
    return 4 * np.exp(-2*y)  #0 < x < y2
uno = dblquad(lambda y, x: f(x, y), 0, np.inf, lambda x: x**.5, np.inf)[0] #Revisar que la densidad integre 1
#den = quad(lambda y: f(y, 1), 0, np.inf)[0] #f_X(1)
#num = lambda y: y * f(y, 1) #y * f_XY (1, y)
#ey_x1 = quad(num, 0, np.inf)[0] / den
ex = dblquad(lambda y, x: x * f(x, y), 0, np.inf, lambda x: x**.5, np.inf)[0]
print(f'1 = {uno:.5f}')
print(f'E[X|Y=y] = y**2/2    pues es uniforme (0, y^2)')
print(f'E[X] = {ex:.5f}       hacer cuentas o usar E[X]=E[E[Y|X]]')

print('')
print('Ejercicio 3')
print('Hacer graficos y medir áreas, quedan paralelogramos')
print('F_W(w) = w/2 1{0<=w<2} + 1{2<=w}; luego W~U(0, 2)')


print('')
print('Ejercicio 4 final PyE')
print('Sea mu = EX = 1/P, mu_est = X_prom')
print('E[mu_est] = mu insesgado')
print('var(mu_est) = 1/n var(X) = 1/n (1-p)/p**2 = ecm(mu_est, mu)')


print('')
print('Ejercicio 5 final PyE')
xmean = 497.735
s = 6.68
n = 30
tlim = sps.t.isf(.025, n-1)
tobs = (xmean - 500) / (s/n**.5)
pval = sps.t.sf(np.abs(tobs), n-1)*2 
print('Delta(X) = 1 {t_obs notin +-tlim}')
print(f'tobs = {tobs:.5f}')
print(f'tlim = {tlim:.5f}')
print(f'pval(x) = {pval:.5f}')
if pval <= 0.05:
    print('Se rechaza H0')
else:
    print('No hay evidencia para rechazar H0')

print('')
print('Ejercicio 4 final Industriales, ej 5 parcial')
pp = np.array([0.2, 0.4, 0.3, 0.1])
xx = np.array([4, 5, 6, 7])
ex = np.sum(pp*xx)
ex2 = np.sum(pp*xx**2)
vx = ex2 - ex**2
n = 36
S = sps.norm(n*ex, (n*vx)**.5)
print(f'E[X] = {ex:.5f}')
print(f'var(X) = {vx:.5f}')
print(f'P(Xprom < 5.5) = P(Suma < n*5.5) = {S.cdf(n*5.5):.5f} sin corr cont')
print(f'P(Xprom < 5.5) = P(Suma < n*5.5-0.5) = {S.cdf(n*5.5-.5):.5f} con corr cont')

print('')
print('Ejercicio 4 parcial')
print('C|Nt=5 ~ Bin(5, p = 1/2 / (1+5/4+1/2)')
C = sps.binom(5, 1/2 / (1+5/4+1/2) )
print(f'P( (C|Nt=5) = 0) = {C.pmf(0):.5f}')