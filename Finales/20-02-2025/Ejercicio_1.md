Queremos calcular la probabilidad de que la final de un **mejor de 7** entre Hera y Viper haya durado **exactamente 5 partidas**, dado que **Viper ganó la primera partida**.

---

### **Paso 1: Definir eventos**
Llamemos:
- \( H \) a una partida ganada por **Hera**.
- \( V \) a una partida ganada por **Viper**.

Sabemos que:
- **Hera gana cada partida con probabilidad** \( P(H) = 0.7 \).
- **Viper gana cada partida con probabilidad** \( P(V) = 0.3 \).
- La final dura **exactamente 5 partidas**, lo que significa que alguien alcanzó **4 victorias en la quinta partida**.

Queremos calcular:

\[
P(\text{Final dura 5 partidas} \mid V_1)
\]

---

### **Paso 2: Casos en los que la final dura 5 partidas**
Para que la final termine en la **quinta partida**, el ganador (Hera o Viper) debe haber alcanzado **4 victorias en 5 juegos**. Dado que **Viper ganó la primera partida**, los posibles escenarios en los que esto sucede son:

1. **Hera gana la final en 5 partidas**:  
   - La secuencia debe ser **exactamente 4 victorias para Hera y 1 para Viper**.  
   - Como ya sabemos que la primera la ganó Viper, la única posibilidad es:

     \[
     V H H H H
     \]

2. **Viper gana la final en 5 partidas**:  
   - La secuencia debe ser **exactamente 4 victorias para Viper y 1 para Hera**.  
   - La única posibilidad es:

     \[
     V V V V H
     \]

---

### **Paso 3: Probabilidad de cada secuencia**
Cada secuencia ocurre con una probabilidad igual al producto de las probabilidades de cada partida. Como las partidas son independientes:

- **Para \( V H H H H \) (Hera gana la final en 5 partidas)**:

  \[
  P(V H H H H) = (0.3) (0.7) (0.7) (0.7) (0.7) = 0.0720
  \]

- **Para \( V V V V H \) (Viper gana la final en 5 partidas)**:

  \[
  P(V V V V H) = (0.3) (0.3) (0.3) (0.3) (0.7) = 0.00567
  \]

Por lo que la probabilidad total de que la final dure **exactamente 5 partidas** dado que **Viper ganó la primera** es:

\[
P(\text{Final dura 5 partidas} \mid V_1) = P(V H H H H) + P(V V V V H)
\]

\[
= 0.0720 + 0.00567 = 0.07767
\]

---

### **Resultado Final**
\[
P(\text{Final dura exactamente 5 partidas} \mid V_1) \approx 0.0777
\]

Es decir, la **probabilidad es aproximadamente 7.77%**.