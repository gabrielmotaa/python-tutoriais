# Padronização de código

Conforme nosso código fica maior e mais complexo, temos que cuidar da sua organização e garantir um padrão na sua construção e manutenção.

## Convenções
Na criação de código, um dos pontos mais importantes é seguir uma conveção bem definida na comunidade da linguagem ou framework a ser trabalhado.

Exemplos:
- Em JavaScript, a regra é utilizar camelCase e PascalCase em funções e classes, entre outros.
- Em PHP, a regra é usar snake_case em frameworks como Wordpress e camelCase em frameworks como Laravel, entre outros.

Em Python, também temos nossas [convenções](https://pep8.org/). Em resumo, os pontos principais são:
- Nomes de funções e variáveis em snake_case
- Nome de constantes em SCREAMING_SNAKE_CASE
- Nome de classes em PascalCase
- Identação por 4 espaços
- Evitar `import` fora do começo do arquivo ou `import *`
Assim em diante.

```python
from random import *  # você está poluindo o módulo com incontáveis funções e variáveis

def getRandomNumber():  # nomeação fora do padrão
    'Retorna um número de 0 a 100'  # docstring com uma aspa
    return randint(0, 100)

class order:  # nomeação fora do padrão
    def __init__(this, product_list):  # this ao invés de self
        this.product_list = product_list  # product_list não é melhor escolha. nesses casos type hints são bem úteis!
        this.id = get_random_number()
```

```python
from random import randint  # explícito quais imports foram feitos

def generate_random_number():  # snake_case e um nome um pouco mais descritivo
    """Retorna um número de 0 a 100."""  # docstring com aspas triplas
    return randint(0, 100)


class Order:   # nomeação correta
    def __init__(self, products):
        self.products = products
        self.id = generate_random_number()
```

É claro, sempre existem exceções à regra, mesmo na própria linguagem. Módulos como `unittest` foram escritos antes da PEP8 e mudar nomeações por pura estética não é prioridade. Existem equipes que montam seus próprios padrões e decidem usar camelCase ou apenas aspas simples. O mais importante é manter os códigos de um projeto consistentes.

Mas pensar em certas regras e formatação é um gasto energético um tanto desnecessário, não?

## Formatadores
Se podemos automatizar quase tudo, porque não automatizar a formatação e checagem de código? Temos três ferramentas para isso:

#### Black
Black é um formatador com 'fortes convicções'. Ele tem regras bem rígidas e vai mudar o seu código quase sempre. Há quem não goste, mas se tornou padrão na comunidade e está até sobre o guarda chuva da [PSF](https://github.com/psf).

#### Isort
Já analisou um dia que a sua lista de imports é confusa e esquisita? Todos já chegamos lá. O isort está aqui para resolver nossa vida, separando imports da biblioteca padrão, de pacotes de terceiros e módulos próprios, tudo em ordem alfabética e mais.

#### Flake8
Flake8 é um linter, ou seja, ele vai analisar o seu código e ver há inconsistências, como imports não utilizados, variáveis perdidas ou utilizações incorretas de certas estruturas. Ele também checa coisas como espaços e tamanho de linhas, mas rodando ele depois do Black esses pontos não serão relevantes.

### Configurações
Um problema na comunidade, e nessas ferramentas, é que cada uma suporta um tipo diferente de arquivo de configuração, às vezes arquivos iguais ou não. Então é um território um tanto desgradável de desbravar.

Temos que configurar:
1. Flake8 para funcionar com o Black
2. Isort para funcionar com o Black
3. coverage e pytest

Pytest e isort podem ficar no mesmo arquivo, `pyproject.toml`:
```toml
[pytest.ini_options]
addopts = "--cov=snps_util --cov-report html"
testspaths = ["tests"]

[tool.isort]
profile = "black"
multi_line_output = 3
src_paths = ["snps_file", "tests"]
```

Flake8 tem seu próprio arquivo, `.flake8`:
```ini
[flake8]
max-line-length = 88
extend-ignore = E203
exclude = __init__.py
```

E por fim, coverage tem `.coveragerc`:
```ini
[run]
branch = True
omit = tests/*
```

Como podemos rodar tudo isso?
```shell
$ python3 -m black .
$ python3 -m isort .
$ python3 -m flake8 snps_util tests
$ python3 -m pytest
```

Mas se estamos querendo automatizar as coisas, isso não é repetitivo? Sim, tanto que podemos criar um script shell para isso, `format.sh`:
```shell
#!/usr/bin/env bash
set -x
python3 -m black .
python3 -m isort .
python3 -m flake8 snps_util tests
python3 -m pytest
```

Basta rodá-lo antes de cada commit. Existe mais uma maneira de automatizar isso antes de cada commit, usando a ferramenta pre-commit, mas isso é assunto para outro tópico.

### Requirements
Até então, só precisamos da biblioteca `requests` para nosso código, todo o resto são ferramentas de desenvolvimento. Instalar todas essas dependências só para rodar o código principal não faz sentido, então podemos separar o arquivo `requeriments.txt` em `requeriments.txt` e `test_requirements.txt`.
