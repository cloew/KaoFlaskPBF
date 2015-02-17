from pbf.templates.template_loader import TemplateLoader
from pbf_kao_flask.templates import TemplatesRoot

class NewServer:
    """ Command to create a new Server """
    TEMPLATE_LOADER = TemplateLoader("server_init.py", TemplatesRoot, defaultFilename="__init__.py")
                          
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('filepath', action='store', help='Path to Filename to copy template to')
    
    def run(self, arguments):
        """ Run the command """
        filepath = arguments.filepath
        self.createServer(filepath)
        
    def createServer(self, filepath):
        """ Create a Server """
        self.TEMPLATE_LOADER.copy(filepath)