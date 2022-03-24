
from cProfile import label
from sqlite3 import Row
from tkinter import *
from variaveis.interface_config import *


def dados_pc_teste():
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
    text_data = colored('Data e Hora do teste:', 'blue', attrs=['bold'])

    cpu = platform.node()
    text_cpu = colored('Equipamento do Teste:', 'blue', attrs=['bold'])

    user = getpass.getuser()
    text_user = colored('Usuario do Sistema:', 'blue', attrs=['bold'])

    texto = f'''
    Data e Hora do teste: {data_e_hora_em_texto}
    Equipamento do Teste: {cpu}
    Usuario do Sistema: {user}'''


    texto_retorno["text"] = texto


janela = Tk() #inicio da janela
janela.title("Aplication System")
janela.geometry("400x400")

texto_inicial = Label(janela, text="teste")
texto_inicial.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Executar", command=dados_pc_teste)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_retorno = Label(janela, text="")
texto_retorno.grid(column=0, row=2, padx=10, pady=10)


janela.mainloop() #fim para manter a janela aberta