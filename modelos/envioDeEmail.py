import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuração
usuario = 'seu e-mail'
senha = 'sua senha'

# Criando objeto
print('Criando objeto servidor...')
server = smtplib.SMTP('smtp.gmail.com', 587)  # servidor e porta

# Login com servidor
print('Login...')
server.ehlo()  # estabelecermos a conexão com o servidor;
server.starttls()  # precisaremos chamar a função starttls(), que irá criptografar nossa conexão;
server.login(usuario, senha)  #  logar nossas credenciais no servidor;

"""
O Google, inicialmente, não vai te permitir realizar o login via smtplib porque por padrão,
ele considera esse tipo de conexão usando software ou código não identificado como “menos segura”.

Para resolver isso é bem tranquilo, basta logar na sua conta do Google e acessar o link a seguir:
https://www.google.com/settings/security/lesssecureapps

Mude para “ON” a oção de “Allow less secure apps”
"""

# Criando mensagem
emailDestino = 'email de destino'
mensagem = 'Mensagem - Um Testes Qualquer de Envio de Mensagem de Email!!'
print('Criando mensagem...')
email_msg = MIMEMultipart()
email_msg['Subject'] = 'Titulo - Testes Envio de e mail com smtplib'
email_msg['From'] = usuario
email_msg['To'] = emailDestino
print('Adicionando texto...')
email_msg.attach(MIMEText(mensagem, 'plain'))

# Enviando mensagem
print('Enviando mensagem...')
server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
# server.sendmail(msg['From'], msg['To'], msg.as_string())
print('Mensagem enviada!')
server.quit()