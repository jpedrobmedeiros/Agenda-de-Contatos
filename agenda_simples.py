#!/usr/bin/python3

dicionario = {
    "joão": {
        "telefone": "90000-1111",
        "e-mail": "joao@email.com",
        "endereço": "Rua primeira vez"
    },
    "josé": {
        "telefone": "92222-3333",
        "e-mail": "jose@email.com",
        "endereço": "Rua segunda vez"
    },
    "maria": {
        "telefone": "94444-5555",
        "e-mail": "maria@email.com",
        "endereço": "Av. Tercerira vez"
    }
}

dicionario["andré"] = {
    "telefone": "96666-7777",
    "e-mail": "andre@email.com",
    "endereço": "Av. Quarta vez"
}

dicionario.pop("joão")

for pessoa in dicionario:
    print(pessoa, dicionario[pessoa])