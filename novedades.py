from main import logged_in, login, driver
from selenium.webdriver.support.ui import WebDriverWait
from time import strftime
from re import search, IGNORECASE

hoy = strftime("%d/%m/%Y")


def get_novedades():
    file = open("Novedades " + hoy +".txt", 'w+')
    driver.find_elements_by_tag_name("select")[2].click()
    driver.find_element_by_xpath('//option[@value="FECHA"]').click()
    driver.find_element_by_xpath('//a[text()="Ordenar"]').click()
    for i in range(7,22):
        autos = driver.find_elements_by_xpath("//i[@class='fa eye fa-lg']/preceding::td[3]")
        if hoy in driver.find_elements_by_tag_name('tr')[i].text:
            expte = autos[i].text
            print (expte)
            file.write(expte + "\n")
        else:
            break



