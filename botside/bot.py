import discord
import settings
import botside.message_handler

async def common_handle_message(message, client):
    text = message.content
    if text.startswith(settings.COMMAND_PREFIX) and text != settings.COMMAND_PREFIX:
        cmd_split = text[len(settings.COMMAND_PREFIX):].split()
        try:
            await botside.message_handler.handle_command(cmd_split[0].lower(), 
                                    cmd_split[1:], message, client)
        except:
            print("Error while handling message", flush=True)
            raise

class Bot(discord.Client):
    async def on_ready(self):
        game = discord.Game(name=settings.NOW_PLAYING)
        if settings.NOW_PLAYING:
            await self.change_presence(activity=game)

    async def on_message(self, message):
        if message.author == self.user:
            return
        else:
            await common_handle_message(message, self)