Dado que \(X\) es una variable aleatoria geométrica de parámetro \(p\), su función de probabilidad es:

\[
P(X = k) = (1 - p)^{k-1} p, \quad k = 1, 2, 3, \dots
\]

La media de \(X\) es:

\[
E[X] = \frac{1}{p}
\]

### **Paso 1: Estimador de Máxima Verosimilitud de \(p\)**

Para una muestra \(X_1, X_2, \dots, X_n\) de una distribución geométrica \(X \sim \text{Geom}(p)\), la función de verosimilitud es:

\[
L(p) = \prod_{i=1}^{n} (1 - p)^{X_i - 1} p
\]

Tomando el logaritmo:

\[
\ell(p) = \sum_{i=1}^{n} \left( (X_i - 1) \ln(1 - p) + \ln p \right)
\]

Derivando respecto a \(p\) e igualando a cero:

\[
\frac{d}{dp} \ell(p) = \sum_{i=1}^{n} \left( \frac{(X_i - 1)}{1 - p} - \frac{1}{p} \right) = 0
\]

Resolviendo para \(p\), obtenemos el estimador de máxima verosimilitud:

\[
\hat{p} = \frac{n}{\sum_{i=1}^{n} X_i}
\]

El estimador de la media \(E[X]\) es:

\[
\hat{\mu} = \frac{1}{\hat{p}} = \frac{\sum_{i=1}^{n} X_i}{n}
\]

lo cual es simplemente la media muestral \( \bar{X} \).

### **Paso 2: Calcular el Error Cuadrático Medio (ECM)**

El error cuadrático medio de \( \hat{\mu} \) está dado por:

\[
ECM(\hat{\mu}) = E[(\hat{\mu} - E[X])^2]
\]

Usando la propiedad de varianza:

\[
ECM(\hat{\mu}) = \text{Var}(\hat{\mu}) + (E[\hat{\mu}] - E[X])^2
\]

Dado que \(E[\hat{\mu}] = E[X] = \frac{1}{p}\), el segundo término es cero. Por lo tanto:

\[
ECM(\hat{\mu}) = \text{Var}(\hat{\mu})
\]

Sabemos que la varianza de \(X\) es:

\[
\text{Var}(X) = \frac{1 - p}{p^2}
\]

Como \( \hat{\mu} \) es la media muestral:

\[
\text{Var}(\hat{\mu}) = \frac{\text{Var}(X)}{n} = \frac{(1 - p)}{n p^2}
\]

Por lo tanto, el error cuadrático medio del estimador de la media de \(X\) es:

\[
ECM(\hat{\mu}) = \frac{(1 - p)}{n p^2}
\]