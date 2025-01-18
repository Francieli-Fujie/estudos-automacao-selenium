from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class BlogPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.url = 'https://www.petz.com.br/blog/pets'

    def acessar_blog(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def clicar_link_gatos(self):
        button_Gatos = self.wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@href="https://www.petz.com.br/blog/pets/gatos/"])[1]')))
        button_Gatos.click()

    def buscar_no_blog(self, termo):
        campo_pesquisa = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Busque no blog"]')))
        campo_pesquisa.send_keys(termo)
        campo_pesquisa.send_keys(Keys.RETURN)
