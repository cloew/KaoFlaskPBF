from pbf.Commands.command_manager import CommandConfig, RegisterCommands

commands = [CommandConfig("mk server", "pbf_kao_flask.Commands.mk_server.MakeServer", description="Make a KaoFlask Server Directory")]

RegisterCommands(commands)