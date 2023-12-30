from selenium import webdriver
from selenium.webdriver.common.by import By
import json


def loginIncorrectCredentials():
    """Celem funkcji jest sprawdzenie logowania błędnymi danymi"""

    # inicjalizacja sterownika przeglądarki
    driver = webdriver.Firefox()

    # otwarcie strony internetowej testarena.pl/zaloguj
    driver.get("http://demo.testarena.pl/zaloguj")

    # Pobranie loginu i hasła
    with open('test\\konfig.json') as config_file:
        config = json.load(config_file)

    # Pobranie loginu i hasła
    email = config['incorrectEmail'] 
    password = config['incorrectPassword']

    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID,"password").send_keys(password)

    login = driver.find_element(By.ID, "login")
    login.click()

    login_error = driver.find_element(By.XPATH,"//div[@class = 'login_form_error']")

    #Sprawdzenie poprawności logowania do strony
    if login_error.is_displayed():
        print("Logowanie nieudane - wynik testu POZYTYWNY")
    else:
        print("Logowanie udane - wynik testu NEGATYWNY")

    driver.quit()


def loginCorrectEmailIncorrectPassword():
    """Celem funkcji jest sprawdzenie logowania prawidłowym adresem email i nieprawidłowym hasłem"""

    # inicjalizacja sterownika przeglądarki
    driver = webdriver.Firefox()

    # otwarcie strony internetowej testarena.pl/zaloguj
    driver.get("http://demo.testarena.pl/zaloguj")

    # Pobranie loginu i hasła
    with open('test\\konfig.json') as config_file:
        config = json.load(config_file)

    # Pobranie loginu i hasła
    email = config['email'] 
    password = config['incorrectPassword']

    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID,"password").send_keys(password)

    login = driver.find_element(By.ID, "login")
    login.click()

    login_error = driver.find_element(By.XPATH,"//div[@class = 'login_form_error']")

    #Sprawdzenie poprawności logowania do strony
    if login_error.is_displayed():
        print("Logowanie nieudane - wynik testu POZYTYWNY")
    else:
        print("Logowanie udane - wynik testu NEGATYWNY")

    driver.quit()


def loginIncorrectEmailCorrectPassword():
    """Celem funkcji jest sprawdzenie logowania nieprawidłowym adresem email i prawidłowym hasłem"""

    # inicjalizacja sterownika przeglądarki
    driver = webdriver.Firefox()

    # otwarcie strony internetowej testarena.pl/zaloguj
    driver.get("http://demo.testarena.pl/zaloguj")

    # Pobranie loginu i hasła
    with open('test\\konfig.json') as config_file:
        config = json.load(config_file)

    # Pobranie loginu i hasła
    email = config['incorrectEmail'] 
    password = config['password']

    driver.find_element(By.ID, "email").send_keys(email)
    driver.find_element(By.ID,"password").send_keys(password)

    login = driver.find_element(By.ID, "login")
    login.click()

    login_error = driver.find_element(By.XPATH,"//div[@class = 'login_form_error']")

    #Sprawdzenie poprawności logowania do strony
    if login_error.is_displayed():
        print("Logowanie nieudane - wynik testu POZYTYWNY")
    else:
        print("Logowanie udane - wynik testu NEGATYWNY")

    driver.quit()



def loginEmptyFields():
    """Celem funkcji jest sprawdzenie logowania bez podania danych"""

    # inicjalizacja sterownika przeglądarki
    driver = webdriver.Firefox()

    # otwarcie strony internetowej testarena.pl/zaloguj
    driver.get("http://demo.testarena.pl/zaloguj")

    login = driver.find_element(By.ID, "login")
    login.click()

    login_error = driver.find_element(By.XPATH,"//div[@class = 'login_form_error']")


    #Sprawdzenie poprawności logowania do strony
    if login_error.is_displayed():
        print("Logowanie nieudane - wynik testu POZYTYWNY")
    else:
        print("Logowanie udane - wynik testu NEGATYWNY")

    driver.quit()


def loginEmptyEmail():
    """Celem funkcji jest sprawdzenie logowania bez podania adresu email"""

    # inicjalizacja sterownika przeglądarki
    driver = webdriver.Firefox()

    # otwarcie strony internetowej testarena.pl/zaloguj
    driver.get("http://demo.testarena.pl/zaloguj")

    # Pobranie loginu i hasła
    with open('test\\konfig.json') as config_file:
        config = json.load(config_file)

    # Pobranie hasła
    password = config['password']

    driver.find_element(By.ID,"password").send_keys(password)

    login = driver.find_element(By.ID, "login")
    login.click()

    login_error = driver.find_element(By.XPATH,"//div[@class = 'login_form_error']")

    #Sprawdzenie poprawności logowania do strony
    if login_error.is_displayed():
        print("Logowanie nieudane - wynik testu POZYTYWNY")
    else:
        print("Logowanie udane - wynik testu NEGATYWNY")

    driver.quit()


def loginEmptyPassword():
    """Celem funkcji jest sprawdzenie logowania bez podania hasła"""

    # inicjalizacja sterownika przeglądarki
    driver = webdriver.Firefox()

    # otwarcie strony internetowej testarena.pl/zaloguj
    driver.get("http://demo.testarena.pl/zaloguj")

    # Pobranie hasła
    with open('test\\konfig.json') as config_file:
        config = json.load(config_file)

    email = config['email']

    driver.find_element(By.ID, "email").send_keys(email)

    login = driver.find_element(By.ID, "login")
    login.click()

    login_error = driver.find_element(By.XPATH,"//div[@class = 'login_form_error']")

    #Sprawdzenie poprawności logowania do strony
    if login_error.is_displayed():
        print("Logowanie nieudane - wynik testu POZYTYWNY")
    else:
        print("Logowanie udane - wynik testu NEGATYWNY")

    driver.quit()




loginIncorrectCredentials()
loginCorrectEmailIncorrectPassword()
loginIncorrectEmailCorrectPassword()
loginEmptyFields()
loginEmptyEmail()
loginEmptyPassword()
