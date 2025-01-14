# GerarToken - Sistema de Geração e Validação de Tokens

## 🚀 O que é o GerarToken?

O **GerarToken** é um sistema simples e eficiente para a geração, validação e gestão de tokens, com integração de autenticação, armazenamento de dados e suporte a variáveis de ambiente para segurança. Ele foi projetado para fornecer uma solução de tokenização de forma automatizada, ideal para aplicações que necessitam de controle de acesso com base em tokens de autenticação. Além disso, ele oferece um fluxo de validação de tokens baseado em tempo, onde a expiração do token é definida pelo número de dias adquiridos pelo usuário.

### Funcionalidades:
- **Geração de Tokens Personalizados:** Permite a criação de tokens com validade definida pelo número de dias comprados.
- **Validação de Tokens:** Garante que o token seja validado dentro de um período específico, expirando caso contrário.
- **Envio Automático de Emails:** Integra com SMTP para envio de emails com o token gerado e agradecimentos.
- **Armazenamento Seguro:** Utiliza variáveis de ambiente para armazenar informações sensíveis, como senhas de SMTP.
- **Interface Web Simples:** Fornece uma interface web básica para interação do usuário com o sistema.

## 🛠 Tecnologias Usadas

- **Flask:** Framework web utilizado para criação da API e interface.
- **Werkzeug:** Biblioteca de utilitários para desenvolvimento de aplicações Python.
- **SMTP:** Protocolo para envio de emails, utilizado para enviar os tokens aos usuários.
- **Git:** Controle de versão utilizado para gerenciar o código-fonte.
- **Render.com:** Plataforma de deploy para hospedar o projeto.
- **SQLite (ou JSON):** Armazenamento de dados dos usuários e tokens.
- **Python 3.11:** Linguagem de programação utilizada no desenvolvimento do sistema.

## 🔧 Como Configurar

### 1. Clonando o Repositório

Primeiro, clone o repositório para sua máquina local:

```bash
git clone https://github.com/SrLuvith/gerartoken.git
cd gerartoken
