import os
import struct
import urllib.request
import json

try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    
def obter_dados_exif(caminho_arquivo):
    with open(caminho_arquivo, 'rb') as arquivo:
        arquivo.seek(2)  # Vai para a posição 2 do arquivo
        marcador_app1 = arquivo.read(2)
        
        if marcador_app1 != b'\xff\xe1':
            return None  # Não é um arquivo JPEG com informações de EXIF
        
        arquivo.seek(16)  # Vai para a posição 18 do app1Data
        num_entradas = struct.unpack('>H', arquivo.read(2))[0]
        
        dados_exif = {}
        
        for _ in range(num_entradas):
            id_tag = struct.unpack('>H', arquivo.read(2))[0]
            tipo_dado = struct.unpack('>H', arquivo.read(2))[0]
            num_componentes = struct.unpack('>I', arquivo.read(4))[0]
            
            if tipo_dado == 2:  # String
                valor = arquivo.read(num_componentes).decode('utf-8')
            elif tipo_dado == 3:  # Inteiro sem sinal curto
                valor = struct.unpack('>H', arquivo.read(2))[0]
            elif tipo_dado == 4:  # Inteiro sem sinal longo
                valor = struct.unpack('>I', arquivo.read(4))[0]
            else:
                arquivo.seek(4, os.SEEK_CUR)  # Vai para a próxima entrada
                continue
            
            dados_exif[id_tag] = valor
        
        return dados_exif

def obter_info_gps(dados_exif):
    if 0x8825 not in dados_exif:
        return None
    
    offset_info_gps = dados_exif[0x8825] + 12  # Offset no arquivo
    info_gps = {}
    
    with open(caminho_arquivo, 'rb') as arquivo:
        arquivo.seek(offset_info_gps)
        num_entradas = struct.unpack('>H', arquivo.read(2))[0]
        
        for _ in range(num_entradas):
            id_tag = struct.unpack('>H', arquivo.read(2))[0]
            tipo_dado = struct.unpack('>H', arquivo.read(2))[0]
            num_componentes = struct.unpack('>I', arquivo.read(4))[0]
            
            if tipo_dado == 2:  # String
                valor = arquivo.read(num_componentes).decode('utf-8')
            elif tipo_dado == 5:  # Racional
                numerador = struct.unpack('>I', arquivo.read(4))[0]
                denominador = struct.unpack('>I', arquivo.read(4))[0]
                valor = numerador / denominador
            else:
                arquivo.seek(4, os.SEEK_CUR)  # Vai para a próxima entrada
                continue
            
            info_gps[id_tag] = valor
        
        return info_gps

def obter_info_localizacao(latitude, longitude):
    req_url = f'https://nominatim.openstreetmap.org/reverse?lat={latitude}&lon={longitude}&format=json'
    resposta = requests.get(req_url).text
    info_localizacao = json.loads(resposta)
    return info_localizacao

def processar_imagem(caminho_arquivo):
    dados_exif = obter_dados_exif(caminho_arquivo)
    
    if not dados_exif:
        return None
    
    largura = dados_exif.get(0x0100, 'N/A')
    altura = dados_exif.get(0x0101, 'N/A')
    fabricante = dados_exif.get(0x010F, 'N/A')
    modelo = dados_exif.get(0x0110, 'N/A')
    data_modificacao = dados_exif.get(0x0132, 'N/A')
    data_captura = dados_exif.get(0x9003, 'N/A')
    
    info_gps = obter_info_gps(dados_exif)
    
    if info_gps:
        latitude = info_gps.get(2, 'N/A')
        longitude = info_gps.get(4, 'N/A')
        info_localizacao = obter_info_localizacao(latitude, longitude)
        cidade = info_localizacao.get('address', {}).get('city', 'N/A')
    else:
        latitude = longitude = cidade = 'N/A'
    
    return {
        'Largura': largura,
        'Altura': altura,
        'Fabricante': fabricante,
        'Modelo': modelo,
        'Data Modificação': data_modificacao,
        'Data Captura': data_captura,
        'Latitude': latitude,
        'Longitude': longitude,
        'Cidade': cidade
    }

def principal():
    diretorio = input("Digite o nome do diretório: ")
    cidades = {}
    
    for nome_arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        
        if os.path.isfile(caminho_arquivo) and nome_arquivo.lower().endswith('.jpg'):
            info_imagem = processar_imagem(caminho_arquivo)
            
            if info_imagem:
                cidade = info_imagem['Cidade']
                cidades[cidade] = cidades.get(cidade, 0) + 1
                
                print(f"\nInformações para o arquivo: {nome_arquivo}")
                for chave, valor in info_imagem.items():
                    print(f"{chave}: {valor}")
    
    print("\nCidades onde fotos foram capturadas:")
    for cidade, quantidade in cidades.items():
        print(f"{cidade}: {quantidade} fotos")

if __name__ == "__main__":
    principal()





