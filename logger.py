#Not perfect system log, but I prefer keep it simple for now 
import logging 

class Logger :
    def __init__(self, levelApp, formatApp, encodingApp, fileNameApp) :
        self.logging = logging
        logging.basicConfig(format =formatApp ,filename=fileNameApp, encoding=encodingApp, level=levelApp)
    
    
    def LogInDebugLevel(self, message) :
        self.logging.debug(message)


    def LogInInfoLevel(self, message) :
        self.logging.info(message)


    def LogInWarningLevel(self, message) : 
        self.logging.warning(message)


    def LogInErrorLevel(self, message) :
        self.logging.error(message)