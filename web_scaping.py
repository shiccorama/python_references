from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://burgerlad.com/burger-king-menu-prices-uk/")

# browser.find_element_by_class_name()
browser.find_element_by_css_selector(".field").send_keys("Double Whopper")

browser.find_element_by_css_selector(".search-icon").click()

browser.find_element_by_css_selector(".all-posts .search-post:first-of-type h3 a").click()

browser.implicitly_wait(3)

views_count = browser.find_element_by_css_selector(".z-info .z-info:last-of-type span:last-child")

browser.implicitly_wait(3)

print(views_count.get_attribute("innerHTML"))

browser.quit()