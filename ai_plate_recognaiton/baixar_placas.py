import os
import time
import requests
from duckduckgo_search import DDGS

# Configurações
busca = "placa de caminhão png"
quantidade = 100
pasta_destino = "placa_png"

# Cria a pasta se não existir
os.makedirs(pasta_destino, exist_ok=True)

# Inicializa a classe DDGS
with DDGS() as ddgs:
    # Busca imagens
    resultados = ddgs.images(busca, max_results=quantidade)

    # Baixa as imagens com intervalo de 5 segundos
    for i, resultado in enumerate(resultados):
        url = resultado["image"]
        try:
            resposta = requests.get(url, timeout=10)
            if resposta.status_code == 200:
                caminho_arquivo = os.path.join(pasta_destino, f"placa_{i+1}.png")
                with open(caminho_arquivo, 'wb') as f:
                    f.write(resposta.content)
                print(f"✅ Imagem {i+1} salva em: {caminho_arquivo}")
            else:
                print(f"❌ Imagem {i+1} falhou (status {resposta.status_code})")
        except Exception as e:
            print(f"⚠️ Erro ao baixar imagem {i+1}: {e}")
        
        time.sleep(5)
