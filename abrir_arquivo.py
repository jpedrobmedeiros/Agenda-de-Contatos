#!/usr/bin/python3

with open("Projetos/Agenda de Contatos/emails.txt") as arquivo:
    for line in arquivo.readlines():
        print(line.strip())