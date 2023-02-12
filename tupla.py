#!/usr/bin/python3

# A tupla eh imutavel
tupla = ("verde", "azul", "vermelho", "verde")

for cor in tupla:
    print(cor)

print(f"A palavra \"verde\" existe {tupla.count('verde')}")