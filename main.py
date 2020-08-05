#!/usr/bin/env python3
"""
Sudoku - Codificação paara resoução do Sudoku usando a lógica
do algorirmo de busca em largura.
Autores : Gustavo Zanatta Bruno e Guilherme F. S. Camnpos
Repositório: https://github.com/zanattabruno/sudoku-ia-unisinos
"""
import sys
import time
import numpy
import busca_largura
import entrada_saida as e_s

def busca_em_largura():
    print('Resolvendo com a busca em largura...')
    t1 = time.time()
    result = numpy.asarray(busca_largura.resolve_sudoku_busca_largura(sudoku.tolist()), dtype=numpy.int32)
    s = busca_largura.get_passos()
    e_s.imprime_quadro(result, time.time() - t1, s)

sudoku = e_s.coverte_txt_to_array('entrada.txt')

while True:
    print("Opções de algoritmos para resolver o SUDOKU:")
    print("1- Implemetação baseada no algoritmo de Busca em Largura")
    print("2- Busca ...")
    print("3- Todos")
    print("0- Sair")
    try:
        option = int(input("Enter a number: "))
        if option < 0 or option > 5:
            raise Exception
    except:
        continue

    if option == 1:
        busca_em_largura()
    elif option == 2:
        pass
    elif option == 3:
        busca_em_largura()
    elif option == 0:
        sys.exit(0)