Para encontrar una cota inferior para la probabilidad de que un artículo tenga entre 600 y 1400 palabras, utilizamos **la desigualdad de Chebyshev**.

---

### **Paso 1: Definir la variable aleatoria**
Sea \( X \) la cantidad de palabras de un artículo, con:

- Media: \( \mathbb{E}[X] = \mu = 1000 \),
- Desviación estándar: \( \sigma = 200 \).

Queremos encontrar una cota inferior para:

\[
P(600 \leq X \leq 1400).
\]

Reescribimos el intervalo en términos de desviaciones estándar:

\[
P(1000 - 400 \leq X \leq 1000 + 400) = P(|X - 1000| \leq 400).
\]

Dividiendo por \( \sigma = 200 \):

\[
P\left(\left| \frac{X - 1000}{200} \right| \leq \frac{400}{200} \right) = P(|Z| \leq 2),
\]

donde \( Z \) es la variable estandarizada \( Z = \frac{X - \mu}{\sigma} \).

---

### **Paso 2: Aplicar la desigualdad de Chebyshev**
La desigualdad de Chebyshev establece que para cualquier \( k > 1 \):

\[
P(|X - \mu| \geq k\sigma) \leq \frac{1}{k^2}.
\]

Para \( k = 2 \):

\[
P(|X - 1000| \geq 400) \leq \frac{1}{2^2} = \frac{1}{4} = 0.25.
\]

Entonces,

\[
P(|X - 1000| \leq 400) \geq 1 - 0.25 = 0.75.
\]

---

### **Conclusión**
Una **cota inferior** para la probabilidad de que un artículo tenga entre 600 y 1400 palabras es **0.75 (o 75%)**.

### Mejor

Si queremos hallar la probabilidad sin usar la desigualdad de Chebyshev, podemos suponer que \(X\) sigue una distribución **normal** \( N(1000, 200^2) \) y calcular la probabilidad exacta utilizando la función de distribución normal estándar.

---

### **Paso 1: Estandarizar la variable**
Queremos calcular:

\[
P(600 \leq X \leq 1400)
\]

Estandarizamos usando la variable normal estándar \( Z \):

\[
Z = \frac{X - \mu}{\sigma} = \frac{X - 1000}{200}.
\]

Transformamos los límites:

\[
P\left( \frac{600 - 1000}{200} \leq Z \leq \frac{1400 - 1000}{200} \right).
\]

\[
P(-2 \leq Z \leq 2).
\]

---

### **Paso 2: Calcular probabilidades**
Usamos la tabla de la distribución normal estándar:

\[
P(Z \leq 2) = 0.9772, \quad P(Z \leq -2) = 0.0228.
\]

Por lo tanto:

\[
P(-2 \leq Z \leq 2) = P(Z \leq 2) - P(Z \leq -2).
\]

\[
0.9772 - 0.0228 = 0.9544.
\]

---

### **Conclusión**
Si asumimos que \( X \sim N(1000, 200^2) \), la probabilidad exacta de que un artículo tenga entre 600 y 1400 palabras es **0.9544 (o 95.44%)**.

Esta es una **cota inferior natural**, porque si la distribución no fuese normal, esta probabilidad podría ser menor, pero no mayor.