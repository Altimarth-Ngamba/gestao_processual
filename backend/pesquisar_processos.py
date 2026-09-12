from database.processosdb import processos


def pesquisar_processo(pesquisa):

    for processo in processos:

        if (
            pesquisa == processo["numero"]
            or pesquisa == processo["accao"]
            or pesquisa == processo["autor"]
            or pesquisa == processo["reu"]
        ):
            return processo

    return None
    
    
