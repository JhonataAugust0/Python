from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from urllib.parse import urlparse

class Historico_pagina:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="/run/media/jhonata/_home/Programação/Python/Selenium/chromedriver")

    def entrar_no_site(self, url):
        driver = self.driver
        driver.get(url)
        time.sleep(1.5) 
    
    def mostar_url(self):
        driver = self.driver 
        url_parseada = urlparse(driver.current_url)
        return url_parseada


teste01 = Historico_pagina()
teste01.entrar_no_site('https://selenium.dunossauro.live/aula_04_b.html')
teste01.mostar_url()