from urllib.request import urlretrieve
from zipfile import ZipFile
from time import sleep
import os


class Download:
    '''
    Este objeto foi criado para baixar automaticamente o webdriver mas recente do MS Edge.
    '''
    def __init__(self, url, caminhoDown, caminhoDesc):
        '''

        :param url: Url do site onde faz o download do webDriver
        :param caminhoDown: Caminho no computador onde quer fazer o download do arquivo
        :param caminhoDesc: Caminho no computador onde quer descompactar o arquivo baixado
        '''
        self.url = url
        self.caminhoDown = caminhoDown
        self.caminhoDesc = caminhoDesc
        self.arquivo = ''

    def download(self):
        '''
        Essa função recebe o objeto BeautifulSoup e analiza o site para fazer o download do edge WebDriver.
        Descrição: Faz o download do arquivo .zip, descompacta o arquivo e deleta o arquivo .zip ao final da execução.
        :return: Retorna o arquivo descompactado e pronto para uso.
        '''
        
        local_filename, headers = urlretrieve(self.caminhoDown)
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
        Feito para deletar o arquivo .zip.
        :return: Remove o arquivo .zip apenas.
        '''
        os.remove(self.arquivo[0])
