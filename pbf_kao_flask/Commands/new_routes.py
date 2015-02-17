from pbf.templates.template_loader import TemplateLoader
from pbf_kao_flask.templates import TemplatesRoot

import os

class NewRoutes:
    """ Command to add a new routes file """
    TEMPLATE_LOADER = TemplateLoader("routes.py", TemplatesRoot, defaultFilename="routes.py")
                          
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('filepath', action='store', help='Path to Filename to copy template to')
    
    def run(self, arguments):
        """ Run the command """
        filepath = arguments.filepath
        self.createRoutes(filepath)
        
    def createRoutes(self, filepath):
        """ Create a Routes """
        self.TEMPLATE_LOADER.copy(filepath)