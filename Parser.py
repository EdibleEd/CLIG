import datetime
import random
#import subprocess
#import platform

def clear(): # not functional
    print(chr(27) + "[2J")
    
# Maybe have a set of methods for entering username etc before this?

class Parser:
    #folder = Folder("root")
    username = "4DM1N"
    is_first_run = True
    instruction_loc = "~/howto"
    sys_name = "HELIOS"
    
    def __init__(self):    
        # load state from file
        
        # if that fails, decide it is first run and populate with initial state
        pass
        
    def first_run(self):
        #load_folder_tree(fname):
        
        # set today as last logon date
        self.last_logon = datetime.datetime.today()
        self.is_first_run = False
    
    def begin(self):
        if(self.is_first_run):
            self.first_run()
            print()
            print("Welcome to {}, {}".format(self.sys_name, self.username))
            print("Since this is your first logon, usage instructions have been provided at {}".format(self.instruction_loc))
            print("Enter 'help' for help and a command list.".format(self.instruction_loc))
            print("Enjoy your stay and use the system responsibly")
            print()
            self.main_loop()
        else:
            print("Welcome back {}".format(self.username))
            print("Last logon was on: {} at {}.".format(self.last_logon.strftime("%d/%m/%y"), self.last_logon.strftime("%H:%M:%S")))
            print()
            self.main_loop()
            
    def main_loop(self):
        while True:
            command = raw_input("> ")
            token_command = self.tokenize(command)
            execute_command(token_command)
    def execute_command(self, command):
        pass
        
    def logout(self):
        self.last_logon = datetime.datetime.today()
        # write to config?
        pass
        
    def tokenize(command):
        pass
        
    def save(self):
        # Store useful info
        pass
        
    def read_token(self):
        pass

    def change_environment(self):
        pass
        
    def load_folder_tree(self):
        pass
        
    def help(self):
        pass
        
