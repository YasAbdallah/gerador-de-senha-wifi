import pymsgbox
import pdfkit

def menssagem(titulo, texto, tempo):
    criador = " Criado Por: Nome."
    return pymsgbox.alert(text=texto, title=titulo + criador, timeout=tempo)


def criarPDF(voucher):
    caminho = 'D:\\scripts\\automacoes\\envio_voucher_wifi_viajantes\\'
    with open(f'{caminho}imagem_senha\\voucher.html', 'w') as senha_wifi:
        imagem_senha = f'''
        <!DOCTYPE html>
            <html lang="pt-br">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width='device-width', initial-scale=1.0">
            </head>
            <body>
                <img style="position:absolute;width:10.00in;height:14.00in" src="{caminho}imagem_senha/ci_1.png" />
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
                <img style="position:absolute;top:8.00in;left:7.95in;width:0.90in;height:1.70in;transform:rotate(23deg);" src="{caminho}imagem_senha/ri_1.png" />
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
    try:
        config = pdfkit.configuration(wkhtmltopdf='wkhtmltopdf\\bin\\wkhtmltopdf.exe')
        pdfkit.from_file(
            f'{caminho}imagem_senha\\voucher.html',
            f'{caminho}imagem_senha\\senha_wifi.pdf',
            configuration=config,
            options={
            "enable-local-file-access": True
            }
            )
    except AttributeError as at:
        # Tive que colocar essa exception pq quando faço um .exe do script da esse erro de atributo
        # dizendo que AttributeError: 'NoneType' object has no attribute 'write'
        # mas quando roda o script sem ser no .exe executa normalmente sem erro algum.
        pass
