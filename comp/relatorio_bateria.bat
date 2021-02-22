:start
echo -----------------------
echo 5: Relatorio de bateria
echo -----------------------
echo.
powercfg /batteryreport
move battery-report.html D:\scripts\Relatorios\
echo.
echo -- Teste concluido --