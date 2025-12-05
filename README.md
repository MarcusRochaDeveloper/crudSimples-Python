# 🚀 TaskFlow: CRUD Simples em Python (Atividade SENAI)

Este projeto consiste em uma aplicação de console simples em Python que implementa as operações básicas de **CRUD** (Create, Read, Update, Delete) para gerenciamento de usuários e tarefas.

O projeto foi desenvolvido como **Atividade Prática** do módulo de Banco de Dados/Programação, utilizando o MariaDB (ou MySQL) como sistema gerenciador.

---

## 💻 1. Tecnologias Envolvidas

| Componente | Tecnologia | Versão |
| :--- | :--- | :--- |
| **Linguagem Principal** | Python | 3.x |
| **Banco de Dados** | MariaDB / MySQL | 10.x / 8.x |
| **Driver de Conexão** | `mysql-connector-python` | Latest |

---

## 🐧 2. Ambiente de Desenvolvimento

Esta atividade foi desenvolvida e testada integralmente em um ambiente **Linux**.

* **Sistema Operacional:** CachyOS (Base Arch Linux).
* **Implicações:** A configuração do ambiente seguiu as boas práticas do Linux, sendo obrigatório o uso de **Ambiente Virtual (`venv`)** para gerenciamento de dependências, conforme as diretrizes da **PEP 668** (evitando o erro `externally-managed-environment`).

---

## 📋 3. Pré-requisitos e Setup do Banco de Dados

Antes de executar a aplicação Python, o banco de dados deve ser configurado.

### A. Criação do Banco

1.  Garanta que o MariaDB ou MySQL esteja instalado e rodando.
2.  Execute o script SQL completo fornecido na atividade: `script_taskflow.sql`.
3.  O script criará o banco **`taskflow_db`** e as tabelas **`usuarios`** e **`tarefas`** com todas as regras de `COLLATION` (`utf8mb4_unicode_ci`), chaves primárias, chaves estrangeiras (`ON DELETE CASCADE`) e índices de performance.

### B. Credenciais de Acesso

O arquivo `main.py` está configurado para tentar se conectar usando as seguintes credenciais padrão:

| Parâmetro | Valor Padrão |
| :--- | :--- |
| **Host** | `localhost` |
| **Usuário** | `root` |
| **Senha** | `123456` |
| **Database** | `taskflow_db` |

**NOTA:** Se suas credenciais de acesso ao MySQL/MariaDB forem diferentes, você deve alterar os valores na função `criar_conexao` dentro do arquivo `main.py`.

---

## 🛠️ 4. Instalação e Execução (Passo a Passo)

### A. Criação e Ativação do Ambiente Virtual (venv)

1.  Navegue até o diretório raiz do projeto.
2.  Crie o ambiente virtual:
    ```bash
    python -m venv venv
    ```
3.  Ative o ambiente (escolha o comando de acordo com o seu shell: Bash, Zsh, Fish):
    ```bash
    # Para Bash ou Zsh:
    source venv/bin/activate
    
    # Para Fish:
    # source venv/bin/activate.fish
    ```

### B. Instalação de Dependências

Com o ambiente virtual ativado, instale o conector MySQL:

```bash
pip install mysql-connector-python
<img width="1920" height="1080" alt="Screenshot From 2025-12-04 23-32-26" src="https://github.com/user-attachments/assets/056bb448-1c1e-46fc-9c98-d7f9b3328742" />





