from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time  


class PegarConteudoDaPagina:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="/home/jhonata/Downloads/chromedriver") 


    def entrarNaPagina(self):
        driver = self.driver
        driver.get('https://curso-python-selenium.netlify.app/exercicio_01.html')
        time.sleep(2)
        #driver.quit()


    def procurar_elementos(self):
        driver = self.driver
        ps = list()
        for i in range (0, 3):
            ps.append(driver.find_elements_by_tag_name('p'))
            print(f'{ps}')
            

            
        

    


testeclss = PegarConteudoDaPagina()
testeclss.entrarNaPagina()
testeclss.procurar_elementos()