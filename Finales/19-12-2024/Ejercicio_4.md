Para estimar el **0.90-cuantil** de \( X \) usando el **estimador de máxima verosimilitud (EMV)**, seguimos estos pasos:

---

### **Paso 1: EMV del parámetro \( \lambda \)**
Sabemos que si \( X \sim \text{Exp}(\lambda) \), el estimador de máxima verosimilitud para \( \lambda \) es:

\[
\hat{\lambda} = \frac{1}{\bar{x}}
\]

donde \( \bar{x} \) es la media muestral:

\[
\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i.
\]

---

### **Paso 2: Cuantil de una exponencial**
El **p-cuántil** de una distribución exponencial \( X \sim \text{Exp}(\lambda) \) se obtiene resolviendo:

\[
P(X \leq q_p) = p.
\]

Usando la función de distribución acumulada de la exponencial:

\[
1 - e^{-\lambda q_p} = p.
\]

Despejamos \( q_p \):

\[
q_p = \frac{-\ln(1 - p)}{\lambda}.
\]

Para el caso del **0.90-cuantil** (\( p = 0.90 \)):

\[
q_{0.90} = \frac{-\ln(0.10)}{\lambda}.
\]

---

### **Paso 3: Sustituir el estimador de \( \lambda \)**
Usamos el estimador \( \hat{\lambda} = \frac{1}{\bar{x}} \) en la fórmula del cuantil:

\[
\hat{q}_{0.90} = -\ln(0.10) \cdot \bar{x}.
\]

Ahora lo calculamos numéricamente.

### **Resultados:**
- Media muestral: \( \bar{x} \approx 18.58 \)
- Estimador de máxima verosimilitud de \( \lambda \): \( \hat{\lambda} \approx 0.0538 \)
- Estimador del **0.90-cuantil**:  
  \[
  \hat{q}_{0.90} \approx 42.79
  \]

Por lo tanto, el estimador de máxima verosimilitud para el **0.90-cuantil** de la distribución es **42.79 mm**.