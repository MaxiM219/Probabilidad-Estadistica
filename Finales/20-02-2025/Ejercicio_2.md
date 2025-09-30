Queremos calcular la esperanza del costo de tratamiento de una arandela tomada al azar.  

### **Paso 1: Definir la variable aleatoria**  
Sea \( X \) el diámetro de la arandela, que sigue una distribución normal:  
\[
X \sim N(5, 0.1^2)
\]
Las categorías de tratamiento dependen de la desviación respecto a \( 5 \):

- **Tratamiento sencillo (1 peso)**: Si \( |X - 5| < 0.05 \)  
- **Tratamiento de adaptación (5 pesos)**: Si \( 0.05 \leq |X - 5| < 0.08 \)  
- **Tratamiento complicado (10 pesos)**: Si \( |X - 5| \geq 0.08 \)  

Definimos la variable de costo \( C \), que toma valores:  
\[
C =
\begin{cases}
1, & \text{si } |X - 5| < 0.05 \\
5, & \text{si } 0.05 \leq |X - 5| < 0.08 \\
10, & \text{si } |X - 5| \geq 0.08
\end{cases}
\]

Queremos calcular la **esperanza del costo**, es decir:

\[
E[C] = 1 \cdot P(|X - 5| < 0.05) + 5 \cdot P(0.05 \leq |X - 5| < 0.08) + 10 \cdot P(|X - 5| \geq 0.08)
\]

---

### **Paso 2: Probabilidades Asociadas**
Definimos la variable tipificada:

\[
Z = \frac{X - 5}{0.1} \sim N(0,1)
\]

Calculamos cada probabilidad:

1. **Tratamiento sencillo**:  
\[
P(|X - 5| < 0.05) = P\left(-0.5 < Z < 0.5\right)
\]
Buscando en la tabla de la normal estándar:

\[
P(Z < 0.5) \approx 0.6915, \quad P(Z < -0.5) \approx 0.3085
\]

\[
P(-0.5 < Z < 0.5) = 0.6915 - 0.3085 = 0.383
\]

2. **Tratamiento de adaptación**:  
\[
P(0.05 \leq |X - 5| < 0.08) = P(0.5 \leq Z < 0.8) + P(-0.8 < Z \leq -0.5)
\]

De la tabla:

\[
P(Z < 0.8) \approx 0.7881, \quad P(Z < -0.8) \approx 0.2119
\]

\[
P(Z < 0.5) \approx 0.6915, \quad P(Z < -0.5) \approx 0.3085
\]

\[
P(0.5 \leq Z < 0.8) = 0.7881 - 0.6915 = 0.0966
\]

\[
P(-0.8 < Z \leq -0.5) = 0.3085 - 0.2119 = 0.0966
\]

\[
P(0.05 \leq |X - 5| < 0.08) = 0.0966 + 0.0966 = 0.1932
\]

3. **Tratamiento complicado**:  
\[
P(|X - 5| \geq 0.08) = P(Z \geq 0.8) + P(Z \leq -0.8)
\]

\[
P(Z \geq 0.8) = 1 - 0.7881 = 0.2119
\]

\[
P(Z \leq -0.8) = 0.2119
\]

\[
P(|X - 5| \geq 0.08) = 0.2119 + 0.2119 = 0.4238
\]

---

### **Paso 3: Cálculo de la Esperanza**
\[
E[C] = 1(0.383) + 5(0.1932) + 10(0.4238)
\]

\[
= 0.383 + 0.966 + 4.238
\]

\[
= 5.587
\]

---

### **Resultado Final**
La esperanza del costo de tratamiento de una arandela tomada al azar es **5.59 pesos (aproximadamente)**.

### Otra forma 
Queremos calcular la **esperanza del costo de tratamiento** para una arandela cuyo diámetro sigue una **distribución normal** \(X \sim N(5, 0.1^2)\).

---

### **Paso 1: Definir los eventos y sus probabilidades**
Sea \(X\) el diámetro de la arandela. Las tolerancias de instalación determinan 3 rangos de tratamiento:

1. **Aptas (Costo = 1 peso):**  
   - \( 4.95 \leq X \leq 5.05 \)
   - Probabilidad: \( P(4.95 \leq X \leq 5.05) \)

2. **Adaptación (Costo = 5 pesos):**  
   - \( 4.92 \leq X < 4.95 \) ó \( 5.05 < X \leq 5.08 \)
   - Probabilidad: \( P(4.92 \leq X < 4.95) + P(5.05 < X \leq 5.08) \)

3. **Tratamiento complicado (Costo = 10 pesos):**  
   - \( X < 4.92 \) ó \( X > 5.08 \)
   - Probabilidad: \( P(X < 4.92) + P(X > 5.08) \)

Dado que \(X\) es normal \(N(5, 0.1^2)\), usamos la **estandarización**:

\[
Z = \frac{X - 5}{0.1} \sim N(0,1)
\]

Transformamos los límites a la escala \(Z\):

\[
P(a \leq X \leq b) = P\left( \frac{a - 5}{0.1} \leq Z \leq \frac{b - 5}{0.1} \right)
\]

### **Paso 2: Calcular las probabilidades usando la distribución normal estándar**
Usamos la tabla de la normal estándar para encontrar los valores de \( P(Z \leq z) \):

| Límite en \(X\) | Límite en \(Z\) | \( P(Z \leq z) \) |
|-----------------|-----------------|-----------------|
| 4.92           | \( \frac{4.92 - 5}{0.1} = -0.8 \) | 0.2119 |
| 4.95           | \( \frac{4.95 - 5}{0.1} = -0.5 \) | 0.3085 |
| 5.05           | \( \frac{5.05 - 5}{0.1} = 0.5 \) | 0.6915 |
| 5.08           | \( \frac{5.08 - 5}{0.1} = 0.8 \) | 0.7881 |

Ahora, calculamos las probabilidades de cada categoría:

1. **Aptas (1 peso):**
   \[
   P(4.95 \leq X \leq 5.05) = P(-0.5 \leq Z \leq 0.5) = 0.6915 - 0.3085 = 0.3830
   \]

2. **Adaptación (5 pesos):**
   \[
   P(4.92 \leq X < 4.95) = P(-0.8 \leq Z < -0.5) = 0.3085 - 0.2119 = 0.0966
   \]
   \[
   P(5.05 < X \leq 5.08) = P(0.5 < Z \leq 0.8) = 0.7881 - 0.6915 = 0.0966
   \]
   \[
   P(\text{adaptación}) = 0.0966 + 0.0966 = 0.1932
   \]

3. **Tratamiento complicado (10 pesos):**
   \[
   P(X < 4.92) = P(Z < -0.8) = 0.2119
   \]
   \[
   P(X > 5.08) = P(Z > 0.8) = 1 - 0.7881 = 0.2119
   \]
   \[
   P(\text{complicado}) = 0.2119 + 0.2119 = 0.4238
   \]

---

### **Paso 3: Calcular la esperanza del costo**
La esperanza \(E[C]\) del costo de tratamiento se calcula como:

\[
E[C] = (1 \times P_1) + (5 \times P_5) + (10 \times P_{10})
\]

\[
E[C] = (1 \times 0.3830) + (5 \times 0.1932) + (10 \times 0.4238)
\]

\[
E[C] = 0.3830 + 0.9660 + 4.238
\]

\[
E[C] = 5.587
\]

---

### **Conclusión**
La **esperanza del costo de tratamiento** para una arandela tomada al azar es **5.59 pesos (aproximadamente)**.

