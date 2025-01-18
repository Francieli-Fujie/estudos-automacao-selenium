import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class PesquisaPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def clicar_link_ratos(self):
        button_Ratos = self.wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@href="https://www.petz.com.br/blog/dicas/nomes-para-ratos/"])[1]')))
        button_Ratos.click()

    def rolar_pagina(self, vezes=7):
        body = self.driver.find_element(By.TAG_NAME, 'body')
        for _ in range(vezes):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)  # Aguardar 1 segundo entre as rolagens
