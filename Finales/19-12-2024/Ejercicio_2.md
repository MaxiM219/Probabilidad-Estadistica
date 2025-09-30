Nos dan que \( T^2 \) sigue una distribución **exponencial** con media 25. Nuestro objetivo es determinar un tiempo de garantía \( t_g \) tal que la probabilidad de que el motor falle antes de ese tiempo sea a lo sumo 0.05.

---

### **Paso 1: Relación con la distribución exponencial**

Si \( T^2 \sim \text{Exp}(\lambda) \), sabemos que el **valor esperado** de una variable exponencial es:

\[
E[T^2] = \frac{1}{\lambda}
\]

Nos dicen que \( E[T^2] = 25 \), así que:

\[
\frac{1}{\lambda} = 25 \quad \Rightarrow \quad \lambda = \frac{1}{25}
\]

La función de distribución acumulativa (CDF) de una variable exponencial \( X \sim \text{Exp}(\lambda) \) es:

\[
P(X \leq x) = 1 - e^{-\lambda x}
\]

En este caso, reemplazamos \( X = T^2 \):

\[
P(T^2 \leq t_g^2) = 1 - e^{-\frac{t_g^2}{25}}
\]

Queremos que esta probabilidad sea como máximo 0.05:

\[
1 - e^{-\frac{t_g^2}{25}} \leq 0.05
\]

---

### **Paso 2: Despejar \( t_g \)**

\[
e^{-\frac{t_g^2}{25}} \geq 0.95
\]

Aplicamos logaritmo natural en ambos lados:

\[
-\frac{t_g^2}{25} \geq \ln(0.95)
\]

Usamos que \( \ln(0.95) \approx -0.0513 \):

\[
-\frac{t_g^2}{25} \geq -0.0513
\]

Multiplicamos por \( -1 \):

\[
\frac{t_g^2}{25} \leq 0.0513
\]

Multiplicamos por 25:

\[
t_g^2 \leq 1.2825
\]

Tomamos raíz cuadrada:

\[
t_g \leq \sqrt{1.2825}
\]

Aproximamos:

\[
t_g \leq 1.13
\]

---

### **Resultado Final:**
El fabricante debe ofrecer una garantía de **a lo sumo 1.13 años** si quiere que la probabilidad de reemplazo sea **como máximo 0.05**.