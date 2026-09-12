import datetime
from banco_de_dados.dados import processos


def buscar_por_trimestre( mes_inicial, mes_final):
    encontrados = []

    for processo in processos:
        mes = processo["data_criacao"].month

        if mes_inicial <= mes <= mes_final:
            encontrados.append(processo)

    return encontrados
    
def buscar_por_semestre( mes_inicial, mes_final):
    encontrados = []

    for processo in processos:
        mes = processo["data_criacao"].month

        if mes_inicial <= mes <= mes_final:
            encontrados.append(processo)

    return encontrados
     
'''
#suponhamos que dentro do programa eu chame o erceiro

if navegacao == '3':
    resultado = buscar_por_periodo(7, 9)

    for processo in resultado:
        print(processo)
'''

