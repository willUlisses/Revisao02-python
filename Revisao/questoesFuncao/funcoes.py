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

#quinta questão

def calcula_imc(peso, altura):
    return (peso/(altura**2))

def classifica_imc(valor_imc):
    if valor_imc  >= 25:
        print("Acima do peso")
    elif valor_imc < 18.5:
        print("Abaixo do peso")
    else:
        print("Peso normal")


imc = calcula_imc(67, 1.70)
classifica_imc(imc)


# sexta questão

def calcula_imposto(preco):
    return preco + (preco * 0.15)


