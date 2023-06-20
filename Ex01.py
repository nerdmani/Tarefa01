#Escreva um programa que leia 3 notas de um aluno e a média das notas dos exercícios realizados por ele. Calcular a média de aproveitamento, usando a fórmula:
#MA = (N1 + N2*2 + N3*3 + ME)/7. A
#partir da média, informar o conceito de acordo com os itens abaixo:
#maior ou igual a 9
#menor que 4



N1 = int(input("Porfavor insira a primeira nota: "))
N2 = int(input("Por favor inisira a segunda nota: "))
N3 = int(input("Por favor insira a terciera nota: "))
ME = float(input("Por fravor digite a média das notas: "))


MA = (N1 + N2*2 + N3 *3 + ME) // 7

if MA >= 9 :    
    print("A média de aproveitamento foi maior ou igual a 9")

else:
    print("A média de aproveitamento foi maior que 4")

if MA < 4 :
    print("A média de aproveitamento foi menor que 4")


