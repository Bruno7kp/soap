Trabalho de Sistemas de Informação 7º Semestre.

Disciplina de Sistemas Distribuídos.

Alunos: Bruno Varela, Elias, Ricardo.


### Instalação
Baixe ou clone os arquivos desse repositório para a sua máquina.
Abra o terminal na pasta principal e execute os seguintes comandos:

Para criar o ambiente virtual do python:

```python -m venv venv```

Para ativar o ambiente virtual:

```venv\Scripts\activate.bat```

Para instalar as bibliotecas utilizadas:

```python -m pip install pysimplesoap```

```python -m pip install zeep```

Para iniciar o servidor e os clientes, execute os comandos listados abaixo:

### Servidor
- Linguagem: Python 3.8
- Bibliotecas: PySimpleSOAP 1.16.2
- Comando: ```python servidor.py```


### Clientes

#### Python (zeep)
- Linguagem: Python 3.8
- Bibliotecas: zeep 4.0
- Comando: ```python cliente_zeep.py```


#### Python (pysimplesoap)
- Linguagem: Python 3.8
- Bibliotecas: PySimpleSOAP 1.16.2
- Comando: ```python cliente_simple.py```


#### PHP
- Linguagem: PHP 7.4
- Extensões: php-soap (https://www.php.net/manual/pt_BR/book.soap.php)
- Obs: Precisa habilitar a extensão php-soap nas configurações do php
- Comando: ```php cliente.php```


#### Node (JavaScript)
- Linguagem: Node 14.15.0
- Bibliotecas: soap 0.37.0 (https://github.com/vpulim/node-soap)
- Comando 1: ```npm install soap```
- Comando 2: ```node cliente.js```


#### Ruby 
- Linguagem: Ruby 2.7.3
- Bibliotecas: Savon 2.12.1 (https://www.savonrb.com/version2/client.html)
- Comando 1: ```gem install savon --version '2.12.1'```
- Comando 2: ```ruby cliente.rb```



