Para hallar la función de distribución de \( W = 2(X + Y - 1) \), seguimos estos pasos:

### **Paso 1: Determinar los valores extremos de \( W \)**
Dado que \( (X, Y) \) sigue una distribución uniforme en la región:

\[
R = \{ (x, y) : 0 < x < 2, \quad 1 - x < y < 3 - x \}
\]

Definimos \( W \) en términos de \( X \) y \( Y \):

\[
W = 2(X + Y - 1).
\]

Para encontrar los valores mínimo y máximo de \( W \), evaluamos los extremos de la región \( R \):

- **Valor mínimo de \( W \)**: cuando \( X = 0 \) y \( Y = 1 - X = 1 \):

  \[
  W_{\min} = 2(0 + 1 - 1) = 0.
  \]

- **Valor máximo de \( W \)**: cuando \( X = 2 \) y \( Y = 3 - X = 1 \):

  \[
  W_{\max} = 2(2 + 1 - 1) = 4.
  \]

Por lo tanto, \( W \) toma valores en \( [0, 4] \).

---

### **Paso 2: Determinar la función de distribución \( F_W(w) = P(W \leq w) \)**
\[
P(W \leq w) = P(2(X + Y - 1) \leq w) = P(X + Y \leq 1 + \frac{w}{2}).
\]

Esto se traduce en calcular el área de la región \( X + Y \leq 1 + \frac{w}{2} \) dentro de \( R \). La distribución es uniforme, por lo que la probabilidad se obtiene como la fracción del área contenida en esta subregión.

---

### **Paso 3: Graficar \( F_W(w) \)**
Procedemos a graficar la función de distribución \( F_W(w) \).

Aquí tienes la gráfica de la función de distribución acumulada \( F_W(w) \). La función comienza en 0, crece cuadráticamente en el intervalo \( [0,4] \) y alcanza 1 en \( w = 4 \).