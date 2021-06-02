@echo off
title *** Funcoes do PIP ***
echo.
echo -----------------------------------------
echo   Instalacao dos pacotes para o python
echo -----------------------------------------
echo.
echo 1 - Atualizando o PIP:
echo.
pip install --upgrade pip
echo.
pip install pyautogui
REM usado para criar bots para automatizar tarefas repetitivas
echo.
pip install pillow
REM biblioteca voltada para a manipulação de imagens
echo.
pip install selenium
REM para execuat testes no browser
echo.
pip install termcolor
echo.
REM proporciona formatação ANSII e permite a saída de cores no terminal
REM ativar a cor do pacote
reg add HKEY_CURRENT_USER\Console /v VirtualTerminalLevel /t REG_DWORD /d 0x00000001 /f
echo.
echo.
echo -----------------------------------------
echo          Processo finalizado
echo -----------------------------------------
echo.
echo 2 - Itens relacionados para instalacao:
echo pyautogui - pillow - selenium - termcolor
echo.
echo 2.1 - Vou listar os itens ativados:
echo.
pip list
echo.
echo.
echo ---------------------------------------------
echo. Concluindo, vou abrir o sistema para voce..
echo ---------------------------------------------
echo.
start C:\scripts\sistema.py
echo.
pause