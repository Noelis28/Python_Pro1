# Creamos un diccionario llamado meme_dict que contiene palabras modernas como claves
# y sus definiciones como valores

meme_dict = {
    "LOL": "Una respuesta común a algo gracioso",
    "CRINGE": "Algo excepcionalmente raro o embarazoso",
    "ROFL": "Una respuesta a una broma",
    "SHEESH": "Ligera desaprobación",
    "CREEPY": "Aterrador, siniestro",
    "AGGRO": "Ponerse agresivo/enojado",
    "GOAT": "Se usa para describir a alguien extremadamente bueno en algo",
    "VIBES": "Sensación o energía que transmite una situación, persona o lugar",
    "FIAO": " También puede referirse a un crédito o préstamo sin interés.",
    "CHANTÍN": "Casa o hogar, lugar donde alguien vive.",
    "BOCHINCHE": "Chisme o cotorreo, conversación de cosas triviales o rumores."
}

# Imprime un mensaje de bienvenida al usuario
print("¡Bienvenido al Diccionario de Palabras Modernas!")
# Instrucciones para el usuario
print("Este programa te ayudará a entender palabras modernas utilizadas en internet.")
print("Puedes escribir hasta 5 palabras, y te daremos su significado.")

# Bucle que se repite 5 veces para que el usuario pueda ingresar 5 palabras
for _ in range(5):
    # Solicita al usuario que escriba una palabra (en mayúsculas)
    word = input("Escribe las palabras que no entiendas (¡con mayúsculas!): ")

    if word in meme_dict.keys():
         # Si está, imprime la palabra y su definición
        print(f"{word}: {meme_dict[word]}")
    else: 
        # Si no está, muestra un mensaje indicando que no se encontró
        print(f"Lo siento, no encontramos '{word}' en el diccionario.")
    
    print()  

# Mensaje final del programa
print("¡Gracias por usar el Diccionario de Palabras Modernas!")
