from ejercicio_3_diccionario import word_counter

"""4. Escribir una función que reciba una cadena de caracteres y devuelva un diccionario con cada
palabra que contiene y la cantidad de veces que aparece (frecuencia). Escribir otra función
que reciba el diccionario generado con la función anterior y devuelva una tupla con la
palabra más repetida y su frecuencia."""

def frecuency():
    chain = "password, internet, website, localhost, 404, 200, identation, 404, internet, website, 404, website, 404"
    diccionario = word_counter(chain)
    controler = 0
    llave_frecuente = ""
    for item in diccionario.keys():
        value = diccionario[item]
        if value > controler:
            controler = value
            llave_frecuente = item
    tupla = tuple([llave_frecuente, controler])
    
    return tupla
  
print(type(frecuency()))
print(frecuency())


