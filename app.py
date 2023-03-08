def aOctal():
    decimal = int(input('ingresa un número decimal -> '))
    octal = oct(decimal)
    print(f'el numero {decimal} corresponde al numero {octal} en sistema octal')

def aBinario():
    decimal = int(input('ingresa un número decimal -> '))
    binario = bin(decimal)
    print(f'el numero {decimal} corresponde al numero {binario} en sistema binario')

def aHexadecimal():
    decimal = int(input('ingresa un número decimal -> '))
    hexadecimal = hex(decimal)
    print(f'el numero {decimal} corresponde al numero {hexadecimal} en sistema hexadecimal')

switcher = {
    0:aOctal,
    1:aBinario,
    2:aHexadecimal
    
}

opcion = int(input("""Ingresa una opción:
0 convierte un numero decimal a Octal
1 convierte un numero decimal a Binario
2 convierte un numero decimal a Hexadecimal
--> """))

funcion = switcher.get(opcion)
funcion()
