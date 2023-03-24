from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
from urllib.error import HTTPError, URLError
from zipfile import ZipFile
from time import sleep
import os


class Download:
    '''
    Este objeto foi criado para baixar automaticamente o webdriver mais recente do webDriver de sua preferência.
    '''
    def __init__(self, caminhoDown, caminhoDesc):
        '''

        :param url: Url do site onde faz o download do webDriver
        :param caminhoDown: Caminho no computador onde quer fazer o download do arquivo
        :param caminhoDesc: Caminho no computador onde quer descompactar o arquivo baixado
        '''
        self.url = 'https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/'
        self.caminhoDown = caminhoDown
        self.caminhoDesc = caminhoDesc
        self.arquivo = ''

    def pegaPagina(self):
        '''

        :return: Retorna um objeto BeautifulSoup para tratamento dos dados no futuro
        '''
        try:
            html = urlopen(self.url)
        except HTTPError as e:
            print(e)
        except URLError as e:
            print(e)
        else:
            return BeautifulSoup(html.read(), 'html.parser')

    def download(self):
        '''
        Essa função recebe o objeto BeautifulSoup e analiza o site para fazer o download do edge WebDriver.
        Descrição: Faz o download do arquivo .zip, descompacta o arquivo e deleta o arquivo .zip ao final da execução.
        :return: Retorna o arquivo descompactado e pronto para uso.
        '''
        bs = self.pegaPagina()
        for child in bs.find('p', {'class': 'driver-download__meta'}).children:
            if 'x64' in child:
                x64 = child.attrs['href']
                self.arquivo = str(x64).split('/')[-1]
                local_filename, headers = urlretrieve(x64, filename=f'{self.caminhoDown}{self.arquivo}')
                down = open(local_filename)
                down.close()
                self.descompacta()

    def descompacta(self):
        '''
        Feito para descompactar o arquivo .zip em uma pasta.
        :return: Retorna o arquivo descompactado.
        '''
        self.arquivo = [os.path.join(d, a[0]) for d, f, a in os.walk(self.caminhoDesc)]
        desc = ZipFile(self.arquivo[0])
        desc.extractall(self.caminhoDesc)
        desc.close()
        sleep(3)
        self.deletaZip()

    def deletaZip(self):
        '''
        Deleta o arquivo .zip.
        :return: Remove o arquivo .zip apenas.
        '''
        return os.remove(self.arquivo[0])
