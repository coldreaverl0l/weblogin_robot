from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep 
import credenciales

# Inicializa el WebDriver (por ejemplo, Chrome)
driver = webdriver.Chrome()

# Navega a la página web y espera 15 segundos
driver.get('https://www.facebook.com/?locale=es_LA')
sleep(5)

# Encuentra el campo de entrada y elimina el atributo readonly #rut para la cuenta rut
input_field = driver.find_element(By.ID, 'email')
driver.execute_script("arguments[0].removeAttribute('readonly')", input_field)

# Envía un valor al campo de entrada
input_field.send_keys(credenciales.email)

# Encuentra el campo de contraseña y elimina el atributo readonly si es necesario #password para la cuenta rut
password_field = driver.find_element(By.NAME, 'pass')
driver.execute_script("arguments[0].removeAttribute('readonly')", password_field)

# Envía un valor al campo de contraseña
password_field.send_keys(credenciales.password2)

#5 segundos por el amor de Dios 
sleep(5)

# Encuentra y hace clic en el botón de inicio de sesión #btnLogin pa la cuenta rut
button = driver.find_element(By.NAME, 'login')
button.click();

# esperamos 10 segundos luego de ingresar el rut
sleep(20)

# Cierra el navegador
#driver.quit()

