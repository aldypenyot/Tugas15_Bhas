from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path = ChromeDriverManager().install())

driver=webdriver.Chrome(service=service)
driver.get("https://www.google.com/")

from selenium.webdriver.common.keys import Keys #import keys(keyboard)
from selenium.webdriver.common.by import By #import tag by(name, id, css selector)
import time

#get searchbox dan isi searchbox

searchbox=driver.find_element(By.NAME,"q")
searchbox.send_keys("Alfamart")

time.sleep(5)

#cara kirim/klik enter pada search box
searchbox.send_keys(Keys.RETURN)

# #click button search setelah isi searchbox
# buttonSearch = driver.find_element(By.NAME,"btnK")
# buttonSearch.click()

label_result=driver.find_element(By.ID,"result-stats")
print(label_result.text)

# cari harga saham
nilai_saham=driver.find_elements(By.CSS_SELECTOR, '.kno-fv span') #css selector
print(nilai_saham[2].text)
#index=0
#for span in spans:
#    print(f"{index} - {span.text}")
#    index=index

saham=driver.find_element(By.XPATH, '//span[@class="kno-fv"]/span[3]') #xPATH
print(saham.text)
driver.save_screenshot("alfamart_page.png") #mengambil screenshot

#execute javascript

driver.execute_script("window.scrollBy(0,10000);")
driver.save_screenshot("alfamart_page_bawah.png")

time.sleep(10)