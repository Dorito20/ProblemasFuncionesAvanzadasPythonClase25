#Deber: Mejora el analizador de sentimientos para manejar oraciones con múltiples emociones, asignando diferentes ponderaciones a las palabras según su intensidad (por ejemplo, "genial" podría tener más peso que "bien").

# Diccionario de puntuaciones para palabras positivas y negativas
puntuaciones_positivas = {
    "bien": 1,
    "genial": 2,
    "fantástico": 3,
    "excelente": 3,
    "feliz": 2
}

puntuaciones_negativas = {
    "mal": 1,
    "terrible": 2,
    "horrible": 3,
    "malo": 2,
    "triste": 2
}

def analizar_sentimiento(texto):
    texto = texto.lower()
    puntuacion_total = 0
    
    # Calcular puntuación total positiva
    for palabra, puntuacion in puntuaciones_positivas.items():
        if palabra in texto:
            puntuacion_total += puntuacion * texto.count(palabra)
    
    # Calcular puntuación total negativa
    for palabra, puntuacion in puntuaciones_negativas.items():
        if palabra in texto:
            puntuacion_total -= puntuacion * texto.count(palabra)
    
    # Determinar el sentimiento basado en la puntuación total
    if puntuacion_total > 0:
        return "Sentimiento positivo"
    elif puntuacion_total < 0:
        return "Sentimiento negativo"
    else:
        return "Sentimiento neutral"

# Ejemplo de uso
texto = input("Escribe una oración para analizar: ")
resultado = analizar_sentimiento(texto)
print(f"El resultado del análisis es: {resultado}")
