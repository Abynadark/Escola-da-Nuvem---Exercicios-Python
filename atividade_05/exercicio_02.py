"""
Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). 
Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""

import string

def verificar_palindromo(texto):
    
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

frase = input("Digite uma palavra ou frase: ")
resultado = verificar_palindromo(frase)
print(f"É palíndromo? {resultado}")
