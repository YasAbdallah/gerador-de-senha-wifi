import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep

import pdfkit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

edge_options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=edge_options)
tempo = lambda t: sleep(t)
driver.get('https://localhost:8443/manage/hotspot/')
tempo(1)
# Verificando se existe o botão de aviso de segurança
if driver.find_element(By.XPATH, '//*[@id="details-button"]'):
    driver.find_element(By.XPATH, '//*[@id="details-button"]').click()
    driver.find_element(By.XPATH, '//*[@id="proceed-link"]').click()

# Efetuando login
tempo(1)
campoLogin = driver.find_element(By.NAME, 'username')
campoSenha = driver.find_element(By.NAME, 'password')
botaoLogin = driver.find_element(By.ID, 'loginButton')
campoLogin.send_keys('alfmno')
campoSenha.send_keys('Alf@30163016')
botaoLogin.click()

# Clicando no botão do voucher
tempo(5)
botaoVouchar = driver.find_element(By.XPATH, '/html/body/div/ui-view/ui-view/div/div/div/div/div/div/div/div[4]')
botaoVouchar.click()
tempo(1)
# Clicando no botão de criar novo vouver
botaoCriaVouchar = driver.find_element(By.XPATH, '/html/body/div/ui-view/ui-view/div/div/div/ui-view/div/div[1]/div/div[1]/div/button')
botaoCriaVouchar.click()
tempo(1)
# Escolhendo Quatidade de chaver voucher que deseja criar
campoQntVoucher = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[3]/div/div/div/div/form/div[2]/div/div/div[1]/div/div/input')
campoQntVoucher.send_keys(Keys.CONTROL + 'a')
campoQntVoucher.send_keys('1')
tempo(1)

# Selecionando quantos usuarios usarão o mesmo voucher
campoSelectMultUser = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[3]/div/div/div/div/form/div[2]/div/div/div[2]/div/div[1]/select')
campoSelectMultUser.click()
tempo(1)
campoOptionMultUser = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[3]/div/div/div/div/form/div[2]/div/div/div[2]/div/div[1]/select/option[4]')
campoOptionMultUser.click()
tempo(1)

# Selecionando quanto tempo durará o voucher
campoSelectTempoVoucher = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[3]/div/div/div/div/form/div[2]/div/div/div[3]/div/div[1]/select')
campoSelectTempoVoucher.click()
tempo(1)
campoOptionTempoVoucher = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[3]/div/div/div/div/form/div[2]/div/div/div[3]/div/div[1]/select/option[7]')
campoOptionTempoVoucher.click()
tempo(1)
inputDias = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[3]/div/div/div/div/form/div[2]/div/div/div[3]/div/div[1]/input')
inputDias.send_keys(Keys.CONTROL + 'a')
inputDias.send_keys('31')
tempo(1)

# Definindo limite de conexão de download e upload do wifi
botaoLimiteDownload = driver.find_element(By.XPATH, '//*[@id="limitDownload"]')
botaoLimiteDownload.click()
tempo(1)
campoLimiteDownload = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[3]/div/div/div/div/form/div[2]/div/div/div[4]/div/div[1]/input[2]')
campoLimiteDownload.send_keys('5632')
tempo(1)
botaoLimiteUpload = driver.find_element(By.XPATH, '//*[@id="limitUpload"]')
botaoLimiteUpload.click()
tempo(1)
campoLimiteUpload = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[3]/div/div/div/div/form/div[2]/div/div/div[5]/div/div[1]/input[2]')
campoLimiteUpload.send_keys('5632')
tempo(1)

# salvando voucher novo.
botaoSalvaVoucher = driver.find_element(By.XPATH, '/html/body/div/div[4]/div[3]/div/div/div/div/form/div[3]/div/div/div/button[2]')
botaoSalvaVoucher.click()
tempo(1)
voucher = driver.find_element(By.XPATH, '//*[@id="vouchersTable"]/tbody/tr[1]/td[2]').text

# fechandose navegador automatizado.
driver.quit()

with open('imagem_senha\\voucher.html', 'w') as senha_wifi:
    imagem_senha = f'''
    <html>
    <head>
    <link rel="stylesheet" type="text/css" href="style.css"/>
    </head>
    <body>.
    <img style="position:absolute;width:8.00in;height:13.00in" src="ci_1.png" />
    <div style="position:absolute;top:6.00in;left:1.74in;width:3.00in;line-height:3.00in;">
        <span style="font-style:normal;font-weight:normal;font-size:150pt;font-family:Alice;color:#000000">WIFI</span>
        <span style="font-style:normal;font-weight:normal;font-size:150pt;font-family:Alice;color:#000000"> </span>
        <br/>
    </div>
    <img style="position:absolute;top:6.00in;left:6.60in;width:1.00in;height:2.00in" src="ri_1.png" />
    <div style="position:absolute;top:4.83in;left:1.00in;width:8.49in;line-height:2.34in;">
        <span style="font-style:normal;font-weight:normal;font-size:100pt;font-family:Alice;color:#000000">Senha do</span>
        <span style="font-style:normal;font-weight:normal;font-size:100pt;font-family:Alice;color:#000000"> </span>
        <br/>
    </div>
    <div style="position:absolute;top:8.60in;left:2.00in;width:6.95in;line-height:1.60in;">
        <span style="font-style:normal;font-weight:normal;font-size:60pt;font-family:Alice;color:#000000">{voucher}</span>
        <span style="font-style:normal;font-weight:normal;font-size:89pt;font-family:Alice;color:#000000"> </span>
        <br/>
    </div>
    </body>
    </html>
    '''
    senha_wifi.write(imagem_senha)
tempo(1)

try:
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
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
tempo(1)
# Iniciando servidor para envio de email automatico
# Iniciando o servidor smtp
host = 'smtp.gmail.com'
port = '587'
login = 'voucherwifi.naoresponder@gmail.com'
senha = 'irf@$3004'

server = smtplib.SMTP(host=host, port=port)
server.set_debuglevel(1)
server.ehlo()
server.starttls()
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

O Vale acima é a senha para rede "Viajantes" e é valido para os próximos 30 dias.




Esta mensagem é automática, por favor não responda.
Em caso de dúvidas ou houver algum problema com o código enviado, falar com responsável da ‘internet’.

________________________________________________
Criado por: Yasser Ibrahim Abdallah Vaz Condoluci.
Desenvolvedor de aplicações e automações
Cel: (67) 99167-8140
E-mail: yassercondoluci@hotmail.com
'''

email_message = MIMEMultipart()
email_message['From'] = login
with open('C:\\Users\\Asus SATEC\\Desktop\\VoucherAuto\\emails.txt', 'r') as emails:
    email = [x.strip() for x in emails.readlines()]
    for x in email:
        email_message['Subject'] = 'Voucher Wi-fi (Favor não responder)'
        email_message.attach(MIMEText(corpo, 'plain'))

        # colocamos o anexo no corpo do email.
        email_message.attach(att)

        # 3- Enviando e fechando o servidor
        server.sendmail(email_message['From'], x, email_message.as_string())
# fechando servidor de e-mail
server.quit()
