def ordena_bubble(lista):
    try:
        for i in range(len(lista)):
            for j in range(0, len(lista) - i - 1):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
        return True, lista
    except Exception as e:
        return False, None

def ordena_insertion(lista):
    try:
        for i in range(1, len(lista)):
            chave = lista[i]
            j = i - 1
            while j >= 0 and chave < lista[j]:
                lista[j + 1] = lista[j]
                j -= 1
            lista[j + 1] = chave
        return True, lista
    except Exception as e:
        return False, None

def ordena_selection(lista):
    try:
        for i in range(len(lista)):
            min_index = i
            for j in range(i + 1, len(lista)):
                if lista[j] < lista[min_index]:
                    min_index = j
            lista[i], lista[min_index] = lista[min_index], lista[i]
        return True, lista
    except Exception as e:
        return False, None

def ordena_quick(lista):
    def partition(arr, low, high):
        i = low - 1
        pivot = arr[high]
        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quick_sort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort(arr, low, pi - 1)
            quick_sort(arr, pi + 1, high)

    try:
        quick_sort(lista, 0, len(lista) - 1)
        return True, lista
    except Exception as e:
        return False, None

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            lista = [int(line.strip()) for line in arquivo]
        return True, lista
    except FileNotFoundError:
        return False, None
    except Exception as e:
        return False, None

def main():
    while True:
        nome_arquivo = input("Digite o nome do arquivo a ser lido: ")

        sucesso, lista = ler_arquivo(nome_arquivo)

        if sucesso:
            print("Lista lida do arquivo:", lista)
            
            while True:
                print("Escolha um método de ordenação:")
                print("Digite 1 para BUBBLE")
                print("Digite 2 para INSERTION")
                print("Digite 3 para SELECTION")
                print("Digite 4 para QUICK")
                
                escolha = input("Sua escolha: ")
                
                if escolha == "1":
                    metodo_ordena = "BUBBLE"
                elif escolha == "2":
                    metodo_ordena = "INSERTION"
                elif escolha == "3":
                    metodo_ordena = "SELECTION"
                elif escolha == "4":
                    metodo_ordena = "QUICK"
                else:
                    print("Opção inválida. Escolha uma opção válida (1 a 4).")
                    continue

                _, lista_ordenada = globals()[f'ordena_{metodo_ordena.lower()}'](lista)
                if lista_ordenada:
                    print(f"Lista ordenada ({metodo_ordena}): {lista_ordenada}")
                else:
                    print(f"Falha na ordenação ({metodo_ordena}).")
                break
        
        else:
            print("Arquivo não encontrado ou falha ao ler o arquivo. Por favor, tente novamente.")
            continue
        
        continuar = input("Deseja continuar? (S/N): ").strip().lower()
        if continuar != 's':
            break
    
    print("Fim da execução.")

if __name__ == "__main__":
    main()




