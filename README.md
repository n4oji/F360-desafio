# F360-desafio

Este repositório contém a resolução de três desafios de programação e um exercício extra, cada um com foco em diferentes competências.



## Desafios

### 1. Integração com a API do OpenWeatherMap

**Objetivo**: Consumir a API do OpenWeatherMap para obter dados metereológicos de uma cidade escolhida e salvar o retorno em um arquivo CSV.

**Arquivos**:


```http
desafio_1.py
.env
```

| Parâmetro   | Tipo       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `API_KEY_OPENWEATHER` | `string` | **Obrigatório**. A chave da sua API do OpenWeatherMap |

#### Retorna as informações em um print do Python e um arquivo CSV com os dados salvos.

```http
Cidade: sao paulo
Temperatura: 22.63°C
Umidade: 91%
Pressão: 1013 hPa
Descrição: light rain
Dados de sao paulo salvos em weather.csv
```

**Como usar**: 
 - Colocar a chave da API dentro do arquivo .env
 - Execurtar o arquivo python _desafio_1.py_
 - Observar os dados salvos no arquivo gerado _weather.csv_


### 2. Manipular dados com Pandas

**Objetivo**: Utilizar a biblioteca Pandas para criar um dataframe com os dados fornecidos, calcular a média da notas e adicionar uma nova coluna para saber se o aluno está ou não aprovado.

**Dados**:
```json
{"Nomes": ["Ana", "Bruno", "Carlos", "Daniela"],"Idades": [22, 23, 21, 22],"Notas": [88, 92, 95, 85]}
```

**Arquivos**:
```http
desafio_2.py
```

**Como usar**:
 - Execurtar o arquivo python _desafio_2.py_
 - Observar os dados fornecidos no terminal com o print

### 3. Manipulação de Dados no Excel

**Objetivo**: Manipular dados da planilha excel fornecida, calcular os valores totais por categoria e adicionar essas informações em uma nova aba.

**Arquivos**:

```http
desafio_3.py
vendas_ecommerce.xlsx
```
**Como usar**: 
 - Execurtar o arquivo python _desafio_3.py_
 - Observar os dados salvos na planilha _vendas_ecommerce.xlsx_


### 4. Extra - Desenvolvimento de Algoritmo
**Objetivo**: Escrever uma função para identificar a maior soma de subarray contínuo dado uma lista de inteiros.

**Arquivos**:

```http
extras.py
test_extras.py
```
**Como usar**: 
 - Execurtar o arquivo python _test_extras.py_
 - Observar se algum teste apresenta algum erro, você tanbém pode alterar os valores dos testes no arquivo _test_extras.py_ para checar o funcionamento do algoritmo.

## Instalação

### Pré-requisitos
- Python 3.x instalado
- Bibliotecas necessárias: `pandas`, `requests`, `openpyxl`, `python-dotenv` 
- Api do OpenWeatherMap para rodar o primeiro desafio

#### 1. Clonar o repositório ou copiar os scripts e arquivo excel para executar o desafio 3
#### 2. Instalar as bibliotecas necessárias
```bash
  pip install pandas requests openpyxl python-dotenv
```
#### 3. Executar cada Script como mencionado acima
    