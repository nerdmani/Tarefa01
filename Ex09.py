a1 = int(input("Digite o valor inicial: "))
q = int(input("Digite a razão (sendo esta maior ou igual a 2): "))
n = int(input("Digite o números de termos: "))

if q >= 2:
    Sn =a1*(q**n -1) / (q-1)
    print("O resultado da soma dos termos da PG é", Sn)

else: 
    print("Não foi possível realizar a conta, reveja o valor da razão")
