## Estimación del 0.90-Cuantil para una Distribución Exponencial

### Enunciado del Problema
La cantidad de agua (en mm) precipitada en un día de lluvia en la ciudad de Zorg es una variable aleatoria
\(X\) con distribución exponencial de parámetro \(\lambda\), independientemente del día. Durante 5 días se midieron las siguientes cantidades de agua precipitada:

\[ 7.44, 12.1, 25.81, 20.52, 27.05. \]

A partir de la muestra observada, se busca hallar el estimador de máxima verosimilitud para el 0.90-cuantil de \(X\).

### Paso 1: Estimación de \(\lambda\)
Para una muestra \(X_1, X_2, ..., X_n\) de una distribución exponencial \(X \sim \text{Exp}(\lambda)\), la función de verosimilitud es:

\[
L(\lambda) = \prod_{i=1}^{n} \lambda e^{-\lambda x_i}
\]

Tomando el logaritmo:

\[
\ell(\lambda) = \sum_{i=1}^{n} \ln \lambda - \lambda \sum_{i=1}^{n} x_i
\]

Derivando respecto de \(\lambda\) e igualando a cero:

\[
\frac{d}{d\lambda} \ell(\lambda) = \frac{n}{\lambda} - \sum_{i=1}^{n} x_i = 0
\]

De donde obtenemos el estimador de máxima verosimilitud:

\[
\hat{\lambda} = \frac{n}{\sum_{i=1}^{n} x_i}
\]

Sustituyendo los valores de la muestra:

\[
\hat{\lambda} = \frac{5}{7.44 + 12.1 + 25.81 + 20.52 + 27.05} \approx 0.0538
\]

### Paso 2: Cálculo del 0.90-Cuantil
El \(p\)-cuantil de una distribución exponencial \(X \sim \text{Exp}(\lambda)\) se obtiene resolviendo:

\[
P(X \leq q_p) = p
\]

Dado que la función de distribución acumulada es:

\[
F(x) = 1 - e^{-\lambda x}
\]

despejamos \(q_p\):

\[
q_p = -\frac{\ln(1 - p)}{\lambda}
\]

Sustituyendo \(p = 0.90\) y \(\hat{\lambda} = 0.0538\):

\[
q_{0.90} = -\frac{\ln(0.10)}{0.0538} \approx 42.79 \text{ mm}
\]

### Resultado Final
El estimador de máxima verosimilitud para el 0.90-cuantil de \(X\) es:

\[
\hat{q}_{0.90} \approx 42.79 \text{ mm}
\]

