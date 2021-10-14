
import pyautogui
import time
import pyperclip

pyautogui.PAUSE = 1

#-----------------------------------

## abrindo o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter") #pressiona o enter do teclado
pyautogui.click(x=1288, y=565) #posição coletada de onde vai ser clicado
pyautogui.press("enter")

#-----------------------------------

## planilha de horas
pyautogui.hotkey("ctrl", "t") #atalho do teclado
link_excel = "https://compasso-my.sharepoint.com/:x:/r/personal/douglas_alves_compasso_com_br/_layouts/15/WopiFrame.aspx?sourcedoc=%7B63404A37-077C-427D-9BEA-BDF78383499F%7D&file=Horas%20compasso.xlsx&action=default"
pyperclip.copy(link_excel)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(1)


## nova aba do navegador
pyautogui.hotkey("ctrl", "t")
link = "https://www.dimepkairos.com.br"
pyperclip.copy(link)
## add conteudo do kairos - link
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
time.sleep(5)
pyautogui.click(x=1318, y=167)
pyautogui.press("enter")
time.sleep(17)
pyautogui.click(x=2459, y=131)
pyautogui.click(x=2481, y=162)
pyautogui.press("enter")
pyautogui.click(x=260, y=728)
pyautogui.press("enter")


## compasso refinamento de atividades
pyautogui.hotkey("ctrl", "t")
link_atividades = "https://compasso.ninja/pls/interno/whsrefinamentoatividades"
pyperclip.copy(link_atividades)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
pyautogui.click(x=1337, y=263)
pyautogui.press("enter")
time.sleep(1)
## preenchimento
""" pyautogui.click(x=246, y=325)
pyautogui.press("enter")
pyautogui.click(x=282, y=372)
pyautogui.press("enter") """