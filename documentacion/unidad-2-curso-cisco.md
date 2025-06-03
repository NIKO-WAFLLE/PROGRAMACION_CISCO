# seguna unidad curso phyton

## La función print()

> Observa la línea de código de abajo:


```py
print("¡Hola, Mundo!")
 ```
La palabra ```print ```que puedes ver aquí es el nombre de una función. Eso no significa que dondequiera que aparezca esta palabra, será siempre el nombre de una función. El significado de la palabra proviene del contexto en el cual se haya utilizado la palabra.

Probablemente hayas encontrado el término función muchas veces antes, durante las clases de matemáticas. Probablemente también puedes recordar varios nombres de funciones matemáticas, como seno o logaritmo.

Las funciones de Python, sin embargo, son más flexibles y pueden contener más que sus parientes matemáticos.

Una función (en este contexto) es una parte separada del código de computadora el cual es capaz de:

causar algún efecto (por ejemplo, enviar texto a la terminal, crear un archivo, dibujar una imagen, reproducir un sonido, etc.); esto es algo completamente inaudito en el mundo de las matemáticas.
evaluar un valor (por ejemplo, la raíz cuadrada de un valor o la longitud de un texto dado) y devolverlo como el resultado de la función; esto es lo que hace que las funciones de Python sean parientes de los conceptos matemáticos.
Además, muchas de las funciones de Python pueden hacer las dos cosas anteriores juntas.

## La función print() y su efecto, argumentos, y valores retornados

El efecto es muy útil y muy espectacular. La función:

1. toma sus argumentos (puede aceptar más de un argumento y también puede aceptar menos de un argumento)

1. los convierte a un formato legible si es necesario (como puedes sospechar, las cadenas no requieren esta acción, ya que la cadena ya es legible)

1. y envía los datos resultantes al dispositivo de salida (normalmente la consola); en otras palabras, todo lo que pongas en la función print() se aparecerá en tu pantalla.

> notas raras 

para hacer un salto de linea o un espacio se puede colocar un ``` print() ``` entre otros print 

 ![ejemplo](../IMG/Captura%20de%20pantalla%202025-06-02%20034627.png)

  la invocación vacía de ```print()``` no está tan vacía como podrías haber esperado - genera una línea vacía o (esta interpretación también es correcta) genera una nuevalínea.


  ## Caracteres de escape y nueva línea en Python
   
```py
print("\n")
```

La barra invertida (\\) tiene un significado muy especial cuando se usa dentro de cadenas - se llama carácter de escape.

La palabra escape debe entenderse específicamente - significa que la serie de caracteres en la cadena se escapa por un momento (un momento muy breve) para introducir una inclusión especial.

En En otras palabras, la barra invertida no significa nada en sí misma, sino que es solo una especie de anuncio de que el siguiente carácter después de la barra invertida también tiene un significado diferente.

La la letra n colocada después de la barra invertida proviene de la palabra newline.

Tanto la barra invertida como n forman un símbolo especial llamado un carácter de nuevalínea, que insta a la consola a iniciar una nuevalínea de salida.

> notas raras

para mostar solo un "\\" en el print hay que colocar dos "\\\\" si solo que soloca uno esto marcara error en la terminal

## usando multiples argumentos 

```py 
print("La Witsi Witsi Araña" , "subió" , "a su telaraña.")
```
Hay una invocación de la función print(), pero contiene tres argumentos. Todos ellos son cadenas.

Los argumentos están separados por comas. Los hemos rodeado de espacios para hacerlos más visibles, pero no es realmente necesario, y no lo haremos más.

En este caso, las comas al separar los argumentos juega un papel completamente diferente al de la coma dentro de la cadena. El primero es parte de la sintaxis de Python, mientras que el segundo está diseñado para mostrarse en la consola.

1. La función print() invocada con más de un argumento los muestra todos en una sola línea.
1. La función print() pone un espacio entre los argumentos de salida por iniciativa propia.

### Argumentos posicionales 

La forma en que estamos pasando los argumentos a la función print() es la más común en Python, y se llama la forma posicional. Este nombre proviene del hecho de que el significado del argumento está dictado por su posición (por ejemplo, el segundo argumento se mostrará después del primero, no al revés).


