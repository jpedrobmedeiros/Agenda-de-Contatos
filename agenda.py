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

def incluirEditarContato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco
    }
    print(f">>>>> Contato {contato} adicionado/editado com sucesso!")

mostrarAgenda()
incluirEditarContato("Paulo", "93333-3333", "paulo@email.com", "Av. 3")
incluirEditarContato("João", "93333-4444", "jp@email.com", "Av. 2")
incluirEditarContato("José", None, None, "Av. 4")
mostrarAgenda()