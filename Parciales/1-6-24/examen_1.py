import numpy as np
#import sympy as sy
import matplotlib.pyplot as plt
from scipy.integrate import quad, dblquad
from scipy.optimize import brentq, root
from scipy.special import comb, factorial, gamma
import scipy.stats as sps

# Examen
print('Probabilidad - 1-6-2024')
print('Ejercicio 1')
pd = factorial(3) * 4*3*5/(12*11*10)
pi = (4*3*2 + 3*2*1 + 5*4*3)/(12*11*10)
p = pi + pd*pi
print(f'P((I1) U (D1, I2) = P(I1) + P(D1)*P(I2) = {p:.5f}') 

print('')
print('Ejercicio 2 - PyE A')
def f(x,y): return 3/5*(x**2*y+x)
uno = dblquad(lambda y, x: f(x,y), 0,1,0,2)[0]
print(f'uno = {uno:.5f}')
ex = dblquad(lambda y, x: x*f(x,y), 0,1,0,2)[0]
ey = dblquad(lambda y, x: y*f(x,y), 0,1,0,2)[0]
exy = dblquad(lambda y, x: x*y*f(x,y), 0,1,0,2)[0]
cov = exy - ex*ey
print(f'cov(2X,Y) = 2 cov(X,Y) = {2*cov:.5f}')

print('')
print('Ejercicio 3')
print('Observar que X~U(0, 3), Y|X=x ~ Gamma(2, 1/(x+1))')
print('de tabla E[Y|X=2] = 6')
print('Alternativa: hacer todas las cuentas')

print('Solucion numerica haciendo cuentas')
def f(y, x): return 1/3 * y/(x+1)**2 * np.exp(-y / (x+1)) #x 0 a 3, y 0 a inf
x0 = 2
uno = dblquad(f, 0, 3, 0, np.inf)[0] #Revisar que la densidad integre 1
den = quad(lambda y: f(y, x0), 0, np.inf)[0] #f_X(x0)
num = lambda y: y * f(y, x0) #y * f_XY (x0, y)
ey_x1 = quad(num, 0, np.inf)[0] / den
print(f'uno = {uno:.5f}')
print(f'E[Y|X={x0}] = {ey_x1:.5f}')
print('')
print('Para proba B')
print('E[Y|X] = 2(X+1)')
print('P(2X+2 < 6) = P(X<2) = 2/3')

print('')
print('Ejercicio 4')
print('P, C, N ~ Mul(16, 0.4, 0.5, 0.1)')
print('P|C=7 ~ Bin(9, 0.5/0.6')
PdC7 = sps.binom(9, 5/6)
print(f'P(P<=8|C=7) = {PdC7.cdf(8):.5f}')
    
print('')
print('Ejercicio 5')
print('X ~ N(mu, s2), P(X<x1) = p1, P(X>x2) = p2, sistema 2x2 lineal')
print('se resuelve a mano (aca solver numerico por fiaca)')
x1 = 900
p1 =  0.15866
x2 = 1200
p2 = 0.02275
def cero(musig):
    X = sps.norm(musig[0], musig[1])
    return np.array([X.cdf(x1)-p1, X.sf(x2)-p2])
sol = root(cero, np.array([(x1+x2)/2, (x1+x2)/20]))
mu = sol.x[0]
sig = sol.x[1]
print(f'mu = {mu:.5f}, sig = {sig:.5f}')
X = sps.norm(mu, sig)
num = X.cdf(1150)-X.cdf(1000)
den = X.sf(1000)
print(f'P(X<1150|X>1000) = {num:.3f}/{den:.3f} = {num/den:.5f}')