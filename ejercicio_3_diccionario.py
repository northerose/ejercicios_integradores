"""3. Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con
cada palabra que contiene (como llave) y la cantidad de veces que aparece (como valor)(frecuencia)."""




def word_counter(chain_string):
    words = {}
    for element in chain_string.split(', '):
        result = words.get(element)
        if result:
            words[element] += 1
        else:
            words[element] = 1
    return words

chain = "password, internet, website, localhost, 404, 200, identation, 404, internet, website, 404, website, 404"
print(word_counter(chain))