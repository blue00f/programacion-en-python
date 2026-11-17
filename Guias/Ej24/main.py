import numpy as np

class PerceptronMulticapa:
    def __init__(self, tamanio_entrada, tamanio_oculto, tamanio_salida=1, tasa_aprendizaje=1.0):
        self.tasa_aprendizaje = tasa_aprendizaje
        self.pesos = np.random.randn(tamanio_entrada, tamanio_oculto)
        self.sesgos = np.zeros((1, tamanio_oculto))
        self.pesos_salida = np.random.randn(tamanio_oculto, tamanio_salida)
        self.sesgos_salida = np.zeros((1, tamanio_salida))

    def _sigmoide(self, x):
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))

    def _derivada_sigmoide(self, sig):
        return sig * (1 - sig)

    def entrenar(self, entradas, salidas_esperadas, epocas=500):
        numero_muestras = entradas.shape[0]
        
        for epoca in range(epocas):
            z_oculto = np.dot(entradas, self.pesos) + self.sesgos
            a_oculto = self._sigmoide(z_oculto)
            z_salida = np.dot(a_oculto, self.pesos_salida) + self.sesgos_salida
            salidas = self._sigmoide(z_salida)

            error = salidas_esperadas - salidas
            d_salida = error * self._derivada_sigmoide(salidas)
            
            error_oculto = d_salida.dot(self.pesos_salida.T)
            d_oculto = error_oculto * self._derivada_sigmoide(a_oculto)

            self.pesos_salida += (a_oculto.T.dot(d_salida) / numero_muestras) * self.tasa_aprendizaje
            self.sesgos_salida += (np.sum(d_salida, axis=0, keepdims=True) / numero_muestras) * self.tasa_aprendizaje
            self.pesos += (entradas.T.dot(d_oculto) / numero_muestras) * self.tasa_aprendizaje
            self.sesgos += (np.sum(d_oculto, axis=0, keepdims=True) / numero_muestras) * self.tasa_aprendizaje

    def predecir(self, entradas):
        z_oculto = np.dot(entradas, self.pesos) + self.sesgos
        a_oculto = self._sigmoide(z_oculto)
        z_salida = np.dot(a_oculto, self.pesos_salida) + self.sesgos_salida
        return self._sigmoide(z_salida)

np.random.seed(42)
cantidad_datos = 200

entradas_masivas = np.random.rand(cantidad_datos, 2)
salidas_esperadas_masivas = ((entradas_masivas[:, 0] + entradas_masivas[:, 1]) > 1).astype(int).reshape(-1, 1)

perceptron = PerceptronMulticapa(tamanio_entrada=2, tamanio_oculto=4, tamanio_salida=1, tasa_aprendizaje=1.0)

print(f"=== ENTRENAMIENTO CON {cantidad_datos} REGISTROS ===")
perceptron.entrenar(entradas_masivas, salidas_esperadas_masivas, epocas=2000)

predicciones = perceptron.predecir(entradas_masivas)
predicciones_binarias = (predicciones >= 0.5).astype(int)
precision = np.mean(predicciones_binarias == salidas_esperadas_masivas) * 100

print("\n--- RESULTADOS POR CADA DATO ---")
for i in range(cantidad_datos):
    print(f"  Entrada: [{entradas_masivas[i][0]:.2f}, {entradas_masivas[i][1]:.2f}] -> Esperado: {salidas_esperadas_masivas[i][0]} | Predicción: {predicciones[i][0]:.4f} (Redondeado: {predicciones_binarias[i][0]})")

print(f"\nPrecisión total en los datos: {precision:.2f}%")