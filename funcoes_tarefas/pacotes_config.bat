::::::::::::::::::::::::::::::::::::::::::::
:: Elevate.cmd - Version 4
:: Automatically check & get admin rights
::::::::::::::::::::::::::::::::::::::::::::
@echo off
CLS

:init
setlocal DisableDelayedExpansion
set cmdInvoke=1
set winSysFolder=System32
set "batchPath=%~0"
for %%k in (%0) do set batchName=%%~nk
set "vbsGetPrivileges=%temp%\OEgetPriv_%batchName%.vbs"
setlocal EnableDelayedExpansion

:checkPrivileges
NET FILE 1>NUL 2>NUL
if '%errorlevel%' == '0' ( goto gotPrivileges ) else ( goto getPrivileges )

:getPrivileges
if '%1'=='ELEV' (echo ELEV & shift /1 & goto gotPrivileges)
ECHO.
ECHO **************************************
ECHO Invoking UAC for Privilege Escalation
ECHO **************************************

ECHO Set UAC = CreateObject^("Shell.Application"^) > "%vbsGetPrivileges%"
ECHO args = "ELEV " >> "%vbsGetPrivileges%"
ECHO For Each strArg in WScript.Arguments >> "%vbsGetPrivileges%"
ECHO args = args ^& strArg ^& " "  >> "%vbsGetPrivileges%"
ECHO Next >> "%vbsGetPrivileges%"

if '%cmdInvoke%'=='1' goto InvokeCmd 

ECHO UAC.ShellExecute "!batchPath!", args, "", "runas", 1 >> "%vbsGetPrivileges%"
goto ExecElevation

:InvokeCmd
ECHO args = "/c """ + "!batchPath!" + """ " + args >> "%vbsGetPrivileges%"
ECHO UAC.ShellExecute "%SystemRoot%\%winSysFolder%\cmd.exe", args, "", "runas", 1 >> "%vbsGetPrivileges%"

:ExecElevation
"%SystemRoot%\%winSysFolder%\WScript.exe" "%vbsGetPrivileges%" %*
exit /B

:gotPrivileges
setlocal & cd /d %~dp0
if '%1'=='ELEV' (del "%vbsGetPrivileges%" 1>nul 2>nul  &  shift /1)

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
REM Usar get/post/delete com o requets
pip install requests
echo.
REM biblioteca para barra de progresso
pip install tqdm
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
echo requests - tqdm
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