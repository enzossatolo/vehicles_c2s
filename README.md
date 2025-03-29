# Vehicles C2S

---

## Português

### Sobre o Projeto

Vehicles C2S é uma aplicação moderna que permite buscar e filtrar veículos em um banco de dados através de um agente inteligente. O sistema utiliza conceitos de conversação e inteligência artificial para auxiliar o usuário durante a consulta, proporcionando uma experiência interativa e dinâmica na busca por veículos conforme características específicas.

### Tecnologias e Frameworks

O projeto foi desenvolvido utilizando as seguintes tecnologias e frameworks:

- **Python** – Linguagem de programação principal.
- **SQLAlchemy** – ORM para interação com o banco de dados.
- **SQLite** – Banco de dados utilizado (pode ser alterado conforme necessidade).
- **AsyncIO** – Suporte para operações assíncronas.
- **Docker** – Para execução encapsulada e consistente da aplicação.
- **LangChain** – Framework para criação de agentes inteligentes e manipulação de linguagem natural.
- **MCP** – Ferramenta para comunicação entre processos (client/server) muito utilizada em agentes de LLM.

### Executando o Projeto em um Container Docker

#### Pré-requisitos

- Docker instalado na máquina.
- Crie um arquivo `.env` na raiz do projeto com as variáveis necessárias (OPENAI_API_KEY).
- Acesso ao Makefile para facilitar a execução (opcional).

#### Rodando com Makefile
```bash
make all
```

#### Rodando Sem o Makefile

1. **Build do container:**
   ```bash
   docker build -t vehicles-c2s .
   ```
2. **Executar o container:**
   ```bash
   docker run -it --rm vehicles-c2s bash
   ```
> Observação: Após entrar no container, no primeiro uso, crie e popule o banco de dados com:
> ```bash
> python -m src.scripts.populate_db
> ```
> Em seguida, para executar o agente com o MCP Client, rode:
> ```bash
> python -m src.services.mcp.client
> ```

### Executando o Projeto Localmente (Fora do Container)

#### Pré-requisitos

- Python 3.10+ instalado.
- Dependências instaladas via pip (utilize o `requirements.txt`):
  ```bash
  pip install -r requirements.txt
  ```

#### Instruções de Execução

1. **Configuração do ambiente:**
   - Crie um arquivo `.env` na raiz do projeto com a variável `OPENAI_API_KEY` e outras configurações necessárias.
   - Defina a variável de ambiente `PYTHONPATH` apontando para a raiz do projeto para que o Python localize os módulos corretamente:
     - **No Linux/Mac:**  
       Abra o terminal e execute:
       ```bash
       export PYTHONPATH=$(pwd)
       ```
     - **No Windows (cmd.exe):**  
       Abra o prompt de comando e execute:
       ```cmd
       set PYTHONPATH=%cd%
       ```
     - **No Windows (PowerShell):**  
       Abra o PowerShell e execute:
       ```powershell
       $env:PYTHONPATH = Get-Location
       ```
2. **Criação e população do banco de dados (apenas no primeiro uso):**
   ```bash
   python -m src.scripts.populate_db
   ```
3. **Executando o agente MCP Client:**
   ```bash
   python -m src.services.mcp.client
   ```

---

## English

### About the Project

Vehicles C2S is a modern application that enables users to search and filter vehicles in a database using an intelligent agent. The system leverages conversational concepts and artificial intelligence to assist the user during the query, providing an interactive and dynamic experience when searching for vehicles based on specific characteristics.

### Technologies and Frameworks

The project was developed using the following technologies and frameworks:

- **Python** – The main programming language.
- **SQLAlchemy** – ORM for database interactions.
- **SQLite** – The database used (can be modified as needed).
- **AsyncIO** – Support for asynchronous operations.
- **Docker** – For a encapsulated and consistent deployment of the application.
- **LangChain** – Framework for building intelligent agents and language manipulation.
- **MCP** – A tool used for inter-process communication (client/server), widely used in LLM agents.

### Running the Project in a Docker Container

#### Prerequisites

- Docker installed on your machine.
- Create a `.env` file at the project root with the necessary variables (e.g., OPENAI_API_KEY).
- Optionally, use the provided Makefile to simplify execution.

#### Running with Makefile
```bash
make all
```

#### Running Without the Makefile

1. **Build the container:**
   ```bash
   docker build -t vehicles-c2s .
   ```
2. **Run the container:**
   ```bash
   docker run -it --rm vehicles-c2s bash
   ```
> Note: Once inside the container, for the first time, create and populate the database by running:
> ```bash
> python -m src.scripts.populate_db
> ```
> Then, to run the MCP Client agent, execute:
> ```bash
> python -m src.services.mcp.client
> ```

### Running the Project Locally (Outside the Container)

#### Prerequisites

- Python 3.10+ installed.
- Install dependencies with pip (using `requirements.txt`):
  ```bash
  pip install -r requirements.txt
  ```

#### Execution Instructions

1. **Environment Setup:**
   - Create a `.env` file at the project root with the OPENAI_API_KEY variable and other necessary configurations.
   - Define the `PYTHONPATH` environment variable pointing to the project root so that Python can locate the modules correctly:
     - **On Linux/Mac:**  
       Open the terminal and run:
       ```bash
       export PYTHONPATH=$(pwd)
       ```
     - **On Windows (cmd.exe):**  
       Open the command prompt and run:
       ```cmd
       set PYTHONPATH=%cd%
       ```
     - **On Windows (PowerShell):**  
       Open PowerShell and run:
       ```powershell
       $env:PYTHONPATH = Get-Location
       ```
2. **Create and Populate the Database (only for the first run):**
   ```bash
   python -m src.scripts.populate_db
   ```
3. **Running the MCP Client Agent:**
   ```bash
   python -m src.services.mcp.client
   ```
