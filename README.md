# 🚀 TaskFlow: CRUD Simples em Python (Atividade SENAI)

Este projeto consiste em uma aplicação de console simples em Python que implementa as operações básicas de **CRUD** (Create, Read, Update, Delete) para gerenciamento de usuários e tarefas.

O projeto foi desenvolvido como **Atividade Prática** do módulo de Banco de Dados/Programação, utilizando o MariaDB (ou MySQL) como sistema gerenciador.

---

## 📸 Demonstração

A imagem abaixo ilustra a estrutura do código Python (`main.py`) e a visualização dos dados de teste na tabela `usuarios` através de um cliente de banco de dados.

<img width="1920" height="1080" alt="Código Python no VS Code e Tabela Usuarios no Banco de Dados" src="https://github.com/user-attachments/assets/f9ed7187-f440-45f6-87cd-08808fd890b7" />

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
* **Implicações:** A configuração do ambiente levou em consideração as diretrizes do Arch Linux (`PEP 668 - Externally Managed Environment`), sendo a solução preferida e mais eficiente para instalação de dependências através do gerenciador de pacotes nativo (`pacman`).

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

## 🛠️ 4. Instalação das Dependências e Execução

### A. Instalação (Solução Recomendada para Arch/CachyOS)

Devido às políticas do Arch Linux, a maneira mais estável e segura de instalar o driver Python é usando o gerenciador de pacotes do sistema:

```bash
sudo pacman -S python-mysql-connector
