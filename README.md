# Testes em Python
Nessas branchs de `testes-x`, vamos entender como criar testes em Python utilizando o framework Pytest e algumas ferramentas da biblioteca padrão. 

# Teste 5
Testes nos permitem refatorar o código com maior segurança! Vamos melhorar a descoberta de `vendors` a partir dos arquivos e não vamos ter que reescrever nenhum teste! Depois da mudança, todos os testes devem passar.

Também vamos adicionar docstrings em todo código do nosso módulo!
## Instruções
Clone o repositório em seu computador e rode os seguintes comandos:

### Windows
```shell
$ cd python-tutoriais
$ git checkout testes-5
$ python3 -m venv venv
$ \venv\Scripts\activate
$ python3 -m pip install -r requirements.txt
$ python3 -m pytest . -v
```

### Linux
```shell
$ cd python-tutoriais
$ git checkout testes-5
$ python3 -m venv venv
$ source venv/bin/activate
$ python3 -m pip install -r requirements.txt
$ python3 -m pytest . -v
```