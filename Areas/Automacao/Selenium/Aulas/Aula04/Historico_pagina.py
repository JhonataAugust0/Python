from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Historico_pagina:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="/run/media/jhonata/_home/Programação/Python/Selenium/chromedriver")

    def entrar_no_site(self, url):
        driver = self.driver
        driver.get(url)
        time.sleep(1.5)

    def procurar_caixa(self, tag):
        driver = self.driver
        elementos = driver.find_elements_by_tag_name(tag)
        for elemento in elementos:
            print(f"{elemento}")
            time.sleep(0.4)
            elemento.click()
        for elemento in elementos:
            time.sleep(0.4)
            driver.back()
        for elemento in elementos:
            time.sleep(0.4)
            driver.forward()



teste01 = Historico_pagina()
teste01.entrar_no_site('https://selenium.dunossauro.live/aula_04_b.html')

teste01.procurar_caixa('div')

