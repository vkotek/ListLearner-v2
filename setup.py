import configparser
import os

cfg_file = "config.ini"

def ask_y(text):
    if ( input(text) == "y" ):
        return True
    else:
        return False

def main():
    if not os.path.isfile(cfg_file):
        print("Config file not found. Create new?") 
        if not ( ask_y("..") ):
            exit("Bye!")
    

"""
try:
    with open(cfg_file) as f:
        configparser.RawConfigParser()
        
except:
    print("not found")  
"""

if __name__ == "__main__":
    main()
