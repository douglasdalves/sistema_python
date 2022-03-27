#!/bin/bash

#// Teste para automatizar o docker via WSL

#// docker variaveis

status_docker="wsl service docker status"
subindo_docker="wsl sudo service docker start"
stop_docker="wsl sudo service docker stop"


#// containers
docker_ps="wsl docker ps -a"
docker_log="wsl docker logs"


#// portainer variaveis
portainer_stop="wsl docker stop portainer"


#// menu para automatizar
fun_menu(){
    echo && echo "Automatizando o docker no WSL"
    echo && echo "Status atual:"
    $status_docker
    echo
    echo "Parando o Portainer" && $portainer_stop
    echo && $status_docker
    $stop_docker
    sleep 10
}

fun_menu