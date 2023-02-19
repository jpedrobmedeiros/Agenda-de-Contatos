#!/usr/bin/python3

try:
    with open("Projetos/Agenda de Contatos/nomes.txt", "a+") as arquivo:
        print("Estado anterior do arquivo:")
        arquivo.write("Ingrid Kelly\n")
        # É preciso voltar o ponteiro do arquivo para o inicio para fazer a leitura
        # O ponteiro serve tanto para ler quanto para escrever no arquivo
        # A dinâmica do ponteiro é essencial para utilizar os modos com o +
        arquivo.seek(0)
        print(arquivo.read())
        print("========================\n")
        print("Estado Atual do arquivo:")
        arquivo.seek(0, 2)
        arquivo.write("João Pedro\n")
        arquivo.seek(0)
        print(arquivo.read())
except Exception as erro:
    print("Um erro inesperado ocorreu!")
    print(f"Detalhes: {erro}")