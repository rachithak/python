x = "Global"

def outer():
    x = "Enclosing"
    
    def inner():
        x = "Local"
        print(x) # 1. Searches Local first -> prints "Local"
        
    inner()

outer()