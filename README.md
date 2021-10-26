# Testes em Python
Nessas branchs de `testes-x`, vamos entender como criar testes em Python utilizando o framework Pytest e algumas ferramentas da biblioteca padrão. 

# Teste 6
**Repetição, repetição, repetição!**

Em `testes-2` nós discutimos como o Pytest nos permite reduzir repetição em nossos testes, mas você deve ter reparado que temos muitas repetições em nossos testes! Temos que criar e apagar um arquivo temporário em quase todos os testes!

Vamos mexer com fixtures, que permitem que criemos funções para serem utilizadas em nossos testes! Também vamos criar o arquivo `conftest.py` que o Pytest utiliza para rodar essas funções antes de correr qualquer teste.
## Instruções
Clone o repositório em seu computador e rode os seguintes comandos:

### Windows
```shell
$ cd python-tutoriais
$ git checkout testes-6
$ python3 -m venv venv
$ \venv\Scripts\activate
$ python3 -m pip install -r requirements.txt
$ python3 -m pytest . -v
```

### Linux
```shell
$ cd python-tutoriais
$ git checkout testes-6
$ python3 -m venv venv
$ source venv/bin/activate
$ python3 -m pip install -r requirements.txt
$ python3 -m pytest . -v
```