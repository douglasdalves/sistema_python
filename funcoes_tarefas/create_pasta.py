from pathlib import Path
import os

# Lista de nomes de pastas que você deseja criar
pastas = ["C:/scripts_logs/info-pacotes", "C:/scripts_logs/log-app", 
          "C:/scripts_logs/ping-provedor", "C:/scripts_logs/captura"]

# Diretório onde as pastas serão criadas
diretorio_base = "C:/"

for pasta in pastas:
    caminho_completo = os.path.join(diretorio_base, pasta)
    
    try:
        os.makedirs(caminho_completo, exist_ok=True)
        print(f"Pasta '{pasta}' criada com sucesso!")
    except OSError as erro:
        print(f"Erro ao criar a pasta '{pasta}': {erro}")


# # Especifique o caminho da pasta que você deseja criar
# pasta = Path("C:/sistema_python/automacao_sh2")

# try:
#     pasta.mkdir(parents=True, exist_ok=True)
#     print(f"Pasta '{pasta}' criada com sucesso!")
# except OSError as erro:
#     print(f"Erro ao criar a pasta: {erro}")


