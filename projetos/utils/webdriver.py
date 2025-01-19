from selenium import webdriver

def criar_driver():
    driver = webdriver.Chrome()  # Ou outro driver que você esteja usando
    url = 'https://www.petz.com.br/blog/pets'
    driver.get(url)

    return driver