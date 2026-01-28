#!/bin/bash
# Script de inicialização do ambiente e serviços

# verifica se o arquivo requirements.txt foi modificado recentemente

# Cores para o terminal
CYAN='\033[0;36m'
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'

# Caminhos
VENV_PATH="./venv"
SOCKET_DIR="ideal_notify"
PORT=8000

start() {
    # execução do Celery Worker para processamento de tarefas em segundo plano
    echo "Iniciando servidor Django."
    python manage.py runserver
}

stop() {
    echo -e "${RED}🛑 Parando serviço na porta $PORT...${NC}"

    pkill -f celery
    
    if fuser -k $PORT/tcp > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Processos encerrados.${NC}"
    else
        echo -e "⚠️ Nenhum processo ativo encontrado."
    fi
}


case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        stop
        sleep 2
        start
        ;;
    *)
        echo "Uso: $0 {start|stop|restart|}"
        exit 1
esac