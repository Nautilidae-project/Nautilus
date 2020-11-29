import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def enviaEmail(titulo, mensagem, emailDestino):
    try:
        # Configuração
        usuario = 'seu e-mail'
        senha = 'sua senha do e-mail'

        # Criando objeto
        print('Criando objeto servidor...')
        server = smtplib.SMTP('smtp.gmail.com', 587)  # servidor e porta

        # Login com servidor
        print('Login...')
        server.ehlo()  # estabelecermos a conexão com o servidor;
        server.starttls()  # precisaremos chamar a função starttls(), que irá criptografar nossa conexão;
        server.login(usuario, senha)  # logar nossas credenciais no servidor;

        # Criando mensagem
        print('Criando mensagem...')
        email_msg = MIMEMultipart()
        email_msg['Subject'] = titulo
        email_msg['From'] = usuario
        email_msg['To'] = emailDestino
        print('Adicionando texto...')
        email_msg.attach(MIMEText(mensagem, 'plain'))

        # Enviando mensagem
        print('Enviando mensagem...')
        server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
        print('Mensagem enviada!')
        server.quit()
    except smtplib.SMTPAuthenticationError:
        print('Erro de Autenticação(SMTPAuthenticationError) --> Revise seu e-mail ou senha')
