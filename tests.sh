#!/bin/bash -xe

# parametro -s é o diretorio
# parametro -p é uma regex para dizer quais arquivos procurar
python -m unittest discover -s test -p "*Test*"
