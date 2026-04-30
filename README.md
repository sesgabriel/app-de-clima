# 🌤️ Consultor de Clima Python

Um aplicativo de linha de comando (CLI) simples e eficiente para verificar a previsão do tempo e manter um histórico das suas cidades consultadas.

## 🚀 Funcionalidades

- **Consulta em Tempo Real:** Obtém o clima e a temperatura atualizada via OpenWeatherMap API.
- **Histórico Inteligente:** Armazena as últimas 10 cidades pesquisadas.
- **Auto-limpeza:** Se você pesquisar uma cidade que já está no histórico, ela sobe para o topo da lista sem criar duplicatas.
- **Interface Intuitiva:** Menu interativo com validação de dados.

## 🛠️ Tecnologias Utilizadas

- [Python 3](https://www.python.org/)
- [Requests](https://requests.readthedocs.io/): Para requisições HTTP.
- [OpenWeatherMap API](https://openweathermap.org/api): Fonte dos dados meteorológicos.
- [JSON](https://docs.python.org/3/library/json.html): Para persistência do histórico.

## 📋 Pré-requisitos

Antes de começar, você precisará ter o Python instalado em sua máquina e uma chave de API da OpenWeatherMap.

1. Instale a biblioteca `requests`:
   pip install requests

## 📂 Estrutura do Projeto
clima.py: O arquivo principal que contém a lógica do menu e chamadas de API.

persistencia.py: Módulo responsável por ler e escrever o histórico no arquivo local.

historico_cidades: Arquivo gerado automaticamente onde os dados das cidades são salvos.

## 🔧 Como Usar
Clone o repositório ou baixe os arquivos.

No terminal, navegue até a pasta do projeto.

Execute o comando: python clima.py

Escolha a opção 1 para pesquisar uma cidade ou 2 para ver quem você pesquisou recentemente.


## ⚙️ Configuração da API
No arquivo clima.py, o código utiliza uma chave de API (appid). Para uso profissional ou acadêmico prolongado, recomenda-se gerar sua própria chave gratuita no site da OpenWeather e substituir na variável url.
