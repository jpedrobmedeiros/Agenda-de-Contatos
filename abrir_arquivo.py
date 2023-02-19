#!/usr/bin/python3

try:
    with open("Projetos/Agenda de Contatos/emails.txt") as arquivo:
        for line in arquivo.readlines():
            print(line.strip())
except FileNotFoundError:
    print("Arquivo não encontrado!")
except Exception as erro:
    print("Um erro inesperado ocorreu!")
    print(f"Detalhes: {erro}")