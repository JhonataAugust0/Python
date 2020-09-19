from selenium.webdriver import Chrome 
from time import sleep


url = 'https://curso-python-selenium.netlify.app/aula_03.html'
navegador = Chrome() # Define o navegador
navegador.get(url) # Faz o navegador iniciar numa página pré determinada
sleep(2)

tag_a = navegador.find_element_by_tag_name('a') #"Navegador, procura pra mim uma tag com o nome (a)"


for click in range(0 ,10):
    ps = navegador.find_elements_by_tag_name('p')
    tag_a.click()
    #ps.text == click
    print(f"Valor de ps: {ps[-1].text}, valor do click: {click}.\n")

    print(f"Os avalores são iguais {ps[-1].text == str(click)}") 