numeros=[1,2,30,4,51]
for numero in numeros:
    cuadrado=numero**2
    print(f"el cuadrado de {numero} es {cuadrado}")

print(numeros[4])

#tratamiento de cadenas
nombre="marcos"
apellido="mendoza"
frase="hola esta es una frase"

longitud=len(frase)
print(longitud) 

apellido="mendoza"
frace="Hola esta es una frase"
longitud=len(frase)
print(longitud)
print(apellido[5])

palabras = frace.split()
print(palabras)
print(palabras[0])
palabras[1] = "chau"

print(palabras)

mayusculas= frace.upper()
print(mayusculas)
minusculas = frace.lower()
print(minusculas)

VALORES = [2,4,50,36]
VALORES.append(8)
print(VALORES)
del valores [2]
perosnas= {
    "persona1":{"nombre" :"juan",
                "edad":30, 
                "ciudad":"maadrid"},
         "persona 2":{"nombre":"maria","edad":28,"ciudad":"barcelona"}}

datos= personas^["persona1"]
datos2=personas["persona2"]
print(datos)
print(datos2)
print(datos2["edad"])

#recorrer un dict
for key,value in personas,item():
    print(f"clave:{key}")
    print(f"nombre:{value['nombre']},edad:{value['edad']},ciudad:{value['ciudad']}"