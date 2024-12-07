from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Inisialisasi WebDriver untuk membuka browser Firefox
driver = webdriver.Firefox()


# Arahkan browser ke halaman Google Form
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSfPBd9v4hphJqCFZbvY3hgTy9SZw5zXawYqTrqzcbC_Sol5xw/viewform")

# Tunggu beberapa detik agar halaman memuat
time.sleep(2)

"""
# Fungsi untuk scroll dan klik elemen
def scroll_and_click(xpath):
    # Tunggu elemen bisa di klik
    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    
    # Scroll elemen ke dalam tampilan
    driver.execute_script("arguments[0].scrollIntoView(true);", element)
    
    # Tunggu sebentar agar scroll selesai
    time.sleep(1)
    
    # Klik elemen
    element.click()
    Klik dropdown untuk membuka pilihan
"""


dropdown_xpath = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[1]"  # Ganti dengan XPath dropdown yang sesuai
dropdown = driver.find_element(By.XPATH, dropdown_xpath)
dropdown.click()



# Tunggu agar dropdown terbuka
time.sleep(2)

# Pilih opsi "Red Force" dalam dropdown berdasarkan data-value atau teks
option_xpath = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[36]/span"  # Pilihan untuk 'Red Force'
option = driver.find_element(By.XPATH, option_xpath)
option.click()


time.sleep(2)

# age
button_age = [
    "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div",
    "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span"
]
driver.find_element(By.XPATH, random.choice(button_age)).click()



# Gender
button_gender = [
    "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div", 
    "/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div"
]
driver.find_element(By.XPATH, random.choice(button_gender)).click()



# income
button_income = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[1]/div/div[3]/div"
click_button_income = driver.find_element(By.XPATH, button_income)
click_button_income.click()


# priorities
button_priorities = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div"
click_button_priorities = driver.find_element(By.XPATH, button_priorities)
click_button_priorities.click()


# find 
button_find = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[1]/div/div[3]/div"
click_button_find = driver.find_element(By.XPATH, button_find)
click_button_find.click()


# price
button_price = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[5]/label/div/div[1]/div/div[3]/div"
click_button_price = driver.find_element(By.XPATH, button_price)
click_button_price.click()


# Important
button_important = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div"
click_button_important = driver.find_element(By.XPATH, button_important)
click_button_important.click()



# interested
button_interested = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div"
click_button_interested = driver.find_element(By.XPATH, button_interested)
click_button_interested.click()


# often 
button_often = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div"
click_button_often = driver.find_element(By.XPATH, button_often)
click_button_often.click()


# opinion
button_opinion = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div"
driver.find_element(By.XPATH, button_opinion).click()


# recommend
button_recommend = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div"
driver.find_element(By.XPATH, button_recommend).click()



# innovation 
button_innovation = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div"
driver.find_element(By.XPATH, button_innovation).click()



# packaging 
button_packaging = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div"
driver.find_element(By.XPATH, button_packaging).click()


# payment
button_payment = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div"
driver.find_element(By.XPATH, button_payment).click()


# send
button_send = "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span"
driver.find_element(By.XPATH, button_send).click()


time.sleep(5)

# ------------------ page fill another response --------------------------------
link = "/html/body/div[1]/div[2]/div[1]/div/div[4]/a"
driver.find_element(By.XPATH, link).click()


# Tunggu beberapa detik agar browser dapat menampilkan halaman
input("Tekan Enter untuk menutup browser...")

# Tutup browser setelah interaksi
driver.quit()
