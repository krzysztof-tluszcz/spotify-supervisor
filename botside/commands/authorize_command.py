import botside.commands.base_command
import settings

class Authorize(botside.commands.base_command.BaseCommand):

    def __init__(self):
        description = "Authorize command."
        params = []
        super().__init__(description, params)

    async def handle(self, params, message, client):
        return


