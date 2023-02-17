#!/usr/bin/python3

# Erro em tempo de compilação
# SyntaxError
# while True
#     print("Olá Mundo!")

# Erro em tempo de execução
# ZeroDivisionError
# print(2 / 0)

# Erro de lógica
#função exercendo uma operação diferente do seu propósito
#def dividir(a, b):
#    print(a * b)

#dividir(2, 2)

def dividir(a, b):
    try:
        print(a / b)
    except Exception as e:
        print("Divisão inválida!")
        print(e)

dividir(2, "a")