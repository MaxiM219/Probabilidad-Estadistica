import numpy as np
print(np.__version__)

# Guia 11
# 4. La cantidad de agua (en mm) precipitada en un día de lluvia en la ciudad de Zorg es una variable aleatoria
# X con distribucion exponencial de parámetro λ, independientemente del día. Durante 5 días se midieron las
# siguientes cantidades de agua precipitada
# 7.44, 12.1, 25.81, 20.52, 27.05.
# A partir de la muestra observada, hallar el estimador de máxima verosimilitud para el 0.90-cuantil de X.

# Datos de la muestra
muestra = np.array([7.44, 12.1, 25.81, 20.52, 27.05])

# Estimador de máxima verosimilitud de λ
n = len(muestra)
#^lambda ^λ
lambda_hat = n / np.sum(muestra)

print(lambda_hat)

# Cuantil 0.90
p = 0.90
q_90_hat = -np.log(1 - p) / lambda_hat
print("^λ en 0.90", q_90_hat)

lambda_hat, q_90_hat