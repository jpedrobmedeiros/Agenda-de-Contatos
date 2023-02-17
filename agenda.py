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

def buscarContato(contato):
    print("-------------------------------------")
    print("Nome:", contato)
    print("Telefone:", AGENDA[contato]["telefone"])
    print("E-mail:", AGENDA[contato]["email"])
    print("Endereço:", AGENDA[contato]["endereco"])
    print("-------------------------------------")

def incluirEditarContato(contato, telefone, email, endereco):
    AGENDA[contato] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco
    }
    print("-------------------------------------")
    print(f">>>>> Contato {contato} adicionado/editado com sucesso!")
    print("-------------------------------------")

def excluirContato(contato):
    AGENDA.pop(contato)
    print("-------------------------------------")
    print(f">>>>> Contato {contato} excluido com sucesso!")
    print("-------------------------------------")

def imprimirMenu():
    print("-------------------------------------")
    print("1 - Mostrar Agenda")
    print("2 - Buscar Contato")
    print("3 - Incluir Contato")
    print("4 - Editar Contato")
    print("5 - Excluir Contato")
    print("0 - Fechar Programa")
    print("-------------------------------------")

while True:
    imprimirMenu()
    OPCAO = input("Digite o número da opção: ")

    if OPCAO == "1":
        mostrarAgenda()
    elif OPCAO == "2":
        contato = input("Digite o nome do contato: ")
        buscarContato(contato)
    elif OPCAO == "3" or OPCAO == "4":
        contato = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o e-mail do contato: ")
        endereco = input("Digite o endereco do contato: ")
        incluirEditarContato(contato, telefone, email, endereco)
    elif OPCAO == "5":
        contato = input("Digite o nome do contato: ")
        excluirContato(contato)
    elif OPCAO == "0":
        print("-------------------------------------")
        print(">>>>> Fechando o programa...")
        print("-------------------------------------")
        exit()
    else:
        print("-------------------------------------")
        print(">>>>> Opção inválida!")
        print("-------------------------------------")