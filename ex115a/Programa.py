from lib import interface, cor
from time import sleep

while True:
    resposta = interface.menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        interface.cabecalho('Opção 1')
        sleep(2)
    elif resposta == 2:
        interface.cabecalho('Opção 2')
        sleep(2)
    elif resposta == 3:
        interface.cabecalho('Finalizando Sistema... Até logo!')
        break
    else:
        print(cor.vermelho('ERRO! Por favor escolha uma opção valida!'))
        sleep(2)
