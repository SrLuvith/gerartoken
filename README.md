## GerarToken - Sistema de Geração e Validação de Tokens

### O que é o GerarToken?
O GerarToken é um sistema simples e eficiente para a geração, validação e gestão de tokens, com integração de autenticação, armazenamento de dados e suporte a variáveis de ambiente para segurança. Ele foi projetado para fornecer uma solução de tokenização de forma automatizada, ideal para aplicações que necessitam de controle de acesso com base em tokens de autenticação. Além disso, ele oferece um fluxo de validação de tokens baseado em tempo, onde a expiração do token é definida pelo número de dias adquiridos pelo usuário.

### ➨ Funcionalidades:
- **Geração de Tokens Personalizados**: Permite a criação de tokens com validade definida pelo número de dias comprados.
- **Validação de Tokens**: Garante que o token seja validado dentro de um período específico, expirando caso contrário.
- **Envio Automático de Emails**: Integra com SMTP para envio de emails com o token gerado e agradecimentos.
- **Armazenamento Seguro**: Utiliza variáveis de ambiente para armazenar informações sensíveis, como senhas de SMTP.
- **Interface Web Simples**: Fornece uma interface web básica para interação do usuário com o sistema.

### ➨ Tecnologias Usadas:
- **Flask**: Framework web utilizado para criação da API e interface.
- **Werkzeug**: Biblioteca de utilitários para desenvolvimento de aplicações Python.
- **SMTP**: Protocolo para envio de emails, utilizado para enviar os tokens aos usuários.
- **Git**: Controle de versão utilizado para gerenciar o código-fonte.
- **Render.com**: Plataforma de deploy para hospedar o projeto.
- **SQLite (ou JSON)**: Armazenamento de dados dos usuários e tokens.
- **Python 3.11**: Linguagem de programação utilizada no desenvolvimento do sistema.

### ➨ Como Configurar:
1. **Clonando o Repositório**: Primeiro, clone o repositório para sua máquina local.
2. **Instalação das Dependências**: Instale as dependências necessárias listadas no `requirements.txt`.
3. **Configuração das Variáveis de Ambiente**: Este projeto requer a configuração de variáveis de ambiente para garantir a segurança de informações sensíveis, como a senha do servidor SMTP. Para isso, crie um arquivo `.env` na raiz do projeto e adicione a chave da senha do SMTP e outras variáveis necessárias, como o e-mail de envio.
4. **Rodando o Projeto Localmente**: Para rodar o projeto localmente, basta executar o comando especificado. O servidor estará disponível em `http://127.0.0.1:5000/`.
5. **Deploy no Render**: Se você deseja realizar o deploy no Render.com, siga as etapas de configuração e obtenção de variáveis de ambiente como descrito na documentação do Render.

### ➨ Como Usar:
- **Gerar um Token**: Acesse a interface web ou utilize a API para gerar um token, especificando o número de dias que deseja que o token tenha de validade. O token será enviado para o e-mail fornecido pelo usuário.
- **Validar o Token**: Após gerar o token, o usuário terá um tempo específico para validá-lo. Caso o token não seja validado dentro do prazo, o acesso será negado.
- **Reembolso de Tokens Expirados**: Se o token não for validado dentro de 10 minutos após a criação, o sistema acionará uma rotina para que o usuário possa solicitar um reembolso.

### ➨ Contribuindo
Contribuições são bem-vindas! Caso queira contribuir com melhorias ou novas funcionalidades, siga os seguintes passos:
1. Faça um fork do repositório.
2. Crie uma branch para a sua feature.
3. Faça suas alterações e commit.
4. Envie a branch para o seu repositório.
5. Crie um novo Pull Request.

### ➨ Licença
Este projeto está licenciado sob a MIT License.

### ➨ Contato
Se você tiver dúvidas ou sugestões, sinta-se à vontade para abrir uma issue ou entrar em contato diretamente.

Whatsapp: (61) 99325-4624 - Philippe.
