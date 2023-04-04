import smtplib
from lib.funcoes import menssagem
from datetime import date, timedelta
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email:
    def __init__(self, email, pwd, voucher):
        self.email = email
        self.pwd = pwd
        self.voucher = voucher
        self.caminho = 'D:\\scripts\\automacoes\\envio_voucher_wifi_viajantes\\'
    def conectarServidor(self):
        try:
            server = smtplib.SMTP(host='smtp.office365.com', port=587)
            server.set_debuglevel(1)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(self.email, self.pwd)
            return server
        except Exception as e:
            menssagem('Erro ao conectar ao servidor de email. Verifique se o email ou a senha estão corretas, caso estejam entre em  contato com o administrador.')

    
    def enviarEmail(self, server):
        attachment = open(f'{self.caminho}imagem_senha\\senha_wifi.pdf', 'rb')

        # pegando o arquivo do modo binario e convertendo em base 64 (é o que o email precisa)
        att = MIMEBase('application', 'octet-stream')
        att.set_payload(attachment.read())
        encoders.encode_base64(att)

        # Adicionamos o cabecalho no tipo anexo de email
        att.add_header('Content-Disposition', f'attachment; filename= senha_wifi.pdf')
        attachment.close()
        menssagem("Montando corpo do email.", "Quase lá, montando corpo do email.", 2000)
        
        # 2- Montando corpo do email
        corpo = f'''
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
        </head>
        <body style="background-color: #eeeeee">
            <div style="text-align: center;">
                <h1>Olá, Segue o novo voucher do mes {date.today().month + 1}</h1>
            </div>
            <div>
                <h1 style="text-align: center;padding:80px;font-size:45px;">{self.voucher}</h1>
                    <p style="text-align: center;font-family:verdana;font-size:15px">Este é o novo voucher para rede "Viajantes". Ele é válido até
                        <mark>{format(date.today() + timedelta(30), "%d/%m/%Y")}</mark>.</p>
                    <p style="text-align: center;font-family:verdana;font-size:15px">Em caso de dúvidas ou houver algum problema com o voucher enviado,
                        informar o responsável pelo controle da internet.</p>
                    <p style="text-align: center;margin-top:45px;font-family:Monospace, Lucida console;font-size:18px;">Este e-mail é automatico. Por favor não responder.</p>
            </div>
            <br><br>
            <hr>
            <div>
                <footer style="background-color: #eaeaea">
                    <table>
                        <tr>
                            <td style="font-family:arial;font-size:12px;padding-left:10px;">
                                <strong style="font-family:garamond; font-size:16px">Desenvolvido por: </strong> Seu nome aqui.<br>
                                <i><small> Seu cargo aqui </small></i><br>
                                <ul>
                                    <h3><strong>Contato</strong></h3>
                                    <li><strong>Telefone: (00) 0 0000-0000</strong></li>
                                    <li><strong>E-mail: </strong><a href="mailto:">Clique aqui</a> e entre em contato. </li>
                                    <li><strong>LinkedIn: </strong> Veja meu linkedIn <a href="https://www.linkedin.com/in//">Clicando aqui</a>. </li>
                                    <li><strong>GitHub : </strong> Veja meu Github <a href="https://github.com/">clicando aqui</a>. </li>
                                </ul>
                            </td>
                        </tr>
                    </table>
                </footer>
            </div>
        </body>
        </html>
        '''

        email_message = MIMEMultipart()
        email_message['From'] = self.email
        with open(f'{self.caminho}dados\\emails.txt', 'r') as emails:
            email = [x.strip() for x in emails.readlines()]
            for x in email:
                email_message['Subject'] = 'Voucher Wi-fi (Favor não responder)'
                email_message.attach(MIMEText(corpo, 'html', 'utf-8'))
                # colocamos o anexo no corpo do email.
                email_message.attach(att)
                menssagem("Enviando email.", f"Enviando email para {x}.", 1500)
                server.sendmail(email_message['From'], x, email_message.as_string())
            server.close()
