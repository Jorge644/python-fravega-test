lista2 = [1,2,3,4,5,6]
f = open("../outputs/results.txt", "w")
for item in lista2:
    f.write(str(item)+ "\n")
f.close()


class Save_file():
    
    def __init__(self, file,form):
        self.file = open(file,form)
        
        
    def save_text(self,text_to_save):
            self.file.write(str(text_to_save))
    
    def close_file(self):
        self.file.close()
        
        
        
        
