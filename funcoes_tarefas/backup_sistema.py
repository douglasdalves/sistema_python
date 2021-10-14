
import os
from datetime import datetime

LOG_FILENAME = datetime.now().strftime('Script_sistema_%d_%m_%Y_%H_%M')
caminho_origem = r'C:/'
caminho_destino = r'D:/scripts'

os.chdir(caminho_origem)
#copiar_dados = os.listdir("scripts")

os.system('cp -r scripts D:/scripts')
os.chdir(caminho_destino)
os.rename('scripts', LOG_FILENAME)

#os.system('ls -ltr Script_sistema*')
#print(copiar_dados)