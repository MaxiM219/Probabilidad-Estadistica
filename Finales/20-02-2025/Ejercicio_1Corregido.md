Queremos calcular la probabilidad de que la final del torneo se haya definido en exactamente 5 partidas, dado que Viper ganó la primera partida.

---

### **Paso 1: Entender la condición del problema**
- El torneo es **al mejor de 7**: el primero en ganar 4 partidas es el campeón.
- **Hera gana con probabilidad 0.70** por partida.
- **Viper ganó la primera partida**.
- Queremos que la final se defina en **exactamente 5 partidas**. Esto significa que después de 5 partidas, uno de los jugadores ya ganó 4 veces.

---

### **Paso 2: Posibles secuencias para una final en 5 partidas**
Dado que Viper ganó la primera partida, para que la final termine en 5 partidas, hay dos escenarios posibles:

1. **Hera gana las siguientes 4 partidas consecutivas**:  
   - Secuencia: \( V, H, H, H, H \)
   - Probabilidad de esta secuencia:
     \[
     P(VH H H H) = (0.70)^4 = 0.2401.
     \]

2. **Viper gana 3 de las siguientes 4 partidas (para alcanzar 4 victorias en total)**:  
   - Posibles secuencias donde Viper alcanza 4 victorias en 5 partidas:
     - \( V, V, V, H, V \)  
     - \( V, V, H, V, V \)  
     - \( V, H, V, V, V \)  
     - \( V, V, V, V, H \)  

   - En cada caso, Viper gana 3 de las 4 partidas con probabilidad \( (0.30)^3 (0.70) \), y hay 4 formas de distribuir estas victorias:

     \[
     4 \times (0.30)^3 (0.70) = 4 \times 0.0189 = 0.0756.
     \]

---

### **Paso 3: Calcular la probabilidad total**
Sumamos las probabilidades de los dos casos:

\[
P(\text{final en 5 partidas} | \text{Viper gana la primera}) = 0.2401 + 0.0756 = 0.3157.
\]

Por lo tanto, la probabilidad de que la final se haya definido en exactamente 5 partidas, dado que Viper ganó la primera, es **0.3157 (31.57%)**.