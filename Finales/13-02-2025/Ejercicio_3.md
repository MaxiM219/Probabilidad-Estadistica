Si queremos calcular la probabilidad de que un artículo tenga entre **600 y 1400 palabras** sin usar la desigualdad de Chebyshev, debemos hacer una suposición razonable sobre la distribución de la cantidad de palabras.  

Dado que solo nos dan la media y la desviación estándar, **suponemos que la cantidad de palabras sigue una distribución normal**:

\[
X \sim N(1000, 200^2)
\]

Luego, podemos calcular la probabilidad usando la distribución normal y la regla de la probabilidad total.

---

### **Paso 1: Estandarización**
Definimos la variable tipificada:

\[
Z = \frac{X - \mu}{\sigma} = \frac{X - 1000}{200}
\]

Queremos calcular:

\[
P(600 \leq X \leq 1400)
\]

Esto equivale a:

\[
P\left( \frac{600 - 1000}{200} \leq Z \leq \frac{1400 - 1000}{200} \right)
\]

\[
P\left( \frac{-400}{200} \leq Z \leq \frac{400}{200} \right)
\]

\[
P(-2 \leq Z \leq 2)
\]

---

### **Paso 2: Usar la tabla de la normal estándar**

La probabilidad acumulada de \( Z = 2 \) en la tabla de la normal estándar es:

\[
P(Z \leq 2) = 0.9772
\]

La probabilidad acumulada de \( Z = -2 \) es:

\[
P(Z \leq -2) = 0.0228
\]

Por lo tanto, la probabilidad de estar entre -2 y 2 es:

\[
P(-2 \leq Z \leq 2) = P(Z \leq 2) - P(Z \leq -2)
\]

\[
= 0.9772 - 0.0228 = 0.9544
\]

---

### **Resultado Final**
Bajo la **suposición de normalidad**, la probabilidad de que un artículo tenga entre **600 y 1400 palabras** es aproximadamente **0.9544 (95.44%)**.