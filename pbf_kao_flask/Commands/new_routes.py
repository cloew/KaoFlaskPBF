from pbf.helpers.file_helper import IsDirectory
from pbf_kao_flask.templates import TemplatesRoot
from pbf.templates import template_manager

import os

class NewRoutes:
    """ Command to add a new routes file """
                          
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('filepath', action='store', help='Path to Filename to copy template to')
    
    def run(self, arguments):
        """ Run the command """
        filepath = arguments.filepath
        self.createRoutes(filepath)
        
    def createRoutes(self, filepath):
        """ Create a Routes """
        if IsDirectory(filepath):
            filepath = os.path.join(filepath, 'routes.py')
        keywords = {}
        template_manager.CopyTemplate(filepath, "routes.py", keywords, TemplatesRoot) # Add proper template file name here