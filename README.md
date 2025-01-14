<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GerarToken - Sistema de Geração e Validação de Tokens</title>
</head>
<body style="font-family: Arial, sans-serif; margin: 20px; line-height: 1.6;">
    <h1>GerarToken - Sistema de Geração e Validação de Tokens</h1>
    <h2>O que é o GerarToken?</h2>
    <p>
        O GerarToken é um sistema simples e eficiente para a geração, validação e gestão de tokens, com integração de autenticação, armazenamento de dados e suporte a variáveis de ambiente para segurança. Ele foi projetado para fornecer uma solução de tokenização de forma automatizada, ideal para aplicações que necessitam de controle de acesso com base em tokens de autenticação. Além disso, ele oferece um fluxo de validação de tokens baseado em tempo, onde a expiração do token é definida pelo número de dias adquiridos pelo usuário.
    </p>

    <h3>➨ Funcionalidades:</h3>
    <ul>
        <li>Geração de Tokens Personalizados: Permite a criação de tokens com validade definida pelo número de dias comprados.</li>
        <li>Validação de Tokens: Garante que o token seja validado dentro de um período específico, expirando caso contrário.</li>
        <li>Envio Automático de Emails: Integra com SMTP para envio de emails com o token gerado e agradecimentos.</li>
        <li>Armazenamento Seguro: Utiliza variáveis de ambiente para armazenar informações sensíveis, como senhas de SMTP.</li>
        <li>Interface Web Simples: Fornece uma interface web básica para interação do usuário com o sistema.</li>
    </ul>

    <h3>➨ Tecnologias Usadas</h3>
    <ul>
        <li>Flask: Framework web utilizado para criação da API e interface.</li>
        <li>Werkzeug: Biblioteca de utilitários para desenvolvimento de aplicações Python.</li>
        <li>SMTP: Protocolo para envio de emails, utilizado para enviar os tokens aos usuários.</li>
        <li>Git: Controle de versão utilizado para gerenciar o código-fonte.</li>
        <li>Render.com: Plataforma de deploy para hospedar o projeto.</li>
        <li>SQLite (ou JSON): Armazenamento de dados dos usuários e tokens.</li>
        <li>Python 3.11: Linguagem de programação utilizada no desenvolvimento do sistema.</li>
    </ul>

    <h3>➨ Como Configurar</h3>
    <ol>
        <li><strong>Clonando o Repositório:</strong> Primeiro, clone o repositório para sua máquina local.</li>
        <li><strong>Instalação das Dependências:</strong> Instale as dependências necessárias listadas no requirements.txt.</li>
        <li><strong>Configuração das Variáveis de Ambiente:</strong> Este projeto requer a configuração de variáveis de ambiente para garantir a segurança de informações sensíveis, como a senha do servidor SMTP. Para isso, crie um arquivo .env na raiz do projeto e adicione a chave da senha do SMTP e outras variáveis necessárias, como o e-mail de envio.</li>
        <li><strong>Rodando o Projeto Localmente:</strong> Para rodar o projeto localmente, basta executar o comando especificado. O servidor estará disponível em http://127.0.0.1:5000/.</li>
        <li><strong>Deploy no Render:</strong> Se você deseja realizar o deploy no Render.com, siga as etapas de configuração e obtenção de variáveis de ambiente como descrito na documentação do Render.</li>
    </ol>

    <h3>➨ Como Usar</h3>
    <ul>
        <li><strong>Gerar um Token:</strong> Acesse a interface web ou utilize a API para gerar um token, especificando o número de dias que deseja que o token tenha de validade. O token será enviado para o e-mail fornecido pelo usuário.</li>
        <li><strong>Validar o Token:</strong> Após gerar o token, o usuário terá um tempo específico para validá-lo. Caso o token não seja validado dentro do prazo, o acesso será negado.</li>
        <li><strong>Reembolso de Tokens Expirados:</strong> Se o token não for validado dentro de 10 minutos após a criação, o sistema acionará uma rotina para que o usuário possa solicitar um reembolso.</li>
    </ul>

    <h3>➨ Contribuindo</h3>
    <p>Contribuições são bem-vindas! Caso queira contribuir com melhorias ou novas funcionalidades, siga os seguintes passos:</p>
    <ol>
        <li>Faça um fork do repositório.</li>
        <li>Crie uma branch para a sua feature.</li>
        <li>Faça suas alterações e commit.</li>
        <li>Envie a branch para o seu repositório.</li>
        <li>Crie um novo Pull Request.</li>
    </ol>

    <h3>➨ Licença</h3>
    <p>Este projeto está licenciado sob a MIT License.</p>

    <h3>➨ Contato</h3>
    <p>Se você tiver dúvidas ou sugestões, sinta-se à vontade para abrir uma issue ou entrar em contato diretamente.</p>
    <p>Whatsapp: (61) 99325-4624 - Philippe.</p>
</body>
</html>
