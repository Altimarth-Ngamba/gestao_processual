#SISTEMA DE GESTAO PROCESSUAL

##OBJECTIVOS
    Desenvolver um sistema para gerenciar processos, estatisticas, funcionarios do cartorio, para subtituir o contro manual e de planilhas.

##USUARIOS DO SISTEMA

    * Administrador
    * Funcionarios do cartorio

##PROBLEMAS IDENTIFICADOS
    * Demora para localizar processos
    * Demora para fazr mapas estatisticos
    * Pouco control dos processos
    * Risco de perda de dados
    * Problama na hora da consulta de procesos

##REQUISITOS FUNCIONAIS
    *RF01 - Cadastrar Funcionários
    *RF02 - Excluir Funcionários
    *RF03 - Editar Funcionários
    *RF04 - Cadastar Processos
    *RF05 - Editar Processos
    *RF06 - Excluir Processos
    *RF07 - PESQUISAR PROCESSOS
    *RF08 - Criar Mapa estatistico
    *RF09 - Mostrar Lista de Processos

##REQUISITOS NAO FUNCIONAIS
    *RNF01 - O sistema deve possuir autenticação (Processos, Funcionarios, Alterações)
    *RNF02 - O sistema deve funcionar em computadores
    *RNF03 - O Tempo de resposta deve ser de 03 segundos
    *RNF04 - Os dados devem ter backup perodicos
    *RNF05 - Apenas funcionarios autorizados poderão ter  acesso a cetas funcionalidades
    
##REGRAS DE NÉGOCIO
    *RN - Cada funcionario deve ter uma unica conta
    *RN - Cada processo deve ter os dados unicos
    *RN - Apenas Administradores devem excluir funcionarios, visualizar lista de processos, e criar mapas gerais
    *RN - Apenas funcionarios devem excluir e criar processos

##DUVIDAS PARA O CLIETE