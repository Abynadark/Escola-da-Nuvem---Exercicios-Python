""""
Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = Abaixo do peso

< 25: classificacao = Peso normal

 < 30: classificacao = Sobrepeso

 Para os demais cenários: classificacao =  Obeso
 """
while True:
    peso = float(input("Digite o seu peso em quilos(KG): "))
    if (0.1 < peso < 200):
        break
    print("Valor inválido! Digite um valor entre 0.1 e 200")
    
while True:
    altura = float(input("Digite a sua altura em metros: "))
    if (0.20 < altura < 2.10):
        break
    print("Valor inválido! Digite um valor entre 0.20 e 2.1") 

#obs: Coloquei o programa para aceitar valores baixos para incluir recém nascidos

imc = peso/(altura**2)

if  imc < 18.5:
    print("Você está Abaixo do Peso!") 
elif 18.5 <= imc < 25:
    print("Você está com o Peso Normal!") 
elif 25 <= imc < 30:
    print("Você está com Sobrepeso!") 
elif 30 <= imc:
    print("Você está Obeso!") 
    