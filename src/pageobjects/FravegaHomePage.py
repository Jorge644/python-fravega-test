from src.pageobjects.BasePage import Base
from src.values import strings, locators
from src.helpers.file import Save_file
from src.helpers.some_functions import verify_title_over_items
import re 



class FravegaPage(Base):
    BRAND_TO_FOUND =""
    NUMBERS_OF_ITEM_FOUND=0
    
    
    def __init__(self):
        super().__init__()
        
        
    def inicializarPage(self):
        self.driver.get(strings.url_fravega)
        self.driver.maximize_window()
        
    def isTitlePresent(self):
        l_title  = self.driver.title
        assert l_title == strings.fravega_title
        
    def insert_element_to_found(self,item_to_found):
        '''Only insert the word in the input text'''
        l_element = self.find_element(*locators.search_locator)
        l_element.send_keys(item_to_found)
        
    def submit_search(self):
        
        l_element = self.find_element(*locators.search_button_locator)
        l_element.click()
        
    def show_all_brands_available(self):
        
        l_element  = self.find_element(*locators.all_brands_locator)
        l_element.click()
        
    def select_specific_brand(self, brand):
        '''This method find an specify brand given, and save the current
        brand and the specify number of elements founded'''
        
        
        self.BRAND_TO_FOUND = brand
        l_locator = (locators.find_specify_brand_locator[0],
                     locators.find_specify_brand_locator[1].format(brand))
        
        l_element = self.visibility_of_element(*l_locator)
        name_brand_patron = "[a-zA-Z]+"
        i_brand_founded_patron = "[0-9]+"
        name_brand_found = re.findall(name_brand_patron, l_element.text)
        i_brand_found = re.findall(i_brand_founded_patron, l_element.text)
        self.NUMBERS_OF_ITEM_FOUND = int(i_brand_found[-1])
        assert brand == name_brand_found[-1]
        l_element.click()
        
    def submit_specific_brand(self):
        l_element = self.find_element(*locators.submit_specific_brand_locator)
        l_element.click()
        
        
        
    def verify_items_founded(self):
        '''This method verify how many items are displayed in the fronted and compare 
        to the NUMBER_OF_ITEMS_FOUND. 
        Iterate over the currents items founds and verify the title contains the
        specify brand'''
        
        l_list = self.find_elements(*locators.items_founded_locator)#Get the current grid of elements founded
        verify_title_over_items(l_list, self.BRAND_TO_FOUND, locators.items_founded_locator, "w")# verify the title over each item
        
        l_pagination = self.find_elements(*locators.pagination_locator)
        
        '''compare the len and verify if there is more than 1 pagination for the
        current search , considering that the first position is for 'Anterior'
        the last position for 'Siguiente' and the position between them are the 
        pagination for the all the items of the searchs'''
        
        if len(l_pagination) > 3:      
            for idx, value in enumerate(l_pagination):
                if (idx == 0 or idx == 1 or idx == len(l_pagination) - 1):
                    pass
                else:
                    value.click()
                    l_grid = self.visibility_of_elements(*locators.items_founded_locator)
                    verify_title_over_items(l_grid, self.BRAND_TO_FOUND, locators.items_founded_locator, "a")
                    
                    
        
            
                    
            
            
        
        
        
        
        
        
    
    
