import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service
from lib.downloads import Download
from time import sleep


class Navegar:
    def __init__(self, site, caminhoDriver, xpaths):
        """
        :param site: Informar o site que o sistema deve fazer a navegação
        :param caminhoDrive: O caminho onde está localizado o webDriver do navegador
        :param urlWebDriver: Informar o site onde é feito o download
        :param xpath: Informar um dicionario com o xpath e do que deseja ser feito. No caso do click apenas uma string vazia ''
        """
        self.site = site
        self.caminhoDriver = caminhoDriver
        self.versaoDriver = [f for d, f, a in os.walk('C:\\Program Files (x86)\\Microsoft\\Edge\\Application')][0][0]
        self.urlWebDriver = f"https://msedgedriver.azureedge.net/{self.versaoDriver}/edgedriver_win64.zip"
        self.xpaths = xpaths

    def gerarVoucher(self):
        pegarTexto = ''
        try:
            # Procura na pasta onde está instalado o edgrDriver se o mesmo existe.
            for exe in os.scandir(self.caminhoDriver):
                if '.exe' in exe.name:
                    edgeEXE = exe.name
                    break

            print(os.path.join(self.caminhoDriver, edgeEXE))

            #Executa o navegador automatizado.
            opcoes = webdriver.EdgeOptions()
            service = Service(executable_path=os.path.join(self.caminhoDriver, edgeEXE))
            driver = webdriver.Edge(service=service, options=opcoes)
        except Exception as e:
            print(e)
            download = Download(self.urlWebDriver, self.caminhoDriver, self.caminhoDriver)
            download.download()
            self.gerarVoucher()
        else:
            driver.get(self.site)
            for xpath, texto in self.xpaths.items():
                sleep(3)
                if texto == 'getText':
                    pegarTexto = driver.find_element(By.XPATH, xpath).text
                elif texto != '':
                    driver.find_element(By.XPATH, xpath).send_keys(Keys.CONTROL + 'a')
                    driver.find_element(By.XPATH, xpath).send_keys(texto)
                else:
                    driver.find_element(By.XPATH, xpath).click()
            driver.close()
        return pegarTexto