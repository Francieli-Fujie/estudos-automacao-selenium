import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


testeDrive = webdriver.Chrome() ## Mapeia a instância. Neste caso, estamos utilizando o Chrome, que busca sempre a versão mais recente. No entanto, é possível definir outra instância, se necessário (por exemplo definir uma versao especifica do chrome)

wait = WebDriverWait(testeDrive, 10)## ele define um tempo para buscar o elemento dentro da instancia'testeDrive'

url = 'https://www.petz.com.br/blog/pets'

testeDrive.get(url) ## digita a url dentro da instancia.

testeDrive.maximize_window()
time.sleep(3)

button_Gatos = wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@href="https://www.petz.com.br/blog/pets/gatos/"])[1]')))
button_Gatos.click() ## wait.until espera ate que o elemento seja carregado em tela

campo_pesquisa = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder="Busque no blog"]')))
campo_pesquisa.send_keys('Ratos')
campo_pesquisa.send_keys(Keys.RETURN)

button_Ratos = wait.until(EC.visibility_of_element_located((By.XPATH, '(//a[@href="https://www.petz.com.br/blog/dicas/nomes-para-ratos/"])[1]')))
button_Ratos.click()

time.sleep(5)

# Rolar a página várias vezes
body = testeDrive.find_element(By.TAG_NAME, 'body')
for _ in range(7):  # Rola 5 vezes
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)  # Aguardar 1 segundo entre as rolagens


input("Pressione Enter para continuar...")