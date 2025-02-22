import time
from selenium.webdriver.support.ui import WebDriverWait
import sys
import os
# Adiciona o diretório "projetos" ao caminho do Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.webdriver import criar_driver
from pages.pagepetz import BlogPage
from pages.page_pesquisa import PesquisaPage

# Inicializa o driver e o WebDriverWait
driver = criar_driver()
wait = WebDriverWait(driver, 10)

# Inicializa as páginas
blog_page = BlogPage(driver, wait)
pesquisa_page = PesquisaPage(driver, wait)

# Início do teste
blog_page.acessar_blog() 
time.sleep(3)

blog_page.clicar_link_gatos()
blog_page.buscar_no_blog("Ratos")

pesquisa_page.clicar_link_ratos()
pesquisa_page.rolar_pagina(vezes=7)

input("Pressione Enter para continuar...")

# Finaliza o driver após o teste
driver.quit()
