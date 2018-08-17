import csv
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# with open('results_CienciaDosMateriais.csv', 'w') as f:
#     f.write("Indice")

# Open up a Firefow browser and navigate to web page
driver = webdriver.Firefox()
driver.get("https://pt.wikipedia.org/wiki/Ci%C3%AAncia_dos_materiais")

# Extracts lists of data based on xpath
index_items = driver.find_elements_by_xpath('//*[@id="toc"]')
seeAlso_items = driver.find_elements_by_xpath('//*[@id="mw-content-text"]/div/ul[3]')

# See how many items
num_index_items = len(index_items)
num_seeAlso_items = len(seeAlso_items)

# Print out all of the items on the current page
for i in range(num_index_items):
    for j in range(num_seeAlso_items):
        print(index_items[i].text + "," + seeAlso_items[j].text + "\n"

# Print result in .csv
with open('results_CienciaDosMateriais.csv', 'a') as f:
    for i in range(num_index_items):
        for j in range(num_seeAlso_items):
            f.write(index_items[i].text + "," + seeAlso_items[j].text + "\n")

# Clean up (close browser once taks is completed)
driver.close()
