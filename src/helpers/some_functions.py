from .file import Save_file
from src.values import strings



def verify_title_over_items(list_input,expected_title, locator , form):
    file = Save_file(strings.file_elements_path,form)
    for idx, value in enumerate(list_input):
        
        title_webelement = value.find_element(*locator)
        title_text = title_webelement.text
        file.save_text(str(idx)+"- "+title_text+"\n")
        assert expected_title in title_text
    
    file.close_file()
        

            
            
        
        