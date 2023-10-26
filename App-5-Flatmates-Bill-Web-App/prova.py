import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Set the Chromedriver and the PATH
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# Get function to the URL of interest
driver.get("https://www.alimentinutrizione.it/tabelle-nutrizionali/ricerca-per-nutriente")

# Search for the available options related to a specific food
cerca_nutriente_alimento = driver.find_element(By.CSS_SELECTOR, "option:nth-child(3)")
cerca_nutriente_alimento.click()
print(cerca_nutriente_alimento.text)

cerca_nome_alimento = driver.find_element(By.ID, "cercatabella")
print(cerca_nome_alimento.text)









#cerca_nome.send_keys("aglio")

#accedi_alle_tabelle = driver.find_element(By.CLASS_NAME, "btn btn-primary font-weight-bold")
#accedi_alle_tabelle.click()

# Print all the available options
#possibili_scelte = driver.find_element(By.ID, "cercatabella")
#print(possibili_scelte.text)

#input_nome = driver.find_element(By.CLASS_NAME, "elenment cat-list-row1")

time.sleep(30000)