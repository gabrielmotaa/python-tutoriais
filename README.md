# Testes em Python
Nessas branchs de `testes-x`, vamos entender como criar testes em Python utilizando o framework Pytest e algumas ferramentas da biblioteca padrão. 

# Teste 4
Vamos criar uma nova funcionalidade em nosso módulo. Queremos que ele seja capaz de ler um arquivo de snps (no formato FTDNA ou 23andme) e retorne informações como `callrate` ou o genótipo de `rsid` específico. Para isso vamos construir primeiros os testes e depois o código, usando o padrão TDD (Test-Driven Development).
## Instruções
Clone o repositório em seu computador e rode os seguintes comandos:

### Windows
```shell
$ cd python-tutoriais
$ git checkout testes-4
$ python3 -m venv venv
$ \venv\Scripts\activate
$ python3 -m pip install -r requirements.txt
$ python3 -m pytest . -v
```

### Linux
```shell
$ cd python-tutoriais
$ git checkout testes-4
$ python3 -m venv venv
$ source venv/bin/activate
$ python3 -m pip install -r requirements.txt
$ python3 -m pytest . -v
```