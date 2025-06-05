DUNDER METHODS DEFAULT:

__init__ = initainitalizes instances for the class

__str__ = is called when the main fucntion calls for print 

__repr__ = used when the __str__ method is not present in the class


SPECIAL METHODS MATHEMATICAL OPERATORS:

    def __init__(self,number):
        self.number=number
    
    def __add__(self,other):
        return self.number+other
    
    def __sub__(self,other):
        return self.number-other
        
    def __gt__(self,other):
        return self.number>other
        
    def __ge__(self,other):
        return self.number>=other
        
    def __lt__(self,other):
        return self.number<other
        
    def __le__(self,other):
        return self.number<=other
    
    def __truediv__(self,other):
        return self.number/other
    
    def __moddiv__(self,other):
        return self.number/other
    
    def __floordiv__(self,other):
        return self.number/other

    
    def __getitem__(self,other):
        return self.number[key] #in order to access specific elements in a class element, using the get method

