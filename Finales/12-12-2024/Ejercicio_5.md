Este es un problema de **contraste de hipótesis** sobre la media de una población normal con varianza desconocida. Seguimos estos pasos:

---

### **Paso 1: Planteo de hipótesis**
Queremos contrastar la afirmación del proveedor de que la densidad media es \( 500 \) kg/m³. Planteamos las hipótesis:

- **Hipótesis nula** \( H_0 \): \( \mu = 500 \) kg/m³ (la afirmación del proveedor es correcta).
- **Hipótesis alternativa** \( H_1 \): \( \mu \neq 500 \) kg/m³ (la afirmación del proveedor es incorrecta).

Como no nos dicen explícitamente que sospechamos que la densidad es menor o mayor, hacemos un **test bilateral**.

---

### **Paso 2: Estadístico de prueba**
Dado que la variable sigue una distribución normal y la varianza es desconocida, usamos el **estadístico t de Student**:

\[
t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}
\]

donde:
- \( \bar{x} = 497.735 \) (media muestral),
- \( \mu_0 = 500 \) (hipótesis nula),
- \( s = 6.680 \) (desvío estándar muestral),
- \( n = 30 \) (tamaño muestral).

Sustituyamos los valores y calculemos \( t \).

El valor del estadístico de prueba es \( t = -1.857 \).  

---

### **Paso 3: Región crítica**
Dado que el test es bilateral con un nivel de significación \( \alpha = 0.05 \), buscamos los valores críticos para una **t de Student con \( n-1 = 29 \) grados de libertad**:

\[
t_{\alpha/2, 29} = t_{0.025, 29}
\]

Calculamos este valor crítico.

El valor crítico es \( t_{0.025, 29} = 2.045 \).  

La región de rechazo es:

\[
t < -2.045 \quad \text{o} \quad t > 2.045
\]

Dado que \( t = -1.857 \) **no cae en la región de rechazo**, **no podemos rechazar \( H_0 \)** al nivel de significación del 5%.

---

### **Paso 4: Conclusión**
Al 5% de significación, **no hay evidencia suficiente para refutar la afirmación del proveedor** de que la densidad media es \( 500 \) kg/m³.