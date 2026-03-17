# Programa Principal

from funciones_habitos import analizar_habitos
from funciones_habitos import registrar_habitos

lista_habitos = registrar_habitos()

resultados_analisis = analizar_habitos(lista_habitos)

print("\nResultados de los análisis de la lista de hábitos:\nHábito | Frecuencia")

for habito in resultados_analisis.keys():
    frecuencia = resultados_analisis[habito]
    print(f"{habito}: {frecuencia}")
    
