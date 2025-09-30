Queremos calcular la probabilidad de que **Viper haya ganado la primera partida**, dado que la final duró **exactamente 4 partidas**.  

---

### **Paso 1: Definir eventos**
Llamemos:
- \( H \) a una partida ganada por **Hera**.
- \( V \) a una partida ganada por **Viper**.

Sabemos que:
- **Hera gana cada partida con probabilidad** \( P(H) = 0.6 \).
- **Viper gana cada partida con probabilidad** \( P(V) = 0.4 \).
- La final dura **exactamente 4 partidas**, lo que significa que el ganador (Hera o Viper) debe haber alcanzado **3 victorias en la cuarta partida**.

Queremos calcular:

\[
P(V_1 \mid \text{final dura 4 partidas})
\]

donde \( V_1 \) denota que Viper ganó la primera partida.

---

### **Paso 2: Casos en los que la final dura 4 partidas**
La final termina en 4 partidas si alguien gana **exactamente 3 partidas** en las primeras 4. Hay dos formas en que esto sucede:
1. **Hera gana la final en 4 partidas**: La secuencia de partidas debe ser **exactamente 3 victorias para Hera y 1 para Viper**, es decir, de la forma:
   - **\( H H H V \)**
   - **\( H H V H \)**
   - **\( H V H H \)**
   - **\( V H H H \)**

   Hay **4 secuencias posibles** en las que Hera gana en la cuarta partida.

2. **Viper gana la final en 4 partidas**: Viper debe haber ganado exactamente 3 veces en las primeras 4 partidas, lo que implica:
   - **\( V V V H \)**
   - **\( V V H V \)**
   - **\( V H V V \)**
   - **\( H V V V \)**

   También hay **4 secuencias posibles** en las que Viper gana en la cuarta partida.

Por lo tanto, el evento "la final dura exactamente 4 partidas" puede ocurrir de **8 maneras** (4 en las que gana Hera, 4 en las que gana Viper).

---

### **Paso 3: Probabilidad de cada secuencia**
Cada secuencia de partidas ocurre con una probabilidad igual al producto de las probabilidades de cada partida. Como las partidas son independientes:

- La probabilidad de cada secuencia en la que **Hera gana en 4 partidas** es:

  \[
  (0.6)^3 \times (0.4) = 0.0864
  \]

- La probabilidad de cada secuencia en la que **Viper gana en 4 partidas** es:

  \[
  (0.4)^3 \times (0.6) = 0.0384
  \]

Dado que hay **4 secuencias posibles en cada caso**, la probabilidad total de que la final dure exactamente 4 partidas es:

\[
4 \times (0.0864 + 0.0384) = 4 \times 0.1248 = 0.4992
\]

---

### **Paso 4: Calcular \( P(V_1 \mid \text{final dura 4 partidas}) \)**
Queremos contar cuántas de estas secuencias empiezan con \( V_1 \) (Viper ganando la primera partida):

- Las secuencias **donde Hera gana en 4 partidas y empieza con V**:  
  - \( V H H H \) (probabilidad \( 0.0864 \)).

- Las secuencias **donde Viper gana en 4 partidas y empieza con V**:  
  - \( V V V H \) (probabilidad \( 0.0384 \)).
  - \( V V H V \) (probabilidad \( 0.0384 \)).
  - \( V H V V \) (probabilidad \( 0.0384 \)).

La probabilidad total de que la final dure 4 partidas y haya empezado con \( V_1 \) es:

\[
0.0864 + 0.0384 + 0.0384 + 0.0384 = 0.2016
\]

Finalmente, aplicamos la fórmula de probabilidad condicional:

\[
P(V_1 \mid \text{final dura 4 partidas}) = \frac{P(\text{final dura 4 partidas y } V_1)}{P(\text{final dura 4 partidas})}
\]

\[
= \frac{0.2016}{0.4992} = 0.404
\]

---

### **Resultado Final**
\[
P(V_1 \mid \text{final dura 4 partidas}) \approx 0.404
\]

Es decir, la probabilidad de que **Viper haya ganado la primera partida** dado que la final duró **exactamente 4 partidas** es **aproximadamente 40.4%**.