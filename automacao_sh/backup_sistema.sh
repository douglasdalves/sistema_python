#!/bin/bash

##----------------------------------##
## copiar o sistema para a partiçao
##----------------------------------##

CAMINHO_PASTA=/mnt/c
CAMINHO_SSD=/mnt/d/scripts
ARQUIVO_COPIADO=scripts.bkp
ARQUIVO_ORG=scripts.bkp.zip
ARQUIVO_NOVO=scripts.bkp_`date +%F,%H-%M-%S`.zip
cd $CAMINHO_PASTA

gerar_dados(){
    cp -r scripts /mnt/d/scripts/scripts.bkp
    cd $CAMINHO_SSD
    zip -rg scripts.bkp.zip scripts.bkp/
    mv $ARQUIVO_ORG $ARQUIVO_NOVO
    rm -rf $ARQUIVO_COPIADO
}

gerar_dados