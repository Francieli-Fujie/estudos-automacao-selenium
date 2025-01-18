from selenium import webdriver

def criar_driver():
    driver = webdriver.Chrome()  # Ou outro driver que você esteja usando
    return driver