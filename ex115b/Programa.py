from lib import interface, cor, arquivo
from time import sleep

#Verifica se o arquivo ja existe
arquivo.verificar('cadastro.txt')
while True:
    resposta = interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        #Visualizar cadastros
        arquivo.visualizar()
        sleep(2)
    elif resposta == 2:
        #Criar novo cadastro
        arquivo.cadastrar()
        sleep(2)
    elif resposta == 3:
        #Finalizar programa
        interface.cabecalho('Finalizando Sistema... Até logo!')
        break
    else:
        print(cor.vermelho('ERRO! Por favor escolha uma opção valida!'))
        sleep(2)
