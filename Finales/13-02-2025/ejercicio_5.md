## Test de Hipótesis con Nivel de Significación \(\alpha \leq 0.05\)

### **Enunciado**
Se observa un único valor de la variable aleatoria \(X\), cuya función de probabilidad puede ser \(p_0(x)\) o \(p_1(x)\):

| \( x \)  | \( p_0(x) \) | \( p_1(x) \) |
|---------|------------|------------|
| 1       | 0.70       | 0.05       |
| 2       | 0.20       | 0.05       |
| 3       | 0.05       | 0.10       |
| 4       | 0.04       | 0.35       |
| 5       | 0.01       | 0.45       |

Se desea probar las hipótesis:

- **\(H_0\):** \(p(x) = p_0(x)\)
- **\(H_1\):** \(p(x) = p_1(x)\)

### **Paso 1: Razón de Verosimilitud**
Se calcula la razón de verosimilitud:

\[
\Lambda(x) = \frac{p_1(x)}{p_0(x)}
\]

| \( x \)  | \( \Lambda(x) \)  |
|---------|------------------|
| 1       | 0.0714  |
| 2       | 0.25    |
| 3       | 2.0     |
| 4       | 8.75    |
| 5       | 45.0    |

### **Paso 2: Determinar la Regla de Rechazo**
Para \(\alpha \leq 0.05\), elegimos los valores de \(x\) con mayor \(\Lambda(x)\) hasta que la suma de probabilidades bajo \(H_0\) no supere 0.05:

\[
P_{H_0}(X = 5) + P_{H_0}(X = 4) = 0.01 + 0.04 = 0.05
\]

Por lo tanto, la regla de rechazo es:

\[
\text{Rechazar } H_0 \text{ si } X = 4 \text{ o } X = 5.
\]

### **Paso 3: Calcular el Error Tipo II (\(\beta\))**
El error tipo II es:

\[
\beta = P_{H_1}(X = 1) + P_{H_1}(X = 2) + P_{H_1}(X = 3)
\]

Sustituyendo valores:

\[
\beta = 0.05 + 0.05 + 0.10 = 0.20
\]

### **Conclusión**
El test óptimo con \(\alpha = 0.05\) y mínimo \(\beta\) es:

- **Regla de rechazo:** Rechazar \(H_0\) si \(X = 4\) o \(X = 5\).
- **Error tipo II:** \(\beta = 0.20\).

