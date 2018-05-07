#!/bin/bash -xe

python test/server/HttpServer.py &
FOO_PID=$!
echo $FOO_PID

cleanup () {
    kill -9 $FOO_PID
    exit $exit_code
}

trap cleanup EXIT ERR INT TERM

sleep .5

# parametro -s é o diretorio
# parametro -p é uma regex para dizer quais arquivos procurar
python -m unittest discover -s test -p "*Test*" 
exit_code=$?