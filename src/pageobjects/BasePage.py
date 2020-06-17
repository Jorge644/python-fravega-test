from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from src.values import strings



class Base():
    
    def __init__(self):
        self.driver = webdriver.Chrome(strings.path_driver)
        self.driver.implicitly_wait(10)
        
    
    
    def close_driver(self):
        self.driver.close()
        
    def find_element(self,by_name, by_value):
        element = self.driver.find_element(by_name, by_value)
        return element
    
    def find_elements(self,by_name, by_value):
        elements = self.driver.find_elements(by_name, by_value)
        return elements
    
    def visibility_of_element(self,by_name, by_value):
        try:     
            element = WebDriverWait(self.driver,10).until(
                      EC.visibility_of_element_located((by_name,by_value)))
            
            return element
        except(StaleElementReferenceException) as error:
            print(error.args)
            
    def visibility_of_elements(self, by_name, by_value):
        try:
            elements = WebDriverWait(self.driver,10).until(
                EC.visibility_of_all_elements_located((by_name,by_value)))
            return elements
        except(StaleElementReferenceException) as error:
            print(error.args)
            
        
        
        
        
        
        
        