from selenium_support import Driver

mainLogFile = "/logFile.log"
scboyHome = "https://www.scboy.com/"

username = ""
password = ""

driver = Driver(mainLogFile)
driver.open_browser(scboyHome)

# go to login page
if driver.exist_element("//ul[@class='navbar-nav']"):
    driver.click_element("//ul[@class='navbar-nav']")
elif driver.exist_element("//i[@class='icon-user icon']"):
    driver.click_element("//i[@class='icon-user icon']")

# type username, password and get access
driver.text_element(username, "//input[@id='mobile']")
driver.text_element(password, "//input[@id='password']")
driver.click_element("//button[@id='submit']")

# go to 乔伊雷酒吧
driver.click_element("//div/a[contains(text(), '乔伊雷酒吧')]")
while True:
    title = driver.find_element("//ul[contains(@class, 'threadlist')]")

    driver.click_element(ele=title)
    thumbUps = driver.find_elements("//i[@class='icon icon-thumbs-o-up']")
    for thumbUp in thumbUps:
        driver.click_element(ele=thumbUp)
