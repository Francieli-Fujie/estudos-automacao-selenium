import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys




class PesquisaPage:
    

    def __init__(self, driver, wait):

        self.driver = driver
        self.wait = wait

    def clicar_link_ratos(self):
        button_Ratos = self.wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@href="href="https://www.petz.com.br/blog/eventos-petz/""])[1]')))
        button_Ratos.click()

    def rolar_pagina(self, vezes=7):
        body = self.driver.find_element(By.TAG_NAME, 'body')
        for _ in range(vezes):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)  # Aguardar 1 segundo entre as rolagens

    def clicar_evento(self):
        button_Eventos = self.wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@href="https://www.petz.com.br/blog/eventos-petz/"])[1]')))
        button_Eventos.click()

    def selecionar_comarca(self):
        select_Comarca = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//select[@id="estado"]')))
        select_Comarca.click()
        estado_option = 'Minas Gerais'
        select_Estado = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, f'//*[contains(text(), "{estado_option}")]')))
        select_Estado[0].click()
