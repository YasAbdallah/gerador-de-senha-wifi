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
    criador = " Criado Por: Yasser Abdallah."
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
tempo(3)
campoLogin = driver.find_element(By.NAME, 'username')
campoSenha = driver.find_element(By.NAME, 'password')
botaoLogin = driver.find_element(By.ID, 'loginButton')
campoLogin.send_keys('usuario')
campoSenha.send_keys('senha')
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
with open("VoucherAuto\\expire_time.txt", "r") as dias:
    dias = dias.readline()

texto = ["Data de expiração.", f"O tempo de duração do voucher é de {dias} dias. Para alterar essa data clique em ok?"]
troca_data = mensage(texto[0], texto[1], 10000)
if troca_data == 'OK':
    troca = pymsgbox.prompt("Informar a data limite:", default=30)
    with open("VoucherAuto\\expire_time.txt", "w") as dias:
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
host = "smtp.office365.com"
port = 587
login = "login"
senha = "senha"

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

# 2- Montando o email
corpo = f'''

{voucher}

O Vale acima é a senha para rede "Viajantes" e é válido para os próximos {dias} dias.




Esta mensagem é automática, por favor não responda.
Em caso de dúvidas ou houver algum problema com o código enviado, falar com responsável da ‘internet’.

________________________________________________
Criado por:

Cel: (00) 0 0000-0000
E-mail: 
'''

email_message = MIMEMultipart()
email_message['From'] = login
with open('VoucherAuto\\emails.txt', 'r') as emails:
    email = [x.strip() for x in emails.readlines()]
    for x in email:
        email_message['Subject'] = 'Voucher Wi-fi (Favor não responder)'
        email_message.attach(MIMEText(corpo, 'plain'))

        # colocamos o anexo no corpo do email.
        email_message.attach(att)

        # 3- Enviando e fechando o servidor
        server.sendmail(email_message['From'], x, email_message.as_string())
# fechando servidor de e-mail
server.close()
