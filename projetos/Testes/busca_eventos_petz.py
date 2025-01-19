# Adiciona o diretório "projetos" ao caminho do Python
import time
from selenium.webdriver.support.ui import WebDriverWait
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.webdriver import criar_driver
from pages.pagepetz import BlogPage
from pages.page_pesquisa import PesquisaPage

# Inicializa o driver e o WebDriverWait
driver = criar_driver()
wait = WebDriverWait(driver, 10)
blog_page = BlogPage(driver, wait)
pesquisa_page = PesquisaPage(driver, wait)

blog_page.acessar_blog() #abre o site
time.sleep(5)

pesquisa_page.clicar_evento()

pesquisa_page.selecionar_comarca()

input()

