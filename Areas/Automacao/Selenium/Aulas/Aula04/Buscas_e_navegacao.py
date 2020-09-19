from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pprint import pprint
from urllib.parse import urlparse

class Buscas_e_navagacao:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="/run/media/jhonata/_home/Programação/Python/Selenium/chromedriver")

    def entrar_no_site(self, url):
        driver = self.driver
        driver.get(url)
        time.sleep(2) 

    def buscar_lnks_da_pagina(self):
        resultado01 = dict()
        driver = self.driver
        aside = driver.find_element_by_tag_name('aside')
        aside_ancoras = aside.find_elements_by_tag_name('a')
        for ancora in aside_ancoras:
            resultado01[ancora.text] = ancora.get_attribute('href')
        pprint(resultado01)

teste01 = Buscas_e_navagacao()
teste01.entrar_no_site('https://selenium.dunossauro.live/aula_04.html')
teste01.buscar_lnks_da_pagina()