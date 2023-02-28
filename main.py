import datetime
import smtplib
import pymsgbox
import pdfkit

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def mensage(titulo, texto, tempo):
    criador = " Criado Por: Nome."
    return pymsgbox.alert(text=texto, title=titulo + criador, timeout=tempo)


mensage("Bem-vindo ao gerador de voucher.", "Iniciando Gerador de voucher", 3000)

edge_options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=edge_options)
tempo = lambda t: sleep(t)
driver.get('https://localhost:8443/manage/hotspot/')
tempo(3)


# Verificando se existe o botão de aviso de segurança
if driver.find_element(By.XPATH, '//*[@id="details-button"]'):
    driver.find_element(By.XPATH, '//*[@id="details-button"]').click()
    driver.find_element(By.XPATH, '//*[@id="proceed-link"]').click()

# Efetuando login
user_name = ''
password = ''
tempo(3)
campoLogin = driver.find_element(By.NAME, 'username')
campoSenha = driver.find_element(By.NAME, 'password')
botaoLogin = driver.find_element(By.ID, 'loginButton')
campoLogin.send_keys(user_name)
campoSenha.send_keys(password)
botaoLogin.click()

# Clicando no botão do voucher
tempo(5)
botaoVouchar = driver.find_element(By.XPATH, '//div[@class="ubntIcon ubntIcon--navigation icon ubnt-icon--news"]')
botaoVouchar.click()
tempo(3)
# Clicando no botão de criar novo vouver
botaoCriaVouchar = driver.find_element(By.XPATH, '//button[@title="Create vouchers"]')
botaoCriaVouchar.click()
tempo(3)
# Escolhendo Quatidade de chaver voucher que deseja criar
campoQntVoucher = driver.find_element(By.XPATH, '//input[@title="number of vouchers"]')
campoQntVoucher.send_keys(Keys.CONTROL + 'a')
campoQntVoucher.send_keys('1')
tempo(3)

# Selecionando quantos usuarios usarão o mesmo voucher
campoSelectMultUser = driver.find_element(By.XPATH, '//select//option[@label="Multi use (unlimited)"]')
campoSelectMultUser.click()
tempo(3)
with open("D:\\scripts\\automacoes\\envio_voucher_wifi_viajantes\\dados\\expire_time.txt", "r") as dias:
    dias = dias.readline()

texto = ["Data de expiração.", f"O tempo de duração do voucher é de {dias} dias. Para alterar essa data clique em ok?"]
troca_data = mensage(texto[0], texto[1], 10000)
if troca_data == 'OK':
    troca = pymsgbox.prompt("Informar a data limite:", default=30)
    with open("D:\\scripts\\automacoes\\envio_voucher_wifi_viajantes\\dados\\expire_time.txt", "w") as dias:
        dias.write(troca)
        dias = troca

# Selecionando quanto tempo durará o voucher
campoSelectTempoVoucher = driver.find_element(By.XPATH, '//select//option[@label="User-defined"]')
campoSelectTempoVoucher.click()
tempo(3)
inputDias = driver.find_element(By.XPATH, '//input[@name="expire_number"]')
inputDias.send_keys(Keys.CONTROL + 'a')
inputDias.send_keys(dias)
tempo(3)

# Definindo limite de conexão de download e upload do wifi
botaoLimiteDownload = driver.find_element(By.XPATH, '//input[@id="limitDownload"]')
botaoLimiteDownload.click()
tempo(3)
campoLimiteDownload = driver.find_element(By.XPATH, '//input[@type="number" and @name="down"]')
campoLimiteDownload.send_keys('5632')
tempo(3)
botaoLimiteUpload = driver.find_element(By.XPATH, '//input[@id="limitUpload"]')
botaoLimiteUpload.click()
tempo(3)
campoLimiteUpload = driver.find_element(By.XPATH, '//input[@type="number" and @name="up"]')
campoLimiteUpload.send_keys('5632')
tempo(3)

# salvando voucher novo.
botaoSalvaVoucher = driver.find_element(By.XPATH, '//div[@class="busyToggle__body ng-scope" and text()="Save"]')
botaoSalvaVoucher.click()
tempo(3)
voucher = driver.find_element(By.XPATH, '//table[@id="vouchersTable"]/tbody/tr[1]/td[2]').text
# fechandose navegador automatizado.
driver.quit()


mensage("Gerando PDF.", "Gerando PDF para anexo do email", 2000)
with open('imagem_senha\\voucher.html', 'w') as senha_wifi:
    imagem_senha = f'''
    <html>
<head>
<link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
<img style="position:absolute;width:10.00in;height:14.00in" src="ci_1.png" />
<div style="position:absolute;top:6.70in;left:1.80in;width:3.00in;line-height:3.50in;">
    <span style="font-style:normal;font-weight:normal;font-size:98pt;font-family:Alice;color:#000000">"Viajantes"</span>
    <span style="font-style:normal;font-weight:normal;font-size:150pt;font-family:Alice;color:#000000"> </span>
    <br/>
</div>
<div style="position:absolute;top:5.50in;left:2.94in;width:3.00in;line-height:3.40in;">
    <span style="font-style:normal;font-weight:normal;font-size:130pt;font-family:Alice;color:#000000">WIFI</span>
    <span style="font-style:normal;font-weight:normal;font-size:150pt;font-family:Alice;color:#000000"> </span>
    <br/>
</div>
<img style="position:absolute;top:8.00in;left:7.95in;width:0.90in;height:1.70in;transform:rotate(23deg);" src="ri_1.png" />
<div style="position:absolute;top:4.55in;left:2.50in;width:8.49in;line-height:2.90in;">
    <span style="font-style:normal;font-weight:normal;font-size:90pt;font-family:Alice;color:#000000">Senha do</span>
    <span style="font-style:normal;font-weight:normal;font-size:100pt;font-family:Alice;color:#000000"> </span>
    <br/>
</div>
<div style="position:absolute;top:8.60in;left:2.90in;width:6.95in;line-height:2.90in;">
    <span style="font-style:normal;font-weight:normal;font-size:60pt;font-family:Alice;color:#000000">{voucher}</span>
    <span style="font-style:normal;font-weight:normal;font-size:89pt;font-family:Alice;color:#000000"> </span>
    <br/>
</div>
</body>
</html>
    '''
    senha_wifi.write(imagem_senha)
tempo(3)
mensage("Gerando PDF", "Convertendo o PDF", 2000)
try:
    config = pdfkit.configuration(wkhtmltopdf='wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    pdfkit.from_file('imagem_senha\\voucher.html',
                     'imagem_senha\\senha.pdf',
                     configuration=config,
                     options={"enable-local-file-access": True}
                     )
except AttributeError as at:
    # Tive que colocar essa exception pq quando faço um .exe do script da esse erro de atributo
    # dizendo que AttributeError: 'NoneType' object has no attribute 'write'
    # mas quando roda o script sem ser no .exe executa normalmente sem erro algum.
    pass
tempo(3)
# Iniciando servidor para envio de email automatico
# Iniciando o servidor smtp
mensage("Conectando ao email", "Fazendo conexão ao servidor de email.", 2000)
host = "smtp.office365.com"
port = 587
login = ""
senha = ""

server = smtplib.SMTP(host=host, port=port)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
server.ehlo()
server.login(login, senha)


# abrindo o arquivo em modo leitura e binario
cam_arquivo = 'imagem_senha\\senha.pdf'
attachment = open(cam_arquivo, 'rb')

# Lemos o arquivono modo binario e jogamos codificado em base 64 ( e o que o email precisa)
att = MIMEBase('application', 'octet-stream')
att.set_payload(attachment.read())
encoders.encode_base64(att)

# Adicionamos o cabecalho no tipo anexo de email

att.add_header('Content-Disposition', f'attachment; filename= senha.pdf')
attachment.close()
mensage("Montando corpo do email.", "Quase lá, montando corpo do email.", 2000)
# 2- Montando o email
corpo = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body style="background-color: #eeeeee">
    <div style="text-align: center;">
         <h1>Olá, Segue o novo voucher do mes {datetime.date.today().month + 1}</h1>
    </div>
    <div>
        <h1 style="text-align: center;padding:80px;font-size:45px;">{voucher}</h1>
            <p style="text-align: center;font-family:verdana;font-size:15px">Este é o novo voucher para rede "Viajantes". Ele é válido para os próximos
                <mark>{dias} dias</mark>.</p>
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
                        <strong style="font-family:garamond; font-size:16px">Desenvolvido por: </strong><br>
                        <i><small></small></i><br>
                        <strong>Contato</strong><br>
                        <strong>Telefone: () 0 0000-0000</strong><br>
                        <strong>E-mail: </strong><a href="mailto:"></a> <br>
                        <strong>LinkedIn: </strong> <a href="">in//a>
                    </td>
                </tr>
            </table>
        </footer>
    </div>
</body>
</html>
'''

email_message = MIMEMultipart()
email_message['From'] = login
with open('D:\\scripts\\automacoes\\envio_voucher_wifi_viajantes\\dados\\emails.txt', 'r') as emails:
    email = [x.strip() for x in emails.readlines()]
    for x in email:
        email_message['Subject'] = 'Voucher Wi-fi (Favor não responder)'
        email_message.attach(MIMEText(corpo, 'html', 'utf-8'))

        # colocamos o anexo no corpo do email.
        email_message.attach(att)
        mensage("Enviando email.", f"Enviando email para {x}.", 1500)
        # 3- Enviando e fechando o servidor
        server.sendmail(email_message['From'], x, email_message.as_string())
# fechando servidor de e-mail
server.close()
