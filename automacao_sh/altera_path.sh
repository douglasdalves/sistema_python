#!/bin/bash

##----------------------------------##
## no visual code, rodar em bash
##----------------------------------##

CAMINHO_PASTA=/c/scripts_logs/info_path
ARQUIVO_ORG=backupPATH.txt
ARQUIVO_NOVO=PATH_variavel_`date +%F,%H-%M-%S`.txt
cd $CAMINHO_PASTA

gerar_dados(){
    printar_host=$(hostname)
    printar_date=$(date)
    printar_desc=$(echo 'Nome da maquina: '$printar_host)
    printar_info=$(echo 'Data de execução: '$printar_date)
    printar_linha=$(echo '')
    mv $ARQUIVO_ORG $ARQUIVO_NOVO
    echo $printar_linha >> $ARQUIVO_NOVO
    echo $printar_desc >> $ARQUIVO_NOVO
    echo $printar_info >> $ARQUIVO_NOVO
}

gerar_dados