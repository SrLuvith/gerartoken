from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import datetime
import secrets
import smtplib
import json
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = 'chave-secreta'

# Configuração do SMTP
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'suacadela13@gmail.com'
app.config['MAIL_PASSWORD'] = 'rwdz mvxk gqzy kqry'
app.config['MAIL_DEFAULT_SENDER'] = '"SuaCadela.com" <suacadela13@gmail.com>'

# Função para gerar um token
def gerar_token_logica(dias_validade):
    token = secrets.token_hex(16)  # Gera um token aleatório
    data_expiracao = datetime.now() + timedelta(days=dias_validade)  # Define a data de expiração
    return token, data_expiracao

# Função para gerar credenciais aleatórias (login e senha)
def gerar_credenciais():
    login = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))  # Login aleatório
    senha = ''.join(random.choices(string.ascii_letters + string.digits, k=12))  # Senha aleatória
    return login, senha

# Função para enviar o e-mail com o modelo HTML
def enviar_email(destinatario, nome, login, senha, validade, valor):
    remetente = app.config['MAIL_USERNAME']
    senha_email = app.config['MAIL_PASSWORD']

    # Modelo do e-mail em HTML
    html_content = f"""
    <html>
        <body style="font-family: 'Arial', sans-serif; background-color: #f8f9fa; color: #333; padding: 20px;">
            <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                <div style="background-color: #4CAF50; color: white; padding: 10px 20px; text-align: center; border-radius: 8px 8px 0 0;">
                    <h1 style="margin: 0;">Credenciais Geradas com Sucesso!</h1>
                </div>
                <div style="padding: 20px; font-size: 16px; line-height: 1.5;">
                    <p>Olá, {nome},</p>
                    <p>Suas credenciais de acesso foram geradas com sucesso. Veja os detalhes abaixo:</p>
                    <p><strong>Login:</strong> {login}</p>
                    <p><strong>Senha:</strong> {senha}</p>
                    <p><strong>Validade:</strong> {validade['dias']} dias</p>
                    <p><strong>Valor Pago:</strong> <span style="font-size: 16px; color: #555;">R$ {valor:.2f}</span></p>
                    <p><strong>Como funciona:</strong> As credenciais têm validade conforme especificado acima. Após a expiração, você não poderá mais utilizá-las. A contagem regressiva do tempo restante será atualizada automaticamente para que você saiba exatamente quanto tempo ainda tem para usar o token.</p>
                    <p>Clique no botão abaixo para acessar sua conta:</p>
                    <a href="http://localhost:5000/login" style="display: inline-block; padding: 10px 20px; background-color: #4CAF50; color: white; font-size: 16px; text-decoration: none; border-radius: 5px; margin-top: 20px;">Página de Login</a> 
                </div>
            </div>
        </body>
    </html>
    """

    # Cria o objeto de e-mail
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = "Credenciais Geradas com Sucesso!"

    # Anexa o conteúdo HTML no corpo do e-mail
    msg.attach(MIMEText(html_content, 'html'))

    try:
        with smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT']) as server:
            server.starttls()
            server.login(remetente, senha_email)
            server.sendmail(remetente, destinatario, msg.as_string())
        return True
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        return False

# Função para carregar o banco de dados
def carregar_banco_de_dados():
    try:
        with open('database.json', 'r') as f:
            dados = json.load(f)
            if not isinstance(dados, dict):  # Verifica se os dados carregados são um dicionário
                return {}
            return dados
    except FileNotFoundError:
        return {}

# Função para salvar dados no banco
def salvar_banco_de_dados(data):
    with open('database.json', 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/')
def home():
    return redirect(url_for('gerar_token'))  # Redireciona para a rota gerar_token

@app.route('/gerar_token', methods=['GET', 'POST'])
def gerar_token():
    if request.method == 'POST':
        try:
            nome = request.form['nome']  # Obtém o nome do formulário
            email = request.form['email']  # Obtém o e-mail do formulário
            cpf = request.form['cpf']  # Obtém o CPF do formulário
            dias = int(request.form['dias'])  # Obtém o número de dias para o token

            # Gera o token e a data de expiração chamando uma função interna
            token, data_expiracao = gerar_token_logica(dias)  # Corrigido para chamar gerar_token_logica()

            # Gera credenciais aleatórias
            login, senha = gerar_credenciais()

            # Carrega o banco de dados
            dados = carregar_banco_de_dados()

            # Armazena o token, login e senha no banco de dados
            dados[token] = {
                'login': login,
                'senha': senha,
                'data_expiracao': data_expiracao.strftime('%Y-%m-%d %H:%M:%S'),  # Usando o formato sem 'T'
                'email': email,
                'cpf': cpf,
            }

            # Salva as alterações no banco de dados
            salvar_banco_de_dados(dados)

            # Envia o e-mail com as credenciais para o usuário
            email_enviado = enviar_email(email, nome, login, senha, {'dias': dias}, dias * 1.35)

            if email_enviado:
                return render_template('gerar_token.html', token=token, data_expiracao=data_expiracao.strftime('%Y-%m-%d %H:%M:%S'))
            else:
                return jsonify({"error": "Erro ao enviar e-mail com as credenciais."}), 500

        except ValueError:
            return jsonify({"error": "Número de dias inválido"}), 400

    return render_template('gerar_token.html')

@app.route('/login', methods=['GET', 'POST'])
def login_view():
    if request.method == 'POST':
        login_informado = request.form['login']
        senha_informada = request.form['senha']

        # Carrega o banco de dados
        dados = carregar_banco_de_dados()

        # Verifica se o login e a senha informados são válidos
        for token, info in dados.items():
            if login_informado == info['login'] and senha_informada == info['senha']:
                # Verifica a validade do token
                data_expiracao = datetime.strptime(info['data_expiracao'], '%Y-%m-%d %H:%M:%S')  # Formato correto
                if data_expiracao > datetime.now():
                    return redirect(url_for('dashboard'))
                else:
                    return render_template('login.html', error="Token expirado.")
        
        # Se não encontrou o login e senha válidos
        return render_template('login.html', error="Credenciais inválidas.")

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # Carregar os dados dos tokens do banco de dados
    tokens = carregar_banco_de_dados()

    # Obtém o momento atual
    now = datetime.now()

    # Exibe o número de tokens expirados
    expired_tokens = [token for token, info in tokens.items() if datetime.strptime(info['data_expiracao'], '%Y-%m-%d %H:%M:%S') < now]

    # Filtra os tokens ativos e expirados
    active_tokens = [token for token, info in tokens.items() if datetime.strptime(info['data_expiracao'], '%Y-%m-%d %H:%M:%S') >= now]

    # Renderiza a página do dashboard com os tokens expirados e a data atual
    return render_template('dashboard.html', tokens=tokens, now=now, expired_tokens=expired_tokens, active_tokens=active_tokens)

if __name__ == '__main__':
    app.run(debug=True)
