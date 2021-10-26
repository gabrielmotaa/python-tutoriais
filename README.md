# Testes em Python
Nessas branchs de `testes-x`, vamos entender como criar testes em Python utilizando o framework Pytest e algumas ferramentas da biblioteca padrão. 

# Teste 1
Vamos começar por um pequeno script que é capaz de produzir uma fita complementar de segmentos de DNA.

O script vai se chamar `snps_util.py`, pois, conforme o projeto for avançando, vamos criar uma pequena biblioteca com funções de nos ajudar a analisar arquivos de SNPs.

## Instruções
Clone o repositório em seu computador e rode os seguintes comandos:

### Windows
```shell
$ cd python-tutoriais
$ git checkout testes-1
$ python3 -m venv venv
$ \venv\Scripts\activate
$ python3 -m pytest .
```

### Linux
```shell
$ cd python-tutoriais
$ git checkout testes-1
$ python3 -m venv venv
$ source venv/bin/activate
$ python3 -m pytest .
```