import datetime
from database.processosdb import processos, processo


data = str(datetime.datetime.now())


def verificar_existencia_bd():
    pass
    

def adicionar_processo(numero, letra, accao, autor, reu, escrivao, juiz, sala, estado, data_entrada):
    
    processo["numero"]= numero
    processo["letra"]= letra
    processo["accao"]= accao
    processo["autor"]= autor
    processo["reu"]= reu
    processo["escrivao"]= escrivao
    processo["juiz"]= juiz
    processo["sala"]= sala
    processo["estado"]= estado
    processo["data_entrada"]= data_entrada
    processo["data_criacao"]= data
    processos.append(processo)
    print('PROCESSO ADICIONADO COM SUCESSO') 

