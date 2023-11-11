import os
import pandas as pd

def carregar_dados_cartola(ano):
    try:
        # Obtém o diretório do script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        arquivo = os.path.join(script_dir, f"{ano}.csv")
        
        # Verifica se o arquivo existe
        if not os.path.exists(arquivo):
            raise FileNotFoundError(f"Arquivo para o ano {ano} não encontrado em {script_dir}.")
        
        dados = pd.read_csv(arquivo)
        return dados
    except FileNotFoundError as e:
        print(e)
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao carregar os dados: {e}")
        return None

def escolher_esquema_tatico():
    print("Escolha um esquema tático:")
    print("1. 3-4-3")
    print("2. 3-5-2")
    print("3. 4-3-3")
    print("4. 4-4-2")
    print("5. 4-5-1")
    print("6. 5-3-2")
    print("7. 5-4-1")
    
    opcao = input("Digite o número correspondente ao esquema desejado: ")
    
    esquemas = {
        "1": [3, 0, 4, 3],
        "2": [3, 0, 5, 2],
        "3": [2, 2, 3, 3],
        "4": [2, 2, 4, 2],
        "5": [2, 2, 5, 1],
        "6": [3, 2, 3, 2],
        "7": [3, 2, 4, 1]
    }
    
    return esquemas.get(opcao, None)

def selecionar_jogadores(dados, esquema):
    posicoes = ["zagueiro", "lateral", "meia", "atacante", "goleiro", "tecnico"]
    jogadores_selecionados = []

    for posicao, quantidade in zip(posicoes, esquema):
        jogadores_posicao = dados[dados['posicao'] == posicao]
        jogadores_posicao = jogadores_posicao.nlargest(quantidade, 'pontuacao')
        jogadores_selecionados.extend(jogadores_posicao.to_dict(orient='records'))

    return jogadores_selecionados

def exibir_jogadores_selecionados(jogadores):
    for jogador in jogadores:
        print(f"{jogador['posicao']}: {jogador['nome']} ({jogador['time']}) - Pontuação: {jogador['pontuacao']}")

def salvar_arquivo_selecao(jogadores, ano):
    arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"selecao_cartola_fc_{ano}.txt")
    
    with open(arquivo, 'w') as f:
        f.write("posicao;nome;url_foto_atleta;pontuacao;time;url_escudo_time\n")
        for jogador in jogadores:
            f.write(f"{jogador['posicao']};{jogador['nome']};{jogador['url_foto_atleta']};{jogador['pontuacao']};{jogador['time']};{jogador['url_escudo_time']}\n")

def main():
    ano = input("Informe o ano desejado: ")
    dados_cartola = carregar_dados_cartola(ano)

    if dados_cartola is not None:
        esquema_tatico = escolher_esquema_tatico()

        if esquema_tatico is not None:
            jogadores_selecionados = selecionar_jogadores(dados_cartola, esquema_tatico)
            exibir_jogadores_selecionados(jogadores_selecionados)
            salvar_arquivo_selecao(jogadores_selecionados, ano)
        else:
            print("Esquema tático inválido.")

if __name__ == "__main__":
    main()


