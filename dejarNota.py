from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from main import login






def dejar_nota(current_pag=1, user=None, psw=None, logged_in=False):
    pagina = str(current_pag)
    driver = webdriver.Firefox()
    if not logged_in:
        login(user, psw, driver)
    else:
        pass

    # Llega a los expedientes en despacho
    try:
        if "Quitar filtro dejar nota" in driver.page_source:
            pass
        else:
            driver.find_elements_by_class_name("btn-filter")[1].click()
    except NoSuchElementException as e:
        print(e)
        driver.find_elements_by_class_name("btn-filter")[1].click()

    while driver.find_element_by_xpath("//*[text()='Consulta en proceso']").is_displayed():
        sleep(0.3)

    if current_pag > 1:
        driver.find_element_by_xpath('//span[text()=' + pagina + ']').click()
    while driver.find_element_by_xpath("//*[text()='Consulta en proceso']").is_displayed():
        sleep(0.3)

    try:

        for i in range(0, 15):

            driver.execute_script("window.scrollBy(0, 120);")
            # referencia en cada loop los botones de dejar nota y los nombres de los autos, ya que la sesion
            # se vence.
            lapices = driver.find_elements_by_xpath("//a[@class='btn btn-info btn-sm']")

            try:
                while driver.find_element_by_xpath("//*[text()='Consulta en proceso']").is_displayed():
                    sleep(0.3)
            except NoSuchElementException as e:
                pass

            lapices[i].click()

            try:
                while driver.find_element_by_xpath("//*[text()='Consulta en proceso']").is_displayed():
                    sleep(0.3)
            except NoSuchElementException as e:
                pass

            driver.find_element_by_xpath('//input[@value="Dejar Nota"]').click()

            try:
                while driver.find_element_by_xpath("//*[text()='Consulta en proceso']").is_displayed():
                    sleep(0.3)
            except NoSuchElementException as e:
                pass

            if "Ya se ha dejado nota con el usuario" or "Se ha dejado nota en el expediente de forma correcta" in driver.page_source:

                sleep(2)
                autos = driver.find_elements_by_xpath("//a[@class='btn btn-info btn-sm']/preceding::td[5]")
                try:
                    import intercara
                    msj = str("Nota correcta en autos " + autos[i].text)
                    agValor = intercara.Ui_MainWindow
                    agValor.agregar_valor(msj=msj)
                except Exception as e:
                    print(e)

            else:
                print("Error dejando nota, ultima nota en " + autos[i].text + " en pagina: " + pagina)
                print("Intentando reinicio")
                driver.quit()
                if login():
                    dejar_nota(current_pag, logged_in=False)
                break  # Aca va error handling - raise exception
    except IndexError as indice:
        print(indice)
        print("Se ha llegado al final de la lista. Nota terminada")
        driver.quit()


    avanzar_pag(current_pag, driver)

def avanzar_pag(current_pag, driver):
    total_pags = len(driver.find_elements_by_xpath("//a[@class='padding-pagination margin-pagination']"))
    current_pag += 1
    pagina = str(current_pag)

    if current_pag > total_pags:
        print("Se ha llegado al final de la lista. Nota terminada")

    else:

        driver.find_element_by_xpath('//span[text()=' + pagina + ']').click()

        while driver.find_element_by_xpath("//*[text()='Consulta en proceso']").is_displayed():
            sleep(0.1)

        dejar_nota(current_pag, logged_in= True)




