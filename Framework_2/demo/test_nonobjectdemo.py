from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(executable_path="C:/Users/mlively/PycharmProjects/AutomationFrameWorks/Framework_2/drivers/geckodriver.exe")

driver.implicitly_wait(5)
driver.maximize_window()

baseURL="https://letskodeit.teachable.com"
driver.get(baseURL)

loginLink = driver.find_element(By.LINK_TEXT, "Login")
loginLink.click()

emailField = driver.find_element(By.ID, "user_email")
emailField.send_keys("test@email.com")

passwordField = driver.find_element(By.ID,"user_password")
passwordField.send_keys("abcabc")

loginButton = driver.find_element(By.NAME, "commit")
loginButton.click()

userIcon = driver.find_element(By.XPATH, ".//*[@id='navbar']//span[text()='Test User']")

if userIcon is not None:
    print("Login Successful")
else:
    print("Login Failed")

userIcon.click()

logoutLink = driver.find_element(By.LINK_TEXT, "Log Out")
logoutLink.click()

driver.close()
driver.quit()
print("Test Completed")