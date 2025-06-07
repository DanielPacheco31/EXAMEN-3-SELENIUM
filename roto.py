from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

driver = webdriver.Chrome()
driver.get("https://demoqa.com/broken")

def verificar_url(url, tipo):
    try:
        respuesta = requests.get(url, timeout=5)
        estado = "OK" if respuesta.status_code < 400 else "ERROR"
        print(f"{estado}: {tipo} - {url}")
    except:
        print(f"ERROR: {tipo} - {url}")

# Verificar imAgenes
print("IMAGENES")
print("--------")
for img in driver.find_elements(By.TAG_NAME, "img"):
    src = img.get_attribute("src")
    if src:
        verificar_url(src, "Imagen")

# Verificar enlaces
print("\nENLACES")
print("-------")
for link in driver.find_elements(By.TAG_NAME, "a"):
    href = link.get_attribute("href")
    if href:
        verificar_url(href, "Enlace")

driver.quit()