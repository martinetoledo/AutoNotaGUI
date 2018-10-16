from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from time import sleep
from dejarNota import dejar_nota
from novedades import get_novedades

driver = webdriver.Firefox() # Puede cambiarse por Chrome


# Funcion que entra a la pagina de Consulta de Causas
# toma dos argumentos, CUIT y contrasena del usuario que se quiere ingresar

def login(user, psw):
    try:
        driver.get('http://scw.pjn.gov.ar/scw/home.seam')
        iniciarsesion = driver.find_element_by_partial_link_text('Iniciar sesi') # Boton de iniciar sesion
        iniciarsesion.click()
        assert "Ingresar" in driver.page_source

        # Llena formularios de usuario y contrasena y los envia

        driver.find_element_by_id("username").send_keys(user)
        driver.find_element_by_id("password").send_keys(psw)
        driver.find_element_by_id("password").send_keys(Keys.RETURN)
        sleep(2)
        return True


    except TimeoutException as e:
        print(e)
        print("No pudo conectarse al Sistema de Consulta de Causas - revise su conexion a Internet e intente nuevamente")


    except Exception as e2:
        if "CUIT/CUIL o contrase" in driver.page_source:
            print("CUIT/CUIL o contraseña incorrectos.")
            print(e2)









