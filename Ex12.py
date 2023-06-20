altura = float(input("Digite a sua altura: "))
sexo = int(input( "1- Feminino e 2- Masculino: "))

if sexo == 1:
   x = 62.1 * altura - 44.7
   print("Seu peso ideal é:", x)

if sexo == 2:
    y = 72.7 * altura - 58
    print("Seu peso ideal é:", y)

else:
    ("Sexo indefinido")