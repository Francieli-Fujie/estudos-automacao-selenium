import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


testeDrive = webdriver.Chrome()

wait = WebDriverWait(testeDrive, 10)

url = 'https://www.petz.com.br/blog/pets'

testeDrive.get(url)

testeDrive.maximize_window()
time.sleep(3)

button_Gatos = wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@href="https://www.petz.com.br/blog/pets/gatos/"])[1]')))
button_Gatos.click()

campo_pesquisa = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Busque no blog"]')))
campo_pesquisa.send_keys('Ratos')
campo_pesquisa.send_keys(Keys.RETURN)

input("Pressione Enter para continuar...")