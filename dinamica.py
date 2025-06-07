from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time

# Inicializar navegador
driver = webdriver.Chrome()
driver.get("https://demoqa.com/dynamic-properties")

try:
    # Test de cambio de color
    color_button = driver.find_element(By.ID, "colorChange")
    color_inicial = color_button.value_of_css_property("color")
    print(f"Color inicial: {color_inicial}")
    
    # Esperar cambio de color (maximo 10 segundos)
    for i in range(10):
        time.sleep(1)
        color_actual = color_button.value_of_css_property("color")
        if color_actual != color_inicial:
            print(f"Color cambió a: {color_actual}")
            break
    
    # Test de boton que aparece despues de 5 segundos
    try:
        WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.ID, "visibleAfter")))
        boton_visible = driver.find_element(By.ID, "visibleAfter")
        print(f"Botón apareció: {boton_visible.text}")
    except:
        print("El boton no aparecio")
    
    # Test de boton que se habilita despues de 5 segundos
    try:
        WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.ID, "enableAfter")))
        boton_habilitado = driver.find_element(By.ID, "enableAfter")
        print(f"Boton habilitado: {boton_habilitado.text}")
    except:
        print("El boton no se habilito")
    
    # Buscar elementos dinamicos
    elementos = driver.find_elements(By.XPATH, "//*[contains(@id, 'dynamic')]")
    for elemento in elementos:
        print(f"Elemento encontrado: {elemento.get_attribute('id')}")
    
    # Verificar imágenes
    print("\n===VERIFICACI0N DE IMaGENES===")
    imagenes = driver.find_elements(By.TAG_NAME, "img")
    for img in imagenes:
        src = img.get_attribute("src")
        if src:
            try:
                respuesta = requests.get(src, timeout=5)
                if respuesta.status_code == 200:
                    print(f"Imagen OK: {src}")
                else:
                    print(f"Imagen falla: {src}")
            except:
                print(f"Error en imagen: {src}")
    
    # Verificar enlaces
    print("\n===VERIFICACION DE ENLACES ===")
    enlaces = driver.find_elements(By.TAG_NAME, "a")
    for enlace in enlaces:
        href = enlace.get_attribute("href")
        if href:
            try:
                respuesta = requests.get(href, timeout=5)
                if respuesta.status_code == 200:
                    print(f"Enlace OK: {href}")
                else:
                    print(f"Enlace falla: {href}")
            except:
                print(f"Error en enlace: {href}")

finally:
    driver.quit()
    print("\nPrueba completada")