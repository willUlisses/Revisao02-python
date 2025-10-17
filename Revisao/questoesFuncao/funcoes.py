from funcoes_bolsa import verifica_valor

#primeira questão 

def autenticador(email, senha):
    return email == "email" and senha == "senha"


#segunda questão

def aplica_desconto(preco):
    return preco - (preco * 0.1)

#terceira questão

valor = float(input("Digite um valor de ação para ser verificado: "))

print(verifica_valor(valor))

#quarta questão

def verifica_idade(idade):
    return "Maior de idade" if idade >= 18 else "Menor de idade"


