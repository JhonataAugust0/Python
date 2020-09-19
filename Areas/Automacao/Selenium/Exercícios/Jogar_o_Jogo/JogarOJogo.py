from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time  

class JogarOJogo:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="/run/media/jhonata/_home/Programação/Python/Selenium/chromedriver") 


    def entrarNaPagina(self):
        driver = self.driver
        driver.get('https://curso-python-selenium.netlify.app/exercicio_02.html#')
        time.sleep(2)


    def clicar(self):
        driver = self.driver
        tag_a = driver.find_element_by_tag_name('a')
        # print(f'tag a = {type(tag_a)}')
        tag_a.click()
        

    def coletarNumero(self):
        driver = self.driver
        for i in range(0, 3):
            ps = driver.find_elements_by_tag_name('p1')
        print(ps)
        




teste01 = JogarOJogo()
teste01.entrarNaPagina()
teste01.coletarNumero()
teste01.clicar()