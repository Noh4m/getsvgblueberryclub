from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()
# Select the range of your svg generator
for i in range(1, 11):
    driver.get("https://blueberry.club/p/berry/" + str(i))
    
    time.sleep(.7);
    getSvg = driver.find_elements(By.XPATH, '/html/body/column/column/column[2]/column/column/row/row' )
    for my_href in getSvg:
        with open(  "svg/blueberry#" + str(i) + ".svg", "w") as f:
            f.write(my_href.get_attribute("outerHTML"))
            print("blueberry Generate#" + str(i))


driver.close()