import random

def obter_valor_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("O valor informado não é um número inteiro válido. Tente novamente.")

def gerar_lista(quantidade, valor_minimo, valor_maximo):
    if quantidade <= 0 or valor_minimo > valor_maximo:
        return False, None
    
    lista = [random.randint(valor_minimo, valor_maximo) for _ in range(quantidade)]
    return True, lista

def salvar_lista_em_arquivo(nome_lista, nome_arquivo):
    try:
        with open(nome_arquivo, 'w') as arquivo:
            for valor in nome_lista:
                arquivo.write(f"{valor}\n")
        return True
    except Exception as e:
        print(f"Erro ao salvar a lista: {str(e)}")
        return False

def main():
    valor1 = obter_valor_inteiro("Digite o primeiro valor inteiro: ")
    valor2 = obter_valor_inteiro("Digite o segundo valor inteiro: ")
    valor3 = obter_valor_inteiro("Digite o terceiro valor inteiro: ")

    sucesso, lista = gerar_lista(valor1, valor2, valor3)

    if sucesso:
        print("Lista gerada com sucesso:", lista)
        nome_arquivo = input("Digite o nome do arquivo para salvar a lista: ")
        sucesso_salvar = salvar_lista_em_arquivo(lista, nome_arquivo)
        if sucesso_salvar:
            print(f"Lista salva com sucesso no arquivo {nome_arquivo}")
        else:
            print("Falha ao salvar a lista.")
    else:
        print("Falha ao gerar a lista.")

if __name__ == "__main__":
    main()
