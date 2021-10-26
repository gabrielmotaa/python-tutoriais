# Testes em Python
Nessas branchs de `testes-x`, vamos entender como criar testes em Python utilizando o framework Pytest e algumas ferramentas da biblioteca padrão. 

# Teste 7
Nosso módulo parece pronto para ser usado! Temos código, docstrings e testes, mas será que temos certeza de que tudo está em ordem para uma versão 1.0.0? Existe um plugin para o Pytest que nos diz o percentual que nosso código está de fato coberto por testes! Vamos instalar ele e descobrir se alcançamos a desejada cobertura de 100%.

Lembrando que 100% de cobertura não significa que seu código esteja a prova de falhas! A cobertura nos diz o percentual de linhas executadas no nosso módulo durante os testes.

Caso o código não esteja 100% coberto, você pode passar o parâmetro `--cov-report=html` para gerar um arquivo html que mostra claramente quais linhas de seus códigos não passaram pelos testes!

## Instruções
Clone o repositório em seu computador e rode os seguintes comandos:

### Windows
```shell
$ cd python-tutoriais
$ git checkout testes-7
$ python3 -m venv venv
$ \venv\Scripts\activate
$ python3 -m pip install -r requirements.txt
$ python3 -m pytest --cov=snps_util . -v
```

### Linux
```shell
$ cd python-tutoriais
$ git checkout testes-7
$ python3 -m venv venv
$ source venv/bin/activate
$ python3 -m pip install -r requirements.txt
$ python3 -m pytest --cov=snps_util . -v
```