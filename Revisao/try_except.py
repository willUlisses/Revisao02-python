#primeira questão

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

try:
    print(num1 / num2)
except ZeroDivisionError:
    print("Você não pode dividir por zero meu patrão")


# segunda questão

try:
    numero = int(input("Digite um número qualquer: "))
    print(f"você digitou o número {numero}")
except ValueError:
    print("Você deve digitar apenas números")


# terceira questão

try:
    primeiro_valor = int(input("Digite o primeiro valor: "))
    segundo_valor = int(input("Digite o segundo valor: "))
    print(primeiro_valor / segundo_valor)
except ValueError:
    print("Você deve digitar apenas números meu chapa")
except ZeroDivisionError:
    print("Não é possível dividir por zero")


# quarta questão

def dividir(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "[ERROR]: Não é possível realizar divisões por zero"
    
print(dividir(10,0))

    
