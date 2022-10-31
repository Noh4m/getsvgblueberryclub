from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Render Start at =", current_time)
driver = webdriver.Firefox()
# Select the range of your svg generator
for i in range(1, 10001):
    driver.get("https://blueberry.club/p/berry/" + str(i))
    time.sleep(1);
    getSvg = driver.find_elements(By.XPATH, "//row[@class='•29']//*[name()='svg'][1]" )
    for my_href in getSvg:
        with open(  "svg/blueberry#" + str(i) + ".svg", "w", encoding="utf-8") as f:
            f.write(my_href.get_attribute("outerHTML"))
            print("blueberry Generated#" + str(i))

print("Render finish at =", current_time)
driver.close()