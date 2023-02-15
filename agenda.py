#!/usr/bin/python3

AGENDA = {}

AGENDA['Maria'] = {
    "telefone": "91111-1111",
    "email": "maria@email.com",
    "endereco": "Av. 1"
}

AGENDA['João'] = {
    "telefone": "92222-2222",
    "email": "joao@email.com",
    "endereco": "Av. 2"
}

def mostrarAgenda():
    for contato in AGENDA:
        buscarContato(contato)
        print("-----------------------------")

def buscarContato(contato):
    print("Nome:", contato)
    print("Telefone:", AGENDA[contato]["telefone"])
    print("E-mail:", AGENDA[contato]["email"])
    print("Endereço:", AGENDA[contato]["endereco"])

#mostrarAgenda()
buscarContato("João")