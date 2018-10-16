from main import driver, login
from time import sleep


def dejar_nota(current_pag = 1):

    # Llega a los expedientes en despacho
    driver.find_elements_by_class_name("btn-filter")[1].click()
    while driver.find_element_by_xpath("//*[text()='Consulta en proceso']").is_displayed():
        sleep(0.1)

    driver.find_element_by_xpath('//span[text()=' + current_pag + ']').click()

    for i in range(0,16):

        # referencia en cada loop los botones de dejar nota y los nombres de los autos, ya que la sesion
        # se vence.
        lapices = driver.find_elements_by_xpath("//i[@class='fa fa-pencil fa-lg']")
        autos = driver.find_elements_by_xpath("//i[@class='fa pencil fa-lg']/preceding::td[3]")

        while driver.find_element_by_xpath("//*[text()='Consulta en proceso']").is_displayed():
            sleep(0.1)

        lapices[i].click()

        driver.find_element_by_xpath('//input[@value="Dejar Nota"]').click()

        while driver.find_element_by_xpath("//*[text()='Consulta en proceso']").is_displayed():
            sleep(0.1)

        if "Ya se ha dejado nota con el usuario" or "Se ha dejado nota en el expediente de forma correcta" in driver.page_source:
            print("Nota correcta en autos " + autos[i].text)

        else:
            print("Error dejando nota, ultima nota en " + autos[i].text + " en pagina: " + str(current_pag))
            print("Intentando reinicio")
            driver.quit()
            if login():
                dejar_nota(current_pag)
            break # Aca va error handling - raise exception

    avanzar_pag(current_pag)

def avanzar_pag(current_pag):

    total_pags = len(driver.find_elements_by_xpath("//a[@class='padding-pagination margin-pagination']"))
    current_pag += 1

    if current_pag > total_pags:
        print("Se ha llegado al final de la lista. Nota terminada")

    else:

        driver.find_element_by_xpath('//span[text()='+current_pag+']').click()

        while driver.find_element_by_xpath("//*[text()='Consulta en proceso']").is_displayed():
            sleep(0.1)

        dejar_nota(current_pag)

