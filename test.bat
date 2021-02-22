@echo off
title *** Testes de Conectividade ***
:ping
echo *** Executando o Ping x40 para o IP da seanet ***
echo.
ping -n 8 186.251.248.1
echo.
echo -------------------------------------------------
echo.
echo %date%   %time%
echo Computador: %computername%   Usuario: %username%
echo.
echo -- Teste concluido --
echo.
echo -------------------------------------------------
echo.
echo.
echo 4: Automacao do python
start C:\scripts\sistema.py
echo.


REM opcao usar navegador



:end
pause