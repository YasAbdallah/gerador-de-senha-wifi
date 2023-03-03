from lib.funcoes import menssagem, criarPDF
from lib.navegacao import Navegar
from lib.email import Email
from time import sleep
espera = lambda t: sleep(t)

menssagem("Bem-vindo ao gerador de voucher.", "Iniciando Gerador de voucher", 3000)

site_voucher = ''
url_web_driver = ''
caminho_driver = ''

login = {'username': '', 'pwd': ''}

acoes = {
    # Verificando se existe o botão de segurança
    '//*[@id="details-button"]': '',
    '//*[@id="proceed-link"]': '',
    # Logar
    'username': login['username'],
    'password': login['pwd'],
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
driver = Navegar(site=site_voucher, urlWebDriver=url_web_driver, caminhoDriver=caminho_driver, xpaths=acoes)
voucher = driver.gerarVoucher()

# Após o voucher ser gerado, criar o PDF para anexo ao email
menssagem("Gerando PDF.", "Gerando PDF para anexo do email", 2000)

gerarPDF = criarPDF(voucher)

# Conectando ao servidor de email 
conectar = Email(email=login['email'], pwd=login['pwd'], voucher=voucher)

menssagem("Quase lá!.", "Conectanto ao servidor de email", 2000)
conn = conectar.conectarServidor()
menssagem("Tudo pronto!", "Enviando E-mail", 2000)
conectar.enviarEmail(conn)

menssagem("Pronto!!!!", "Tudo certo, aproveite o wi-fi com o voucher novo!", 2000)
