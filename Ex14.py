lado = int(input("Digite a qunatidade de lados do polígono: "))

if lado < 3:
    print("Não é um polígono")

elif lado > 5:
    print("Não foi possível indentificar")

elif lado == 3:
    print("É um triângulo")
    a = float(input("Entre com o comprimrto do lado: "))
    area = (a**2 * (3)**0.5) // 4
    print("A área é:", area)

elif lado == 4:
    print("Quadrado")
    b = float(input("Entre com o comprimrto do lado:"))
    area2 = b**2
    print("A área é:", area2)

elif lado == 5:
    print("Pentágono")
    
else:
    print("Não foi possível realizar")