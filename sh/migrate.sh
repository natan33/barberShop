

if [ -z "$1" ]; then
  echo "Erro: você precisa passar a mensagem do migrate."
  echo "Uso: ./migrate.sh \"Minha mensagem de migrate\""
  exit 1
fi

# Guarda a mensagem em uma variável
COMMIT_MESSAGE=$1

# Adiciona todos os arquivos

# Faz o commit com a mensagem
python manage.py makemigrations $COMMIT_MESSAGE

# Aplica as migrações no banco de dados
python manage.py migrate