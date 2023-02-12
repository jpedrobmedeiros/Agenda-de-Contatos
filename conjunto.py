#!/usr/bin/python3

# O conjunto não permite que um valor se repita em seu conteúdo
conjunto = {"melão", "manga", "graviola"}

conjunto.add("jaca")
conjunto.add("manga")

for fruta in conjunto:
    print(fruta)