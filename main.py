import lib.funcoes as fc
from lib.navegacao import Navegar
from lib.email import Email
import os

fc.menssagem("Bem-vindo ao gerador de voucher.", "Iniciando Gerador de voucher", 3000)

siteVoucher = 'https://localhost:8443/manage/account/'
caminhoDriver = 'C:\\scripts\\webDriver'
if not os.path.exists(caminhoDriver):
    os.makedirs(caminhoDriver)

loginUbiquiti = {'username': 'Opaaa', 'pwd': 'SemSenhaPorAqui'}
loginEmail = {'username': 'issoNaoEUmEmail@valido.com', 'pwd':'semSenhaPorAquiTambem'}

senhaWifi = fc.gerarSenhaWifi()

# Xpath para geração de SENHA!!!!
acoes = {
    # Verificando se existe o botão de segurança
    '//*[@id="details-button"]': '',
    '//*[@id="proceed-link"]': '',
    # Logar
    '//input[@name="username"]': loginUbiquiti['username'],
    '//input[@name="password"]': loginUbiquiti['pwd'],
    '//button[@id="loginButton"]': '',
    # Botão configurações
    '//div[@alt="Settings"]': '',
    # Botão Wireless Network
    '//unifi-settings-side-nav//unifi-settings-nav//span[text()="Wireless Networks"]' if '//unifi-settings-side-nav//unifi-settings-nav//span[text()="Wireless Networks"]' else '//unifi-settings-nav//span[text()="Wireless Networks"]': '',
    # Select wlan group
    '//select//option[text()="satec"]': '',
    # Botão edit rede viajantes -> '//tr[2]//td[@class="wlanActions appTableCell--actions"]//button[1]'
    '//tr[1]//td[@class="wlanActions appTableCell--actions"]//button[1]': '',
    # Campo senha rede viajantes
    '//div[@class="appRow"]//input[@type="password"]': senhaWifi,
    # Botão salvar configurações
    '//button//div[text()="Save"]': '',
}

"""
Xpath para geração de VOUCHER!!!!!
acoes = {
    # Verificando se existe o botão de segurança
    '//*[@id="details-button"]': '',
    '//*[@id="proceed-link"]': '',
    # Logar
    '//input[@name="username"]': loginUbiquiti['username'],
    '//input[@name="password"]': loginUbiquiti['pwd'],
    '//button[@id="loginButton"]': '',
    # Botão Voucher
    '//div[@class="ubntIcon ubntIcon--navigation icon ubnt-icon--news"]': '',
    # Criando um novo voucher
    '//button[@title="Create vouchers"]': '',
    # Quantidade de vouchers que deseja criar
    '//input[@title="number of vouchers"]': '1',
    # Selecior Quantos usuário usaram o mesmo voucher
    '//select//option[@label="Multi use (unlimited)"]': '',
    # Selecior quanto tempo durará o voucher
    '//select//option[@label="User-defined"]': '',
    '//input[@name="expire_number"]': "30",
    # Definindo limite de conexão de download e upload do wifi
    '//input[@id="limitDownload"]': '',
    '//input[@type="number" and @name="down"]': '5632',
    '//input[@id="limitUpload"]': '',
    '//input[@type="number" and @name="up"]': '5632',
    # salvando voucher novo.
    '//div[@class="busyToggle__body ng-scope" and text()="Save"]': '',
    # Pegando o novo Voucher criado para gerar o PDF e o Email.
    '//table[@id="vouchersTable"]/tbody/tr[1]/td[2]': 'getText'
}"""

# Primeiro faz a automação de navegação e criação de um novo Voucher
driver = Navegar(site=siteVoucher, caminhoDriver=caminhoDriver, xpaths=acoes)
voucher = driver.gerarVoucher()

# Após o voucher ser gerado, criar o PDF para anexo ao email
fc.menssagem("Gerando PDF.", "Gerando PDF para anexo do email", 2000)

gerarPDF = fc.criarPDF(senhaWifi)

# Conectando ao servidor de email 
conectar = Email(email=loginEmail['username'], pwd=loginEmail['pwd'], voucher=senhaWifi)

fc.menssagem("Quase lá!.", "Conectanto ao servidor de email", 2000)
conn = conectar.conectarServidor()
fc.menssagem("Tudo pronto!", "Enviando E-mail", 2000)
conectar.enviarEmail(conn)

fc.menssagem("Pronto!!!!", "Tudo certo, aproveite o wi-fi com o voucher novo!", 2000)
