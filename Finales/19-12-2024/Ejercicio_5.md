Para diseñar el test óptimo con nivel de significación \( \alpha \leq 0.05 \) y mínima probabilidad de error tipo II (\(\beta\)), seguimos estos pasos:

---

### **Paso 1: Definir las hipótesis**
- **Hipótesis nula** \( H_0: p(x) = p_0(x) \).
- **Hipótesis alternativa** \( H_1: p(x) = p_1(x) \).

Queremos diseñar una regla de decisión basada en una observación de \( X \).

---

### **Paso 2: Usar la razón de verosimilitudes**
La prueba más poderosa para hipótesis simples contra alternativas simples es el **test de razón de verosimilitudes**, que compara:

\[
\Lambda(x) = \frac{p_0(x)}{p_1(x)}
\]

Calculamos la razón para cada valor de \( X \):

\[
\begin{array}{c|c|c}
x & p_0(x) & p_1(x) & \Lambda(x) = \frac{p_0(x)}{p_1(x)} \\
\hline
1 & 0.70 & 0.05 & 14.00 \\
2 & 0.20 & 0.05 & 4.00 \\
3 & 0.05 & 0.10 & 0.50 \\
4 & 0.04 & 0.35 & 0.114 \\
5 & 0.01 & 0.45 & 0.0222 \\
\end{array}
\]

Para rechazar \( H_0 \), elegimos los valores de \( x \) donde la razón \( \Lambda(x) \) sea más **baja** (porque indica que es más probable bajo \( H_1 \)).

---

### **Paso 3: Elegir el umbral para \( \alpha \)**
El nivel de significación es:

\[
\alpha = P(\text{rechazar } H_0 | H_0 \text{ verdadera}).
\]

\[
\alpha = P(X \in C_R | H_0).
\]

Queremos \( \alpha \leq 0.05 \), por lo que sumamos las probabilidades más pequeñas de \( p_0(x) \):

- Para \( x = 5 \), \( P(X=5 | H_0) = 0.01 \).
- Para \( x = 4 \), \( P(X=4 | H_0) = 0.04 \).

Esto nos da \( \alpha = 0.01 + 0.04 = 0.05 \), que es justo el límite permitido.

Por lo tanto, la regla de rechazo óptima es:

\[
\text{Rechazar } H_0 \text{ si } X = 4 \text{ o } X = 5.
\]

---

### **Paso 4: Calcular \( \beta \)**
El error tipo II es:

\[
\beta = P(\text{no rechazar } H_0 | H_1).
\]

\[
\beta = P(X = 1, 2, 3 | H_1) = p_1(1) + p_1(2) + p_1(3).
\]

\[
\beta = 0.05 + 0.05 + 0.10 = 0.20.
\]

---

### **Conclusión**
- **Regla de decisión**: Rechazar \( H_0 \) si \( X = 4 \) o \( X = 5 \).
- **Nivel de significación**: \( \alpha = 0.05 \).
- **Error tipo II mínimo**: \( \beta = 0.20 \).

Este es el test más poderoso con nivel \( \alpha \leq 0.05 \).