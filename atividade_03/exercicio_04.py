"""
Conversor de Temperatura 

Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

print("----------Conversor de Temperatura----------")

temperatura = float(input("Informe o valor da temperatura: "))

print("-----MENU----- \n1- Celsius \n2-Fahrenheit \n3-Kelvin")
unid_inicial = int(input("Com base no menu, informe o número correspondente a unidade de origem: "))
unid_convertida = int(input("Com base no menu, informe o número correspondente a unidade para qual você deseja converter: "))

if (unid_inicial == 1 and unid_convertida == 2): #Celsius para Fahrenheit
    temp_convertida = (9/5)*temperatura + 32
elif (unid_inicial == 1 and unid_convertida == 3): #Celsius para Kelvin
    temp_convertida = temperatura + 273.15
elif (unid_inicial == 2 and unid_convertida == 1): #Fahrenheit para Celsius
    temp_convertida = (5/9)*(temperatura - 32)
elif (unid_inicial == 2 and unid_convertida == 3): #Fahrenheit para Kelvin
    temp_convertida = (5/9)*(temperatura-32) + 273.15
elif (unid_inicial == 3 and unid_convertida == 1): # Kelvin para Celsius
    temp_convertida = temperatura - 273.15
elif (unid_inicial == 3 and unid_convertida == 2): # Kelvin para Fahrenheit
    temp_convertida = (9/5)*(temperatura - 273.15) + 32
    
print(f"O valor da temperatura convertida é {temp_convertida:.2f}")
    