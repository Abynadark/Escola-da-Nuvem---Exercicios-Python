#Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.

def idade_em_dias(ano_nascimento, ano_atual=None):

    from datetime import date
    if ano_atual is None:
        ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    return idade_anos * 365 

ano_nasc = int(input("Digite seu ano de nascimento: "))
dias = idade_em_dias(ano_nasc)
print(f"Sua idade aproximada em dias: {dias} dias")


