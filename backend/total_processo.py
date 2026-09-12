from banco_de_dados.dados import processos

def total_processos ():
    
    for processo in processos:
        
        total = len(processo)
    print (f'Total de processos: {total}')