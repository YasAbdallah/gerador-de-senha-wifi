import pymsgbox
import wifi_qrcode_generator.generator
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from random import randint

def menssagem(titulo, texto, tempo):
    criador = " Criado Por: Yasser Ibrahim Abdallah Vaz Condoluci."
    return pymsgbox.alert(text=texto, title=titulo + criador, timeout=tempo)

def mm2p(mm):
    return mm / 0.352777

def criarPDF(senha):
    caminho = 'D:\\scripts\\automacoes\\envio_voucher_wifi_viajantes\\'
    cnv = canvas.Canvas("senha_wifi.pdf", pagesize=A4)

    cnv.rect(mm2p(1.70), mm2p(1.70), width=mm2p(206.18), height=mm2p(293.18))
    cnv.drawImage(f"{caminho}imagem_senha\\wifi_logo.png", 100, mm2p(120), width=mm2p(150), height=mm2p(230), preserveAspectRatio=True, mask="auto")
    cnv.drawImage(f"{caminho}imagem_senha\\qrcode_senha.png", mm2p(60), mm2p(53), width=mm2p(90), height=mm2p(150), preserveAspectRatio=True, mask="auto")

    pdfmetrics.registerFont(TTFont('arial', 'arial.ttf'))
    pdfmetrics.registerFont(TTFont('Franklin Gotic', 'framd.ttf'))
    pdfmetrics.registerFont(TTFont('Segoe', 'segoesc.ttf'))

    cnv.setFont('arial', 30)
    cnv.drawString(mm2p(40), mm2p(50), "Para acessar o wifi, aponte a")
    cnv.drawString(mm2p(15), mm2p(40), "câmera do seu celular para QR-Code.")
    cnv.drawString(mm2p(40), mm2p(30), f"Ou use a senha {senha}")

    cnv.setFont('Franklin Gotic', 10)
    cnv.drawString(mm2p(2), mm2p(3), "Criado por: ")
    cnv.setFont('Segoe', 10)
    cnv.drawString(mm2p(20), mm2p(3), "Yasser Ibrahim Abdallah Vaz Condoluci.")
    cnv.save()
    

def gerarqrCode(senha):
    caminho = 'D:\\scripts\\automacoes\\envio_voucher_wifi_viajantes\\'

    qr_code = wifi_qrcode_generator.generator.wifi_qrcode(
        ssid='Viajantes', hidden=False, authentication_type='WPA', password=senha
    )
    qr_code.print_ascii()
    qr_code.make_image().save(f'{caminho}imagem_senha\\qrcode_senha.png')


def gerarSenhaWifi():
    i = 0
    senha = ''
    for i in range(10):
        senha += '-' if i == 5 else ''
        senha += str(randint(0, 10))
    return senha