from main import login, driver
from time import strftime

hoy = strftime("%d/%m/%Y")


def get_novedades():
    file = open("C:\\Users\Martin\Documents\test\\Novedades " + hoy +".txt", 'w+')
    driver.find_elements_by_tag_name("select")[2].click()
    driver.find_element_by_xpath('//option[@value="FECHA"]').click()
    driver.find_element_by_xpath('//a[text()="Ordenar"]').click()
    autos = driver.find_elements_by_xpath("//i[@class='fa fa-eye fa-lg']/preceding::td[3]")
    fechas = driver.find_elements_by_xpath("//i[@class='fa fa-eye fa-lg']/preceding::td[1]")
    for i in range(0,15):
        if hoy in fechas[i].text:
            expte = autos[i].text
            file.write(expte + "\n")
        else:
            break

# TODO: Me falta poner el avanzar pag. y arreglar problemas con el IO