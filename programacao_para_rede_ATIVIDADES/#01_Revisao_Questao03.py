import os
import zipfile

def descompactar_arquivo(arquivo_zip, pasta_destino):
    if os.path.exists(arquivo_zip):
        with zipfile.ZipFile(arquivo_zip, 'r') as zip_ref:
            zip_ref.extractall(pasta_destino)
        return True
    else:
        print(f'O arquivo {arquivo_zip} não foi encontrado.')
        return False

def obter_informacoes_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='latin1') as arquivo:
        linhas = arquivo.readlines()
        informacoes = []

        for linha in linhas[1:]:  # Ignorando cabeçalho
            dados = linha.strip().split(';')
            informacoes.append(dados)

        return informacoes

def criar_diretorio(diretorio):
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

def salvar_lista_em_txt(lista, caminho_arquivo):
    with open(caminho_arquivo, 'w') as arquivo:
        for item in lista:
            linha = ';'.join(map(str, item)) + '\n'
            arquivo.write(linha)

def main():
    # Caminho relativo do arquivo a ser descompactado
    caminho_arquivo_zip = os.path.abspath(os.path.join('RQ03', 'serie_historica_anp.rar'))

    pasta_destino = os.path.abspath(os.path.join('RQ03', 'serie_historica_anp'))

    # Verificar se o arquivo zip existe antes de tentar descompactar
    if descompactar_arquivo(caminho_arquivo_zip, pasta_destino):
        # Restante do código...
        pass  # Adicione aqui o restante do código
    else:
        print("O programa não pode continuar devido à ausência do arquivo.")

if __name__ == "__main__":
    main()






