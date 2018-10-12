from main import logged_in, driver, login
from time import sleep


def dejarnota():

    # Llega a los expedientes en despacho
    driver.find_element_by_link_text()
    driver.find_elements_by_class_name("btn-filter")[1].click()
    while "Consulta en proceso" in driver.page_source:
        sleep(1)
    exptes = driver.find_elements_by_css_selector('.fa-pencil')