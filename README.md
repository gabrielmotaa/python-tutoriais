# Testes em Python
Nessas branchs de `testes-x`, vamos entender como criar testes em Python utilizando o framework Pytest e algumas ferramentas da biblioteca padrão. 

# Teste 8
Vamos adicionar mais funcionalidades ao nosso módulo! Queremos fazer uma consulta ao Ensembl REST API e descobrir informações sobre o rsID informado. Também queremos outra função que nos retorne algo específico, sobre o alelo menos frequente do rsID. Construir a função é fácil (obrigado `requests`) mas testar não é tão trivial. Não podemos testar fazendo requisições de verdade, então precisamos '[mockar](https://pt.wikipedia.org/wiki/Objeto_mock)' elas!


## Instruções
Clone o repositório em seu computador e rode os seguintes comandos:

### Windows
```shell
$ cd python-tutoriais
$ git checkout testes-8
$ python3 -m venv venv
$ \venv\Scripts\activate
$ python3 -m pip install -r requirements.txt
$ python3 -m pytest --cov=snps_util . -v
```

### Linux
```shell
$ cd python-tutoriais
$ git checkout testes-8
$ python3 -m venv venv
$ source venv/bin/activate
$ python3 -m pip install -r requirements.txt
$ python3 -m pytest --cov=snps_util . -v
```