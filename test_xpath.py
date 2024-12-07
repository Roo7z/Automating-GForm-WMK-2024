from selenium import webdriver
from selenium.webdriver.common.by import By
import random

driver = webdriver.Firefox()


# Arahkan browser ke halaman Google Form
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfPBd9v4hphJqCFZbvY3hgTy9SZw5zXawYqTrqzcbC_Sol5xw/viewform")

# age
button_age = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span'
driver.find_element(By.XPATH, button_age).click()

# Tunggu beberapa detik agar browser dapat menampilkan halaman
input("Tekan Enter untuk menutup browser...")

# Tutup browser setelah interaksi
driver.quit()
