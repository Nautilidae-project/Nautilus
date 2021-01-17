import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import mimetypes


def enviaEmail(titulo, mensagem, emailDestino, arquivo=None):
    try:
        # Configuração
        # usuario = 'seu e-mail'
        # senha = 'sua senha do e-mail'
        usuario = 'bustalefoo@gmail.com'
        senha = 'bustalefo@22'

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

        if arquivo != None:
            anexo = open(arquivo, 'rb')

            mimetype_anexo = mimetypes.guess_type(arquivo)[0].split('/')
            tipoDeArquivo = MIMEBase(mimetype_anexo[0], mimetype_anexo[1])

            tipoDeArquivo.set_payload(anexo.read())
            encoders.encode_base64(tipoDeArquivo)
            tipoDeArquivo.add_header('Content-Disposition', 'attachament; filename= %s' % arquivo.split('/')[-1])
            email_msg.attach(tipoDeArquivo)

        # Enviando mensagem
        print('Enviando mensagem...')
        server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
        print('Mensagem enviada!')
        server.quit()
    except smtplib.SMTPAuthenticationError:
        print('Erro de Autenticação(SMTPAuthenticationError) --> Revise seu e-mail ou senha')
