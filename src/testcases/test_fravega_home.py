import unittest
from src.pageobjects.FravegaHomePage import FravegaPage

class search_heladera(unittest.TestCase):
    
    def setUp(self):
        self.page = FravegaPage()
        self.page.inicializarPage()# go to the fravega page


    def test_search_heladera(self):
        
        self.page.isTitlePresent() # verify the current title of the page
        self.page.insert_element_to_found("Heladera") #just insert the string to the searh input text
        self.page.submit_search()#this method just click to the submit button
        self.page.show_all_brands_available()# click over the tag 'Ver todas' to show all available brands over the current search
        self.page.select_specific_brand("Whirlpool")
        self.page.submit_specific_brand()
        self.page.verify_items_founded()
        
    def tearDown(self):
        self.page.close_driver()
        
    

if __name__ == '__main__':
    unittest.main()
    
    
    
    
    
    
    
