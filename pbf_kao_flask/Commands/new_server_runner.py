from pbf.templates.template_loader import TemplateLoader
from pbf_kao_flask.templates import TemplatesRoot

class NewServerRunner:
    """ Command to copy script to run KaoFlask Server """
    TEMPLATE_LOADER = TemplateLoader("run_server.py", TemplatesRoot, defaultFilename="run_server.py")
                          
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('filepath', action='store', help='Path to Filename to copy template to')
    
    def run(self, arguments):
        """ Run the command """
        filepath = arguments.filepath
        self.createServerRunner(filepath)
        
    def createServerRunner(self, filepath):
        """ Create a Server Runner """
        self.TEMPLATE_LOADER.copy(filepath)