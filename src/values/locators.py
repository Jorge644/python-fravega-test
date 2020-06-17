from selenium.webdriver.common.by import By

search_locator = (By.XPATH , "//input[@placeholder='Buscar productos']")
search_button_locator = (By.CSS_SELECTOR , "button[class*='InputBar']")
all_brands_locator = (By.XPATH, "//li[@name='brandsFilter'] //a[text()='Ver todas']")
find_specify_brand_locator = (By.XPATH, "//div[@class='ant-modal-body'] //label[text()='{}']")
pagination_locator = (By.XPATH, "//ul[@class='ant-pagination']/li")
items_founded_locator = (By.XPATH, "//ul[@name='itemsGrid']/li")
submit_specific_brand_locator = (By.XPATH, "//div[@class='ant-modal-body'] //button[@id='apply']")
title_search_element_locator = (By.CSS_SELECTOR,"//h4")  
