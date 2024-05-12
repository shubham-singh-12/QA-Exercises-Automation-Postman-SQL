from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

# Initialize the WebDriver instance
driver = webdriver.Chrome()
driver.maximize_window()  # Maximize the browser window

# Navigate to the application URL
driver.get("https://ecs-qa.kloudship.com")

# Login to the application
username_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "login-email")))
username_field.send_keys("kloudship.qa.automation@mailinator.com")

password_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "login-password")))
password_field.send_keys("Password1")

login_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
login_button.click()

# Wait for the home page to load
WebDriverWait(driver, 30).until(EC.url_contains("home"))

# Navigate to the Package Types page
package_types_link = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//mat-card[8]/p[3]")))
package_types_link.click()

# Wait for the Package Types page to load
# WebDriverWait(driver, 30).until(EC.url_contains("Package Types"))

# Click the "Add Manually" button
add_manually_button = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//button[2]/span/mat-icon")))
add_manually_button.click()

# Generate a random integer less than 20 for dimensions
length = random.randint(1, 9)
width = random.randint(1, 9)
height = random.randint(1, 9)

# Enter the package details
name_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "mat-input-1")))
name_field.send_keys("Shubham_Singh")

length_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "mat-input-2")))
length_field.send_keys(length)

width_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "mat-input-3")))
width_field.send_keys(width)

height_field = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, "mat-input-4")))
height_field.send_keys(height)

# Submit the form
check_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//mat-icon[contains(.,'check')]")))
check_button.click()

# More Button
more_button_hover = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'more_vert')]")))
more_button_hover.click()

# Verify that the package is added successfully
# (You can add your verification logic here)

# Logout of the application
logout_link = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//button[contains(.,'power_settings_new Logout')]")))
logout_link.click()

# Close the WebDriver instance
driver.close()