'''
This class defines a single folder in the virtual filestructure
A folder has one parent, and any number of children which are folders below it, and files within it
'''

class Folder:
    location_string = ""
    children = []
    parent = None
    files = []
    name = ""

    def get_parent(self):
        return self.parent

    def set_parent(self, folder):
        self.parent = folder

    def get_child(self, name):
        if self.has_child(name)
            for i in children:
                if (i.get_name() is name):
                    return i
        return False

    def add_child(self, child):
        children.add(child)

    def has_child(self, name):
        if name in map(lambda iname: iname.get_name(), self.children):
            return True
        return False

    def remove_child(self, child):
        if (self.has_child(child)):
            self.children.remove(child)
            return True
        else:
            return False

    def has_file(self, fname):
        if fname in map(lambda ifname: ifname.get_name(), self.files):
            return True
        return False    

    def get_file(self, fname):
        if (self.has_file()):
            for i in files:
                if (i.get_name() is name):
                    return i
        return False

    def add_file(self, child):
        self.files.add(child)
        
    def remove_file(self, fname):
        if (self.has_file()):
            f = self.get_file(fname):
            self.files.remove(f)
            return True
        return False

    def is_same(self, folder):
        pass

    def get_files(self):
        return files

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
        

