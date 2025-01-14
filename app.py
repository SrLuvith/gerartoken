import logging, smtplib, json, random, string, os, re
from flask import Flask, render_template, request, redirect, url_for, jsonify, session, flash
from datetime import datetime, timedelta
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import secrets

# Configuração do Flask
app = Flask(__name__)
app.secret_key = 'chave-secreta'

# Configuração do SMTP
app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=587,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='suacadela13@gmail.com',
    MAIL_PASSWORD=os.getenv('SMTP_PASSWORD'),
    MAIL_DEFAULT_SENDER='"SuaCadela.com" <suacadela13@gmail.com>'
)

# Caminho do banco de dados JSON
DATABASE = 'database.json'

# Função de configuração de logging
def setup_logging():
    logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info('Sistema de logs iniciado.')
    token_handler = logging.FileHandler('log_tokens.log')
    token_handler.setLevel(logging.DEBUG)
    token_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
    logging.getLogger('token_logger').addHandler(token_handler)

setup_logging()

# Função para obter ou inicializar o banco de dados
def get_db():
    try:
        if not os.path.exists(DATABASE):
            with open(DATABASE, 'w') as db_file:
                json.dump({"tokens": []}, db_file)
        with open(DATABASE, 'r') as db_file:
            data = json.load(db_file)
        if isinstance(data, dict) and "tokens" not in data:
            logging.error('Estrutura do banco de dados inválida, chave "tokens" não encontrada.')
            data = {"tokens": []}
            with open(DATABASE, 'w') as db_file:
                json.dump(data, db_file)
        elif not isinstance(data, dict):
            logging.error('Estrutura do banco de dados inválida, esperando um dicionário.')
            data = {"tokens": []}
            with open(DATABASE, 'w') as db_file:
                json.dump(data, db_file)
        logging.info('Conexão com o banco de dados realizada com sucesso.')
        return data
    except (json.JSONDecodeError, Exception) as e:
        logging.error(f'Erro ao conectar ao banco de dados: {e}')
        return {"tokens": []}

# Função para gerar o token e credenciais aleatórias
def gerar_token_logica(dias_validade):
    try:
        token = secrets.token_hex(16)
        data_expiracao = datetime.now() + timedelta(minutes=10)
        logging.info(f'Token gerado: {token}, Data de Expiração: {data_expiracao}')
        return token, data_expiracao
    except Exception as e:
        logging.error(f'Erro ao gerar token: {e}')
        raise

def gerar_credenciais():
    try:
        login = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        senha = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        logging.info(f'Credenciais geradas: Login - {login}, Senha - {senha}')
        return login, senha
    except Exception as e:
        logging.error(f'Erro ao gerar credenciais: {e}')
        raise

# Função para enviar e-mail
def enviar_email(destinatario, nome, login, senha, validade, valor):
    try:
        remetente, senha_email = app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD']
        html_content = f"""
        <html><body>
            <p><strong>Nome:</strong> {nome}</p>
            <p><strong>Login:</strong> {login}</p>
            <p><strong>Senha:</strong> {senha}</p>
            <p><strong>Validade:</strong> {validade['dias']} dias</p>
            <p><strong>Valor:</strong> R${valor}</p>
        </body></html>
        """
        msg = MIMEMultipart()
        msg['From'], msg['To'], msg['Subject'] = remetente, destinatario, "Credenciais Geradas com Sucesso!"
        msg.attach(MIMEText(html_content, 'html'))
        with smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT']) as server:
            server.starttls()
            server.login(remetente, senha_email)
            server.sendmail(remetente, destinatario, msg.as_string())
        logging.info(f'E-mail enviado com sucesso para {destinatario}.')
        return True
    except Exception as e:
        logging.error(f'Erro ao enviar e-mail para {destinatario}: {e}')
        return False

# Função para salvar e carregar tokens
def salvar_token(token, nome, email, cpf, login, senha, data_expiracao, valor):
    try:
        data = get_db()
        token_data = {
            "token": token, "nome": nome, "email": email, "cpf": cpf, 
            "login": login, "senha": senha, "data_expiracao": data_expiracao.strftime('%Y-%m-%d %H:%M:%S'), "valor": valor
        }
        data['tokens'].append(token_data)
        with open(DATABASE, 'w') as db_file:
            json.dump(data, db_file)
        logging.info(f'Token {token} salvo no banco de dados com sucesso.')
    except Exception as e:
        logging.error(f'Erro ao salvar o token {token} no banco de dados: {e}')

def carregar_banco_de_dados():
    try:
        data = get_db()
        logging.info(f'Dados carregados do banco de dados: {data["tokens"]}')
        return data["tokens"]
    except Exception as e:
        logging.error(f'Erro ao carregar dados do banco: {e}')

# Função para verificar e-mail
def validar_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    valid = bool(re.match(regex, email))
    if valid:
        logging.info(f'E-mail {email} válido.')
    else:
        logging.warning(f'E-mail {email} inválido.')
    return valid

# Função para login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_usuario, senha = request.form['login'], request.form['senha']
        dados = carregar_banco_de_dados()
        for row in dados:
            if row['login'] == login_usuario and row['senha'] == senha:
                logging.info(f'Login bem-sucedido para {login_usuario}.')
                return redirect(url_for('dashboard'))
        logging.warning(f'Login falhou para {login_usuario}.')
        flash('Credenciais inválidas', 'error')
        return redirect(url_for('login'))
    return render_template('login.html')

# Função para gerar token
@app.route('/gerar_token', methods=['POST', 'GET'])
def gerar_token():
    if request.method == 'POST':
        if all(k in request.form for k in ['dias_validade', 'email', 'cpf', 'nome']):
            dias_validade = int(request.form['dias_validade'])
            token, data_expiracao = gerar_token_logica(dias_validade)
            login, senha = gerar_credenciais()
            nome, email, cpf = request.form['nome'], request.form['email'], request.form['cpf']
            valor = dias_validade * 1.35
            if enviar_email(email, nome, login, senha, {'dias': dias_validade}, valor):
                salvar_token(token, nome, email, cpf, login, senha, data_expiracao, valor)
                logging.info(f'Token {token} gerado e salvo com sucesso.')
                return redirect(url_for('sucesso'))
            else:
                logging.error('Erro ao enviar o e-mail.')
                return render_template('erro.html', mensagem="Erro ao processar a solicitação.")
        else:
            logging.error('Dados faltando no formulário.')
            return jsonify({"status": "erro", "mensagem": "Dados faltando no formulário."}), 400
    return render_template('gerar_token.html')

# Página de sucesso
@app.route('/sucesso')
def sucesso():
    return render_template('sucesso.html')

# Página do dashboard
@app.route('/dashboard')
def dashboard():
    tokens = carregar_banco_de_dados()
    now = datetime.now()
    expired_tokens = [token for token in tokens if datetime.strptime(token['data_expiracao'], '%Y-%m-%d %H:%M:%S') < now]
    active_tokens = [token for token in tokens if datetime.strptime(token['data_expiracao'], '%Y-%m-%d %H:%M:%S') >= now]
    return render_template('dashboard.html', tokens=tokens, now=now, expired_tokens=expired_tokens, active_tokens=active_tokens)

# Página inicial
@app.route('/')
def home():
    return render_template('login.html')

# Inicializar banco de dados
def init_db():
    if not os.path.exists(DATABASE):
        with open(DATABASE, 'w') as db_file:
            json.dump({"tokens": []}, db_file)

init_db()

# Executar a aplicação
if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))  # Porta dinâmica da Render ou 5000 por padrão
    app.run(host="0.0.0.0", port=port, debug=True)  # 0.0.0.0 permite acesso externo
