import requests
import json
import unittest
import re

class RestBreweries(unittest.TestCase):
    
    LIST_RESULTS =[]
    URL_ENDPOINT = "https://api.openbrewerydb.org/breweries/"

    def test_get_breweries_by_name(self):
        breweries_name = "lagunitas"
        url_endpoint =  self.URL_ENDPOINT + "autocomplete?query={}".format(breweries_name)
        
                        
        response = requests.get(url_endpoint) #CALL GET METHOD TO THE ENDPOINT
        print("\n Status code ==> " , response.status_code)
        assert response.status_code == 200  #VERIFY THE STATUS CODE SHOULD BE 200 
        result = json.loads(response.text) # PARSE THE RESULT TO A LIST OF JSON
        
        for item in result:
            patron = "Lagunitas Brewing Co"
            text = item["name"]
            isFounded  = re.findall(patron, text) # VERIFY IF CONTAINS THE NAME Lagunitas Brewing Co IN THE CURRENT RESULT
            if len(isFounded) > 0:
                self.LIST_RESULTS.append(item["id"]) # SAVE THE CURRENT ID FOR THE NEXT TEST CASE
            
        print("\n Se obtuvieron los siguientes id ==> " , self.LIST_RESULTS)
    
    def test_get_breweries_by_id(self):
        
        
        if len(self.LIST_RESULTS) > 0: #Verify if the list has elements
            for l_id in self.LIST_RESULTS: # iterate over elements to call get method using id
                url_endpoin = self.URL_ENDPOINT+"{}".format(l_id) #formating the endpoint to specify the current ID
                response = requests.get(url_endpoin) # call get method
                assert response.status_code == 200 # verify the status code should be 200
                l_json = json.loads(response.text) # parsing the response to a json
                if l_json["state"] == "california": # verify the current value of the atributte state
                    assert l_json["id"] == 761 
                    assert l_json["name"] =="Lagunitas Brewing Co"
                    assert l_json["street"] == "1280 N McDowell Blvd"
                    assert l_json["phone"] == "7077694495"
                    




if __name__ == '__main__':
    unittest.main()