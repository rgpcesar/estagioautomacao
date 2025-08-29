from selenium import webdriver

def test_verify_page_title():
    """
    Este teste abre o site demoqa.com e verifica o título da página.
    """
    # Inicializa o driver do Chrome
    driver = webdriver.Chrome()

    # Abre a URL
    driver.get("https://demoqa.com")

    # Pega o título da página
    page_title = driver.title

    # Verifica se o título é o esperado
    assert page_title == "DEMOQA!"

    # Fecha o navegador
    driver.quit()
