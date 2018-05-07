#!/bin/bash -xe
python -m SimpleHTTPServer 8000 &
FOO_PID=$!
echo $FOO_PID

sleep .5

# parametro -s é o diretorio
# parametro -p é uma regex para dizer quais arquivos procurar
python -m unittest discover -s test -p "*Test*"

kill -9 $FOO_PID