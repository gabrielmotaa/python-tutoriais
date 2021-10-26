# Testes em Python
Nessas branchs de `testes-x`, vamos entender como criar testes em Python utilizando o framework Pytest e algumas ferramentas da biblioteca padrão. 

# Teste 3
Agora, para prosseguirmos com uma melhor organização dos nossos códigos e testes, podemos transformar nosso script em um módulo e dexar os testes na pasta `tests`. Como a função que criamos é bem simples, ela vai ficar no arquivo `helpers.py` e vamos importar ela no `__init__.py` para ficar disponível no módulo assim como o teste chamava antes. Veja que todos os testes ainda passam.

## Instruções
Clone o repositório em seu computador e rode os seguintes comandos:

### Windows
```shell
$ cd python-tutoriais
$ git checkout testes-3
$ python3 -m venv venv
$ \venv\Scripts\activate
$ python3 -m pip install -r requirements.txt
$ python3 -m pytest . -v
```

### Linux
```shell
$ cd python-tutoriais
$ git checkout testes-3
$ python3 -m venv venv
$ source venv/bin/activate
$ python3 -m pip install -r requirements.txt
$ python3 -m pytest . -v
```