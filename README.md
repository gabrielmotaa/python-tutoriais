# Testes em Python
Nessas branchs de `testes-x`, vamos entender como criar testes em Python utilizando o framework Pytest e algumas ferramentas da biblioteca padrão. 

# Teste 2
Com os primeiros testes criados, vimos como há muita repetição no código. Testes, assim como os códigos normais, também devem evitar repetições. O Pytest nos fornece ferramentas para isso, nesse caso o decorador `@pytest.mark.parametrize`.

## Instruções
Clone o repositório em seu computador e rode os seguintes comandos:

### Windows
```shell
$ cd python-tests
$ python3 -m venv venv
$ \venv\Scripts\activate
$ python3 -m pytest .
```

### Linux
```shell
$ cd python-tests
$ python3 -m venv venv
$ source venv/bin/activate
$ python3 -m pytest .
```