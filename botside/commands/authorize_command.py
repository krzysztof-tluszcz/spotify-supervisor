import botside.commands.base_command
import settings
import re

class Authorize(botside.commands.base_command.BaseCommand):

    def __init__(self):
        description = "Authorize command."
        params = ["username","url"]
        super().__init__(description, params)

    async def handle(self, params, message, client):
        
        spotify_username = params[0]
        url = params[1]
        code = url.split("code=",1)[1]

        print("\n"+spotify_username+"\n"+str(message.author.id)+"\n"+code)


