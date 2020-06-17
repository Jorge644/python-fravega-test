from src.testcases.test_rest_api import RestBreweries
from src.testcases.test_fravega_home import search_heladera

import HtmlTestRunner
import os 
import unittest

if __name__ == '__main__':
    current_directory = os.getcwd()
    consolidate_test = unittest.TestSuite()
    #ADD the test cases
    consolidate_test.addTests([
        unittest.defaultTestLoader.loadTestsFromTestCase(RestBreweries),
        unittest.defaultTestLoader.loadTestsFromTestCase(search_heladera)
        ])
    #Save the output file 
    output_file = open(current_directory  + "\HTML_TEST_RUNNER.HTML" , "w")
    
    #
    html_runner= HtmlTestRunner.HTMLTestRunner(
            stream = output_file,
            report_title = "HTML Reporting using unittest",
            descriptions= "Jorge prueba"
            )
    html_runner.run(consolidate_test)
    
    
    
    
    
