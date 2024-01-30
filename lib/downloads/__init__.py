from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
from zipfile import ZipFile
from time import sleep
import os


class Download:
    '''
    Este objeto foi criado para baixar automaticamente o webdriver mais recente do webDriver de sua preferência.
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
        self.descompactar()

    def descompactar(self):
        '''
        Feito para descompactar o arquivo .zip em uma pasta.
        :return: Retorna o arquivo descompactado.
        '''
        try:
            desc = ZipFile(os.path.join(self.caminhoDown, self.arquivo))
            desc.extractall(self.caminhoDesc)
            desc.close()
        except Exception as e:
            print(e)
        else:
            return os.remove(os.path.join(self.caminhoDesc, self.arquivo))