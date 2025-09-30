### **Paso 1: Definir la Prueba de Hipótesis**  
Queremos comprobar la afirmación de Tomás de que \( \lambda > 0.125 \), es decir, realizar la prueba de hipótesis:  

\[
H_0: \lambda = 0.125 \quad \text{(hipótesis nula)}
\]
\[
H_1: \lambda > 0.125 \quad \text{(hipótesis alternativa)}
\]

Dado que los tiempos \( X_1, X_2, X_3, X_4, X_5 \) siguen una distribución **exponencial con parámetro \( \lambda \)**, su media es:

\[
E[X] = \frac{1}{\lambda}
\]

Para probar la hipótesis, podemos usar el **estimador de máxima verosimilitud (EMV) de \( \lambda \)**:

\[
\hat{\lambda} = \frac{n}{\sum X_i}
\]

y construir un test basado en la media muestral.

---

### **Paso 2: Calcular la Media Muestral y el Estimador \( \hat{\lambda} \)**  
La muestra es:  
\[
X_1 = 3, \quad X_2 = 5, \quad X_3 = 6, \quad X_4 = 2, \quad X_5 = 9
\]

\[
\bar{X} = \frac{3+5+6+2+9}{5} = \frac{25}{5} = 5
\]

El estimador de \( \lambda \) es:

\[
\hat{\lambda} = \frac{n}{\sum X_i} = \frac{5}{25} = 0.2
\]

---

### **Paso 3: Regla de Decisión**  
Usamos el hecho de que la media muestral \( \bar{X} \) de una distribución exponencial sigue una distribución gamma:

\[
\bar{X} \sim \text{Gamma}(n, \lambda)
\]

Cuando \( n \) es grande, por el teorema central del límite, podemos aproximar \( \bar{X} \) con una distribución normal:

\[
\bar{X} \approx N\left(\frac{1}{\lambda}, \frac{1}{n\lambda^2}\right)
\]

Bajo \( H_0 \) (\(\lambda = 0.125\)):

\[
E[\bar{X}] = \frac{1}{0.125} = 8, \quad \text{Var}[\bar{X}] = \frac{1}{5(0.125)^2} = \frac{1}{5 \times 0.015625} = \frac{1}{0.078125} \approx 12.8
\]

Entonces,

\[
\bar{X} \sim N(8, \sqrt{12.8}) = N(8, 3.58)
\]

Para un nivel de significación \( \alpha = 0.05 \), rechazamos \( H_0 \) si \( \bar{X} \) es significativamente menor que 8. El valor crítico es:

\[
z_{0.05} = -1.645
\]

Convertimos a la escala de \( \bar{X} \):

\[
\text{Regla de decisión: Rechazar } H_0 \text{ si } \bar{X} < 8 + (-1.645) \times \frac{3.58}{\sqrt{5}}
\]

\[
= 8 - 1.645 \times 1.6
\]

\[
= 8 - 2.632 = 5.368
\]

---

### **Paso 4: Tomar una Decisión**  
Tenemos que:

\[
\bar{X} = 5 < 5.368
\]

Como la media muestral es menor que el umbral de rechazo, **rechazamos \( H_0 \)**. Es decir, hay evidencia suficiente para aceptar la afirmación de Tomás de que \( \lambda > 0.125 \) con un nivel de significación \( \alpha = 0.05 \).

---

### **Conclusión**  
- **Regla de decisión:** Rechazar \( H_0 \) si \( \bar{X} < 5.368 \).  
- **Decisión con la muestra:** Como \( \bar{X} = 5 \), **rechazamos \( H_0 \)**.  
- **Interpretación:** Hay suficiente evidencia para concluir que \( \lambda > 0.125 \).

### Otra

### **Planteamiento del problema**  
Nos dan una muestra de tiempos de duración (\(X_1, X_2, X_3, X_4, X_5\)) que siguen una **distribución exponencial** con parámetro \(\lambda\):  
\[
X_i \sim \text{Exp}(\lambda), \quad i = 1,2,3,4,5
\]  
La función de densidad de una distribución exponencial es:  
\[
f(x; \lambda) = \lambda e^{-\lambda x}, \quad x > 0, \lambda > 0
\]  

Tomás afirma que \(\lambda > 0.125\). Queremos comprobar si la afirmación es consistente con la muestra mediante un **test de hipótesis**.

---

### **Paso 1: Formular las hipótesis**  
Planteamos el test de hipótesis:

- **Hipótesis nula (\(H_0\))**: \(\lambda = 0.125\)  
- **Hipótesis alternativa (\(H_1\))**: \(\lambda > 0.125\)  

Este es un **test unilateral derecho**.

---

### **Paso 2: Estadístico de prueba**  
Para una muestra de una distribución exponencial \(X_1, X_2, ..., X_n\), el estimador de máxima verosimilitud de \(\lambda\) es:  

\[
\hat{\lambda} = \frac{1}{\bar{X}}
\]

Donde \(\bar{X}\) es la media muestral:

\[
\bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i
\]

Bajo \(H_0\), se sabe que:

\[
\frac{2n\bar{X} \lambda_0}{\sigma^2} \sim \chi^2_{2n}
\]

Dado que en una distribución exponencial \(E[X] = \frac{1}{\lambda}\), se cumple que:

\[
\frac{2n\lambda_0}{\hat{\lambda}} \sim \chi^2_{2n}
\]

Utilizaremos esta distribución para la región crítica.

---

### **Paso 3: Calcular el estadístico con los datos**  
La muestra es:

\[
3, 5, 6, 2, 9
\]

Calculamos la media muestral:

\[
\bar{X} = \frac{3 + 5 + 6 + 2 + 9}{5} = \frac{25}{5} = 5
\]

El estimador de \(\lambda\):

\[
\hat{\lambda} = \frac{1}{\bar{X}} = \frac{1}{5} = 0.2
\]

---

### **Paso 4: Región de rechazo**  
Queremos verificar si \(\lambda\) es significativamente mayor que 0.125. Bajo \(H_0\), el estadístico:

\[
T = \frac{2n\lambda_0}{\hat{\lambda}}
\]

sigue una distribución \(\chi^2_{2n}\). Calculamos:

\[
T = \frac{2(5)(0.125)}{0.2} = \frac{1.25}{0.2} = 6.25
\]

Para un nivel de significación \(\alpha = 0.05\), buscamos el **cuantil del 95%** de una \(\chi^2_{2(5)} = \chi^2_{10}\):

\[
\chi^2_{10, 0.95} = 18.31
\]

La **región de rechazo** es:

\[
T > 18.31
\]

Como \(T = 6.25\) **no** está en la región de rechazo, **no rechazamos \(H_0\)**.

---

### **Paso 5: Conclusión**  
Dado que el estadístico de prueba no cae en la región de rechazo, **no hay suficiente evidencia estadística para afirmar que \(\lambda > 0.125\) con un nivel de significación del 5%**.  

Por lo tanto, **no podemos respaldar la afirmación de Tomás** de que \(\lambda > 0.125\).