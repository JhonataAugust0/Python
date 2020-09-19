from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Historico_da_pagina():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="/run/media/jhonata/_home/Programação/Python/Selenium/chromedriver")


    def entrar (self, url):
        driver = self.driver
        driver.get(url)
        time.sleep(2)









teste01 = Historico_da_pagina()
teste01.entrar('https://selenium.dunossauro.live/aula_04_b.html')