from lib.funcoes import menssagem, criarPDF
from lib.navegacao import Navegar
from lib.email import Email
from time import sleep

menssagem("Bem-vindo ao gerador de voucher.", "Iniciando Gerador de voucher", 3000)

siteVoucher = 'https://localhost:8443/manage/hotspot'
caminhoDriver = 'D:\\scripts\\webDriver'

loginUbiquiti = {'username': '', 'pwd': ''}
loginEmail = {'username': '', 'pwd':''}

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
}

# Primeiro faz a automação de navegação e criação de um novo Voucher
driver = Navegar(site=siteVoucher, caminhoDriver=caminhoDriver, xpaths=acoes)
voucher = driver.gerarVoucher()

# Após o voucher ser gerado, criar o PDF para anexo ao email
menssagem("Gerando PDF.", "Gerando PDF para anexo do email", 2000)

gerarPDF = criarPDF(voucher)

# Conectando ao servidor de email 
conectar = Email(email=loginEmail['username'], pwd=loginEmail['pwd'], voucher=voucher)

menssagem("Quase lá!.", "Conectanto ao servidor de email", 2000)
conn = conectar.conectarServidor()
menssagem("Tudo pronto!", "Enviando E-mail", 2000)
conectar.enviarEmail(conn)

menssagem("Pronto!!!!", "Tudo certo, aproveite o wi-fi com o voucher novo!", 2000)
