GerarToken - Sistema de Geração e Validação de Tokens

O que é o GerarToken?
O GerarToken é um sistema simples e eficiente criado para gerar, validar e gerenciar tokens de autenticação. Ele foi desenvolvido para aplicações que necessitam de controle de acesso baseado em tokens. A ideia é garantir uma experiência prática e segura para quem precisa de um sistema automatizado de tokenização. Um dos principais recursos do GerarToken é o controle de validade dos tokens, que expiram conforme o número de dias adquiridos pelo usuário.

Funcionalidades
Geração de Tokens Personalizados: Permite a criação de tokens com validade flexível, definida pelo número de dias adquiridos.
Validação de Tokens: Verifica se o token foi validado dentro do prazo estipulado. Caso contrário, o acesso é negado.
Envio Automático de E-mails: Integra-se com um servidor SMTP para enviar os tokens gerados diretamente para o e-mail do usuário, juntamente com agradecimentos.
Armazenamento Seguro: Usa variáveis de ambiente para armazenar informações sensíveis, como senhas de SMTP, garantindo a segurança.
Interface Web Intuitiva: Oferece uma interface web simples para facilitar a interação dos usuários com o sistema.
Tecnologias Utilizadas
Flask: Framework web utilizado para a criação da API e da interface do sistema.
Werkzeug: Biblioteca de utilitários para auxiliar no desenvolvimento da aplicação.
SMTP: Protocolo utilizado para o envio de e-mails, garantindo que os tokens cheguem aos usuários com facilidade.
Git: Sistema de controle de versão usado para gerenciar o código-fonte.
Render.com: Plataforma de deploy utilizada para hospedar o projeto na nuvem.
SQLite (ou JSON): Sistema de armazenamento dos dados dos usuários e dos tokens.
Python 3.11: Linguagem de programação utilizada para o desenvolvimento do sistema.
Como Configurar
Clonando o Repositório
Para começar, clone o repositório para o seu ambiente local.

Instalando as Dependências
Instale as dependências necessárias listadas no arquivo requirements.txt.

Configurando as Variáveis de Ambiente
Este projeto requer que você configure variáveis de ambiente para garantir a segurança dos dados sensíveis, como a senha do servidor SMTP. Para isso, crie um arquivo .env na raiz do projeto e adicione as informações necessárias, como as credenciais do servidor SMTP.

Rodando o Projeto Localmente
Com tudo configurado, basta rodar o projeto localmente. O servidor estará disponível em http://127.0.0.1:5000/.

Deploy no Render
Se você deseja realizar o deploy na plataforma Render.com, siga as etapas de configuração do Render para garantir que as variáveis de ambiente sejam configuradas corretamente.

Como Usar
Gerar um Token
Para gerar um token, você pode acessar a interface web ou utilizar a API. Ao gerar o token, você escolhe o número de dias de validade e o token será enviado para o e-mail informado.

Validar o Token
Após a geração, o token precisa ser validado dentro de um prazo. Caso o token não seja validado dentro do tempo estipulado, o acesso será negado.

Reembolso de Tokens Expirados
Se o token não for validado dentro de 10 minutos após a criação, o sistema permitirá que o usuário solicite um reembolso.

Contribuindo
Contribuições são sempre bem-vindas! Se você deseja melhorar o projeto ou adicionar novas funcionalidades, basta seguir esses passos:

Faça um fork do repositório.
Crie uma nova branch para a sua feature.
Faça as modificações e commit.
Envie a branch para o seu repositório.
Crie um Pull Request para o repositório principal.
Licença
Este projeto está licenciado sob a MIT License.

Contato
Se você tiver dúvidas ou sugestões, fique à vontade para abrir uma issue ou entrar em contato diretamente.