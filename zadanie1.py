from selenium import webdriver
from selenium.webdriver.common.by import By
import json


def login():
    """Celem funkcji jest zalogowanie się do strony http://demo.testarena.pl i potwierdzenie prawidłowego zalogowania"""

    # inicjalizacja sterownika przeglądarki
    driver = webdriver.Firefox()

    # otwarcie strony internetowej testarena.pl/zaloguj
    driver.get("http://demo.testarena.pl/zaloguj")

    # Pobranie loginu i hasła
    with open('test\\konfig.json') as config_file:
        config = json.load(config_file)

    email = config['email']
    password = config['password']

    #Logowanie
    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID,"password").send_keys(password)

    login = driver.find_element(By.ID, "login")
    login.click()

    logo_element = driver.find_element(By.ID,"header_logo")

    #Sprawdzenie poprawności logowania do strony
    if logo_element.is_displayed():
        print("Logowanie prawidłowe")
    else:
        print("Logowanie nieprawidłowe")
    
    driver.quit()

login()
