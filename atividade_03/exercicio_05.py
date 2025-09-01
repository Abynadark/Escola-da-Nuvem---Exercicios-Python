"""
Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.

Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
"""

print("Verificador de Ano Bissexto")

ano = int(input("Digite um ano: "))

if (ano % 100 == 0) and (ano % 400 == 0):
    print(f"O ano {ano} é divissível por 4, 100 e 400, então é bissexto")
elif (ano % 4 == 0) and not(ano % 100 == 0):
    print(f"O ano {ano} é divissível por 4, então é bissexto")
else:
    print(f"O ano {ano} não é bissexto")