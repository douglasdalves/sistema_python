#!/bin/bash

#// Teste para automatizar o docker via WSL

#// docker variaveis

status_docker="wsl service docker status"
subindo_docker="wsl sudo service docker start"
stop_docker="wsl sudo service docker stop"


#// containers
docker_ps="wsl docker ps -a"




#// portainer variaveis
grep_portainer="wsl docker ps | grep portainer"
portainer_stop="wsl docker stop portainer"
log_portainer="wsl docker logs -n 3 portainer"


#// menu para automatizar
fun_menu(){
    echo && echo "Automatizando o docker no WSL"
    echo && echo "Status atual:"
    $status_docker
    echo
    echo "Startando o serviço" && $subindo_docker
    echo
    $log_portainer
}

fun_menu