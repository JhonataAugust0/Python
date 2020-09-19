from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Busca_aninhada_tag_text:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="/run/media/jhonata/_home/Programação/Python/Selenium/chromedriver")
       

    def entrar(self, url):
        driver = self.driver
        driver.get(url)
        time.sleep(2)


    def buscarElementosPorText(self, tag, text):
        driver = self.driver
        elementos = driver.find_elements_by_tag_name(tag)
        for elemento in elementos:
            if elemento.text == text:
                print(elemento.text)


    def buscarElemenosPorLink(self, link):
        driver = self.driver
        elementos = driver.find_elements_by_tag_name('a')
        
        for elemento in elementos:
            if link in elemento.get_attribute('href'): 
                return print(elemento.text, elemento.get_attribute('href'))


    
            




teste01 = Busca_aninhada_tag_text()
teste01.entrar('https://selenium.dunossauro.live/aula_04_a.html')
#teste01.buscarElementosPorText('li', 'DuckDuckGo')  
teste01.buscarElemenosPorLink('ddg')