class File:
    name = ""
    contents = [] # List of lines
    
    def __init__(self):
        pass
        
    def get_contents(self):
        return self.contents
        
    def set_contents(self, new_contents):
        self.contents = new_contents
        return True
    
    def get_name(self):
        return self.name
        
    def set_name(self, new_name):
        self.name = new_name
        return True
        
    def get_owner(self):
        return self.owner
    
    def set_owner(self, new_owner):
        self.owner = new_owner
        return True
        
    def is_equal(self, other):
        if (self.name is other.name):
            if (self.contents is other.contents):
                return True
        return False