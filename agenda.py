#!/usr/bin/python3

AGENDA = {}

# AGENDA['Maria'] = {
#      "telefone": "91111-1111",
#      "email": "maria@email.com",
#      "endereco": "Av. 1"
# }

# AGENDA['João'] = {
#      "telefone": "92222-2222",
#      "email": "joao@email.com",
#      "endereco": "Av. 2"
# }

def mostrarAgenda():
    if AGENDA:
        for contato in AGENDA:
            buscarContato(contato)
    else:
        print("-------------------------------------")
        print("A agenda está vazia!")
        print("-------------------------------------")

def buscarContato(contato):
    try:
        print("-------------------------------------")
        print("Nome:", contato)
        print("Telefone:", AGENDA[contato]["telefone"])
        print("E-mail:", AGENDA[contato]["email"])
        print("Endereço:", AGENDA[contato]["endereco"])
        print("-------------------------------------")
    except KeyError:
        print("-------------------------------------")
        print(f">>>>> Contato {contato} inexistente!")
        print("-------------------------------------")
    except Exception as erro:
        print("-------------------------------------")
        print(">>>>> Um erro inesperado ocorreu!")
        print(f"Detalhes: {erro}")
        print("-------------------------------------")

def lerDetalhes():
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o e-mail do contato: ")
    endereco = input("Digite o endereco do contato: ")
    return telefone, email, endereco

def incluirEditarContato(contato, telefone, email, endereco, acao):
    if acao == "incluído":
        try:
            AGENDA[contato]
            print("-------------------------------------")
            print(f">>>>> O contato {contato} já existe!")
            print("-------------------------------------")
            return None
        except:
            pass
    elif acao == "editado":
        try:
            AGENDA[contato]
            pass
        except:
            print("-------------------------------------")
            print(f">>>>> O contato {contato} não existe!")
            print("-------------------------------------")
            return None
    
    AGENDA[contato] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco
    }

    if acao != "carregado":
        print("-------------------------------------")
        print(f">>>>> Contato {contato} {acao} com sucesso!")
        print("-------------------------------------")
        salvarAgenda()

def excluirContato(contato):
    try:
        AGENDA.pop(contato)
        print("-------------------------------------")
        print(f">>>>> Contato {contato} excluido com sucesso!")
        print("-------------------------------------")
        salvarAgenda()
    except KeyError:
        print("-------------------------------------")
        print(f">>>>> Contato {contato} inexistente!")
        print("-------------------------------------")
    except Exception as erro:
        print("-------------------------------------")
        print(">>>>> Um erro inesperado ocorreu!")
        print(f"Detalhes: {erro}")
        print("-------------------------------------")

def exportarAgenda(nomeArquivo):
    try:
        with open(nomeArquivo, "w") as arquivo:
            arquivo.write("nome,telefone,e-mail,endereço\n")
            for contato in AGENDA:
                telefone = AGENDA[contato]["telefone"]
                email = AGENDA[contato]["email"]
                endereco = AGENDA[contato]["endereco"]
                sep = ","
                arquivo.write(f"{contato}{sep}{telefone}{sep}{email}{sep}{endereco}\n")
            print("-------------------------------------")
            print(">>>>> Agenda exportada com sucesso!")
            print("-------------------------------------")
    except Exception as erro:
        print("-------------------------------------")
        print(">>>>> Um erro inesperado ocorreu!")
        print(f"Detalhes: {erro}")
        print("-------------------------------------")

def importarContatos(nomeArquivo, modo):
    try:
        with open(nomeArquivo) as arquivo:
            linhas = arquivo.readlines()
            if len(linhas) == 1:
                print("-------------------------------------")
                print(">>>>> A agenda está vazia!")
                print("-------------------------------------")
            for linha in linhas:
                if linha == linhas[0]:
                    continue
                informacoes = linha.strip().split(",")
                contato = informacoes[0]
                telefone = informacoes[1]
                email = informacoes[2]
                endereco = informacoes[3]
                if modo == "menu":
                    incluirEditarContato(contato, telefone, email, endereco, "incluído")
                elif modo == "auto":
                    incluirEditarContato(contato, telefone, email, endereco, "carregado")
                    print("-------------------------------------")
                    print(">>>>> Agenda carregada com sucesso!")
                    print(f"{len(AGENDA)} registro(s) carregado(s).")
                    print("-------------------------------------")
    except FileNotFoundError:
        if modo == "auto":
            print("-------------------------------------")
            print(">>>>> A agenda está vazia!")
            print("-------------------------------------")
        else:
            print("-------------------------------------")
            print(">>>>> Arquivo não encontrado!")
            print("-------------------------------------")
    except Exception as erro:
        print("-------------------------------------")
        print(">>>>> Um erro inesperado ocorreu!")
        print(f"Detalhes: {erro}")
        print("-------------------------------------")

def salvarAgenda():
    exportarAgenda("Projetos/Agenda de Contatos/bancodedados.csv")

def carregarAgenda():
    importarContatos("Projetos/Agenda de Contatos/bancodedados.csv", "auto")

def imprimirMenu():
    print("-------------------------------------")
    print("1 - Mostrar Agenda")
    print("2 - Buscar Contato")
    print("3 - Incluir Contato")
    print("4 - Editar Contato")
    print("5 - Excluir Contato")
    print("6 - Exportar agenda para CSV")
    print("7 - Importar contatos CSV")
    print("0 - Fechar Programa")
    print("-------------------------------------")

carregarAgenda()

while True:
    imprimirMenu()
    OPCAO = input("Digite o número da opção: ")

    if OPCAO == "1":
        mostrarAgenda()
    elif OPCAO == "2":
        contato = input("Digite o nome do contato: ")
        buscarContato(contato)
    elif OPCAO == "3":
        contato = input("Digite o nome do contato: ")
        telefone, email, endereco = lerDetalhes()
        incluirEditarContato(contato, telefone, email, endereco, "incluído")
    elif OPCAO == "4":
        contato = input("Digite o nome do contato: ")
        telefone, email, endereco = lerDetalhes()
        incluirEditarContato(contato, telefone, email, endereco, "editado")
    elif OPCAO == "5":
        contato = input("Digite o nome do contato: ")
        excluirContato(contato)
    elif OPCAO == "6":
        nomeArquivo = input("Digite o nome do arquivo para exportar: ")
        exportarAgenda(nomeArquivo)
    elif OPCAO == "7":
        nomeArquivo = input("Digite o nome do arquivo para importar: ")
        importarContatos(nomeArquivo, "menu")
    elif OPCAO == "0":
        print("-------------------------------------")
        print(">>>>> Fechando o programa...")
        print("-------------------------------------")
        exit()
    else:
        print("-------------------------------------")
        print(">>>>> Opção inválida!")
        print("-------------------------------------")