from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time

"""Zadanie 1 - Zalogować się do wersji demo"""

def login():
    """Celem funkcji jest zalogowanie się do strony http://demo.testarena.pl i potwierdzenie prawidłowego zalogowania"""

    # inicjalizacja sterownika przeglądarki
    driver = webdriver.Firefox()

    # otwarcie strony internetowej testarena.pl/zaloguj
    driver.get("http://demo.testarena.pl/zaloguj")

    # Pobranie loginu i hasła
    with open('konfig.json') as config_file:
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

"""Zadanie 2 - Do dowolnego projektu dodać nowe zadanie i potwierdzić, że zostało dodane"""
def addTask():
    """Celem funkcji jest zalogowanie się do strony http://demo.testarena.pl oraz dodanie zadania do projektu 'Testy bazy danych' i potwierdzenie dodania zadania"""

    # inicjalizacja sterownika przeglądarki
    driver = webdriver.Firefox()

    # otwarcie strony internetowej testarena.pl/zaloguj
    driver.get("http://demo.testarena.pl/zaloguj")

    # Pobranie loginu i hasła
    with open('konfig.json') as config_file:
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

    #wybór projektu
    driver.find_element(By.XPATH,"//a[@class='chosen-single']").click()
    driver.find_element(By.XPATH, "//a[@class = 'chosen-single']").send_keys("Testy bazy danych")
    driver.find_element(By.XPATH, "//ul[@class = 'chosen-results']").click()

    #przejście do zakładki "Zadania"
    tasks = driver.find_element(By.XPATH,"//a[@href='http://demo.testarena.pl/testyb/tasks']")
    tasks.click()

    #Kliknięcie w "Dodaj zadanie"
    add_task = driver.find_element(By.XPATH, "//a[@href='http://demo.testarena.pl/testyb/task_add']")
    add_task.click()

    #Elementy zadania
    title = "Błąd w formularzu rejestracji - brak walidacji pola e-mail"
    driver.find_element(By.ID, "title").send_keys(title)
    
    desc = "Środowisko: TME\nPrzeglądarka: Google Chrome w wersji 95.0.4638.69\nSystem operacyjny: Windows 10\nWitryna: www.example.com\nData: 27-12-2023\n\nScenariusz reprodukcji:\n1.Przejdź do strony rejestracji na witrynie.\n2.Wpisz w polu e-mail adres 'testowyemail'.\n3.Kliknij przycisk 'Zarejestruj'.\n\nAktualny rezultat: Nie pojawia się komunikat błędu, formularz jest akceptowany i użytkownik jest zarejestrowany z nieprawidłowym adresem e-mail.\n\nWymagany rezultat: Powinien pojawić się komunikat o nieprawidłowym formacie e-maila."
    driver.find_element(By.ID, "description").send_keys(desc)

    release = "R24.1"
    driver.find_element(By.ID, "releaseName").send_keys(release)

    env = driver.find_element(By.ID, "token-input-environments")
    env.send_keys("TME")
    time.sleep(3)
    env.send_keys(Keys.ENTER)

    version = driver.find_element(By.ID,"token-input-versions")
    version.send_keys("test")
    time.sleep(3)
    version.send_keys(Keys.ENTER)

    calendar = driver.find_element(By.ID, "dueDate")
    calendar.click()

    now = driver.find_element(By.XPATH,"//button[contains(@class,'ui-datepicker-current ')]" )
    now.click()

    ready = driver.find_element(By.XPATH, "//button[contains(@class,'ui-datepicker-close')]")
    ready.click()

    sign = driver.find_element(By.ID,"j_assignToMe")
    sign.click()

    #Zapisanie zadania
    save = driver.find_element(By.ID,"save")
    save.click()
    
    #Sprawdzenie poprawności dodania zadania
    element = driver.find_element(By.XPATH,"//div[@class = 'icon_info']")
    if element.is_displayed():
        print("Zadanie zostało dodane.")
    else:
        print("Zadanie nie zostalo dodane.")

    driver.quit()
    

addTask()

"""Zadanie 3 - Przeprowadzić test logowania przy użyciu błednych danych"""
def loginIncorrectCredentials():
    """Celem funkcji jest sprawdzenie logowania błędnymi danymi"""

    # inicjalizacja sterownika przeglądarki
    driver = webdriver.Firefox()

    # otwarcie strony internetowej testarena.pl/zaloguj
    driver.get("http://demo.testarena.pl/zaloguj")

    # Pobranie loginu i hasła
    with open('konfig.json') as config_file:
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
    with open('konfig.json') as config_file:
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
    with open('konfig.json') as config_file:
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
    with open('konfig.json') as config_file:
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
    with open('konfig.json') as config_file:
        config = json.load(config_file)

    email = config['password']

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
