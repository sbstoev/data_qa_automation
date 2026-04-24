''' This class loads a configuration from JSON to a dictionary. 
Probably it can be directly applied in the DatabaseManager class'''

import json

class ConfigLoader:

    '''config_path is the parameter in which you put your argument
    Example: config_loader = ConfigLoader("config.json")
    "config.json" is the argument
    ''' 

    def __init__(self, config_path):        
        self.config_path = config_path      # The object (self)congif_path stores the variable "config.json"

    # Defines a method (function in a class) to load the config file:

    def load_config(self):                  
        try:
            with open(self.config_path, "r") as file:   # The file is the config.json, "r" is read
                config = json.load(file)                # The content of the json becomes a dict
                return config
        except Exception as e:
            print("Error loading config:", e)
            return None