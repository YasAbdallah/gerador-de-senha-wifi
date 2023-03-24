from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
        self.xpaths = xpaths

    def gerarVoucher(self):
        pegarTexto = ''
        try:
            opcoes = webdriver.EdgeOptions()
            driver = webdriver.Edge(executable_path=f'{self.caminhoDriver}\\msedgedriver.exe', options=opcoes)
        except Exception as e:
            print(e)
            download = Download(self.caminhoDriver, self.caminhoDriver)
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