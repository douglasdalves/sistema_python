import os

def test_conexao():
    print('HTTP Status Code da Página speedtest.net')
    os.system('curl --write-out %{http_code} --silent --output /dev/null www.google.com.br')

#print('Bem Vindo ao teste')
#os.system('curl --write-out %{http_code} --silent --output /dev/null www.google.com.br')
test_conexao()