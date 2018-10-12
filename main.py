from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep

driver = webdriver.Firefox() # Puede cambiarse por Chrome
# Headless en produccion

# Funcion que entra a la pagina de Consulta de Causas
# toma dos argumentos, CUIT y contrasena del usuario que se quiere ingresar
def login(user, psw):

    driver.get('http://scw.pjn.gov.ar/scw/home.seam')
    iniciarsesion = driver.find_element_by_partial_link_text('Iniciar sesi') # Boton de iniciar sesion
    iniciarsesion.click()
    assert "Ingresar" in driver.page_source

    # Llena formularios de usuario y contrasena y los envia

    driver.find_element_by_id("username").send_keys(user)
    driver.find_element_by_id("password").send_keys(psw)
    driver.find_element_by_id("password").send_keys(Keys.RETURN)
    sleep(2)
    return "Ingreso exitoso"


def dejarnota():

    # Llega a los expedientes en despacho
    driver.find_element_by_link_text()
    driver.find_elements_by_class_name("btn-filter")[1].click()
    while "Consulta en proceso" in driver.page_source:
        sleep(1)
    exptes = driver.find_elements_by_css_selector('.fa-pencil')





