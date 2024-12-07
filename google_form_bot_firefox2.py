from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Inisialisasi WebDriver untuk membuka browser Firefox
driver = webdriver.Firefox()

# URL Google Form
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSfPBd9v4hphJqCFZbvY3hgTy9SZw5zXawYqTrqzcbC_Sol5xw/viewform"

# Fungsi untuk mengisi formulir
def fill_form():
    driver.get(form_url)
    time.sleep(2)  # Tunggu halaman memuat

    # Dropdown
    dropdown_xpath = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div[1]/div[1]"
    driver.find_element(By.XPATH, dropdown_xpath).click()
    time.sleep(2)
    option_xpath = "/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[2]/div[36]/span"
    driver.find_element(By.XPATH, option_xpath).click()
    time.sleep(2)

    # Pilihan lainnya
    buttons = [
        [  # Age
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div",
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[3]/label/div/div[2]/div/span"
        ],
        [  # Gender
            "/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[1]/label/div/div[1]/div/div[3]/div",
            "/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div"
        ]
    ]

    for button_options in buttons:
        driver.find_element(By.XPATH, random.choice(button_options)).click()
        time.sleep(1)

    # Klik elemen lainnya
    other_buttons = [
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[1]/div/div[3]/div",  # Income
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div",  # Priorities
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/span/div/div[4]/label/div/div[1]/div/div[3]/div",  # Find
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div/span/div/div[5]/label/div/div[1]/div/div[3]/div",  # Price
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div/span/div/label[1]/div[2]/div/div/div[3]/div",  # Important
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div",  # Interested
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div/span/div/label[3]/div[2]/div/div/div[3]/div",  # Often
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div",  # Opinion
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div",  # Recommend
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/span/div/label[5]/div[2]/div/div/div[3]/div",  # Innovation
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div",  # Packaging
        "/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div/div/span/div/div[2]/label/div/div[1]/div/div[3]/div"   # Payment
    ]

    for button_xpath in other_buttons:
        driver.find_element(By.XPATH, button_xpath).click()
        time.sleep(1)

    # Klik tombol Kirim
    send_button = "/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span"
    driver.find_element(By.XPATH, send_button).click()
    time.sleep(5)  # Tunggu form terkirim

    # Klik link untuk mengisi ulang formulir
    link = "/html/body/div[1]/div[2]/div[1]/div/div[4]/a"
    driver.find_element(By.XPATH, link).click()
    time.sleep(5)

# Perulangan pengisian formulir
try:
    for _ in range(10):  # Isi sesuai jumlah iterasi yang diinginkan
        fill_form()
        print("Form selesai diisi...")
        # print("Form selesai diisi. Menunggu 5 menit...")
        #time.sleep(300)  # Jeda 5 menit
finally:
    driver.quit()
