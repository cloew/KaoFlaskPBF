from pbf_kao_flask.Commands.new_routes import NewRoutes
from pbf_kao_flask.Commands.new_server import NewServer
from pbf_kao_flask.Commands.new_server_runner import NewServerRunner

import os

class MakeServer:
    """ Command to create a KaoFlask Server directory structure """
                          
    def addArguments(self, parser):
        """ Add arguments to the parser """
        parser.add_argument('root', action='store', help='Root directory to add the Server directory in')
    
    def run(self, arguments):
        """ Run the command """
        self.make(arguments.root)
        
    def make(self, rootDirectory):
        """ Make the directory structure """
        NewServerRunner().createServerRunner(rootDirectory)
        
        serverDir = os.path.join(rootDirectory, "Server")
        os.mkdir(serverDir)
        NewRoutes().createRoutes(serverDir)
        NewServer().createServer(serverDir)
        
        for dir in ['static', 'static/js', 'static/partials', 'static/stylesheets', 'templates']:
            os.mkdir(os.path.join(serverDir, dir))