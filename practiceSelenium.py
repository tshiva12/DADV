from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options

chromeOptions = webdriver.ChromeOptions()
# options = Options()
# options.add_argument("--disable-notifications")
preferences = {"download.default_directory" : "G:\\MSIT\\1-1\\Data Science Specialization\\4.DADV\\2.IMDB Assignment\\ZZ"}
# options.add_experimental_option("prefs", preferences)
chromeOptions.add_experimental_option("prefs", preferences)
chromedriver = "C:\\Program Files\\Chrome\\chromedriver.exe"
browser = webdriver.Chrome(executable_path=chromedriver, options=chromeOptions)
browser.maximize_window()
time.sleep(5)

# browser.get("https://sensongsmp3.co.in/")
# time.sleep(5)

# browser.find_element_by_xpath("//a[contains(text(), 'Telugu Songs')]").click()
# time.sleep(5)

# browser.find_element_by_xpath("//a[contains(text(), 'Ala Vaikuntapuramulo')]").click()
# time.sleep(5)

# browser.find_element_by_xpath("//a[contains(text(), '320 Kbps')]").click()
# time.sleep(5)

# browser.find_element_by_xpath("//a[contains(text(), 'Download | డౌన్లోడ్')]").click()
# time.sleep(5)

# browser.switch_to.window(browser.window_handles[0])
# time.sleep(5)

# browser.find_element_by_xpath("//a[contains(text(), 'Download | డౌన్లోడ్')]").click()
# time.sleep(5)

# browser.quit()

browser.get("https://paytm.com/")
time.sleep(5)

browser.find_element_by_class_name("_3ac-").click()
time.sleep(5)

iframe = browser.find_element_by_tag_name('iframe')
browser.switch_to.frame(iframe)

# print("hi")
browser.find_element_by_xpath("//span[contains(text(), 'password')]").click()
time.sleep(5)

browser.find_element_by_name("username").send_keys("8187823307")
time.sleep(5)

browser.find_element_by_name("password").send_keys("Shiva@123")
time.sleep(5)

browser.find_element_by_xpath("//span[contains(text(), 'Login Securely')]").click()
time.sleep(5)
