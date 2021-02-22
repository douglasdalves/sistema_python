@echo off
title *** Testes de Conectividade ***

:choice0
:start
echo ==================================
echo    --- Nenu de Interacao ---
echo ==================================
echo.
echo 1: Testar novamente o Ping*
echo 2: Teste com ping infinito
echo 3: Sair
echo 4: Menu para teste
echo.
echo ==================================
echo.
echo Escolha uma opcao
set /p choice=
echo.
if '%choice%'=='1' goto :choice1
if '%choice%'=='2' goto :choice2
if '%choice%'=='3' goto :choice3
if '%choice%'=='4' goto :choice4
if '%choice%'=='5' goto :choice5
echo "%choice%" is not a valid option. Please try again.
echo.
goto end


REM opcao 1 do menu com ping

:choice1
echo.
:ping
echo 1: Testando novamente o Ping
ping -n 50 186.251.248.1
echo.
echo.
echo %date%  %time%
echo.
echo Computador: %computername%   Usuario: %username%
echo.
echo -- Teste concluido --
echo.
echo 0: Menu de interacao
echo 1: Testar novamente o Ping
echo 3: Sair
echo.
set /p var=Escolha uma das opcoes acima: 
echo. 
if %var%== 0 goto :choice0
if %var%== 1 goto :choice1
if not %var%== 3 :choice3


REM opcao 2 ping -t

:choice2
echo 2: Testando ping com -t
:ping
echo.
ping 186.251.248.1 -t
echo.
echo -- Teste concluido --
echo.
echo 0: Menu de interacao
echo 3: Sair
echo.
set /p var=Escolha uma das opcoes acima: 
echo. 
if %var%== 0 goto :choice0
if not %var%== 3 :choice3

REM opcao para sair do pront

:choice3
echo 3: Saindo do Pront
echo.
exit
goto end

REM teste de traceroute

:choice4
echo 4: Menu para teste
echo.
echo -- Teste concluido --
echo.
echo 0: Menu de interacao
echo 3: Sair
echo.
set /p var=Escolha uma das opcoes acima: 
echo. 
if %var%== 0 goto :choice0
if not %var%== 3 :choice3




REM  Opcao invalida

:choice5
echo.
echo ===============================================
echo * Opcao Invalida! Escolha outra opcao do menu *
echo ===============================================
echo.
pause 
goto choice0


:end
pause