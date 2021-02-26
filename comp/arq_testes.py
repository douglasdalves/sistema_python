#import os

#os.system('ipconfig')
#os.system('start ./funcoes/conexao_seanet.py')

def mensagem():
    print("Olá, mundo")

mensagem()


git remote add origin https://github.com/douglasdalves/sistema_python.git
git branch -M main
git push -u origin main


git push https://github.com/douglasdalves/sistema_python.git


Nome = input("Digite o nome do cliente: ")
DiaVencimento = input("Digite o dia de vencimento: ")
MêsVencimento = input("Digite o mês de vencimento: ")
ValorFatura = input("Digite o valor da fatura: ")

print("Olá,", Nome, "\n A sua fatura com vencimento em ", DiaVencimento, " de ", MêsVencimento, "no valor de R$", ValorFatura, "está fechada.")