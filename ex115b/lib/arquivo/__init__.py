from ex115b.lib import leia, cor, interface


def verificar(nome='cadastro.txt'):
    try:
        arquivo = open('cadastro.txt', 'rt')
        arquivo.close()
    except FileNotFoundError:
        arquivo = open(nome, 'a')
        print(f'O arquivo "{nome}" foi criado com sucesso!')


def visualizar(nome='cadastro.txt'):
    interface.cabecalho('Cadastrados')
    try:
        arquivo = open(nome, 'r')
    except FileNotFoundError:
        print(cor.vermelho('ERRO! Arquivo não encontrado'))
    else:
        for linha in arquivo.readlines():
            linha = linha.replace('\n', '')
            linha = linha.split(';')
            print(f'{linha[0]:<30}{linha[1]} anos')


def cadastrar(nome='cadastro.txt'):
    arquivo = open(nome, 'a')
    interface.cabecalho('Cadastrar nova Pessoa')
    nome = leia.LeiaNome('Nome: ')
    idade = leia.LeiaInt('Idade: ')
    arquivo.write(f'{nome};{idade}\n')
    arquivo.close()
    print(f'{cor.verde("Cadastro realizado com sucesso!")}')
