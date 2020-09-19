from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Busca_aninhada:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="/run/media/jhonata/_home/Programação/Python/Selenium/chromedriver")
       

    def entrar(self, url):
        driver = self.driver
        driver.get(url)
        time.sleep(2)


    def buscarElementos(self, elemento01, elemento02):
        driver = self.driver
        lista_n_ordenada = driver.find_element_by_tag_name(elemento01)
        #print(f'\n {lista_n_ordenada}')
        lis = lista_n_ordenada.find_elements_by_tag_name(elemento02)      
        print(lis[0].find_element_by_tag_name('a').text)
        




teste01 = Busca_aninhada()
teste01.entrar('https://selenium.dunossauro.live/aula_04_a.html')
teste01.buscarElementos('ul', 'li')