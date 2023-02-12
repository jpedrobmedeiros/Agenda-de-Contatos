#!/usr/bin/python3

# Dicionários usam um sistema de chave : valor
dicionario = {
    "melão" : "Uma fruta muito boa quando está na época certa",
    "manga" : "Uma fruta muito boa e diversa",
    "graviola" : "Não julgue pela aparência"
}

for fruta in dicionario:
    print(fruta, "possui o valor", f"\"{dicionario[fruta]}\"")