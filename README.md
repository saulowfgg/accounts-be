# Accounts

Este é um projeto de CRUD de contas utilizando o framework FastAPI.

## Requisitos

Certifique-se de que você tenha o Python 3.10 instalado.

## Configuração do Ambiente Virtual

É recomendado criar um ambiente virtual para isolar as dependências deste projeto. Siga os passos abaixo:

1. Abra o terminal na pasta do projeto.

2. Crie o ambiente virtual:
   ```bash
   python3.10 -m venv .venv

3. Ative o ambiente virtual:
 - No Windows:
    ```bash
    .venv\Scripts\activate

 - No macOS e Linux:
    ```bash
    source .venv/bin/activate

## Instalação das Dependências

Com o ambiente virtual ativado, instale as dependências do projeto usando o comando:

    pip install -r requirements.txt

## Executando o Projeto

Após a instalação das dependências, você pode executar o projeto com o comando:

    uvicorn main:app --reload

Isso iniciará o servidor e você poderá acessar a aplicação em http://localhost:8000.

Lembre-se de desativar o ambiente virtual quando não estiver mais usando o projeto:

    deactivate
