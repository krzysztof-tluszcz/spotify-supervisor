import discord
from sanic import Sanic
import asyncio
import settings
from botside.bot import Bot
from serverside.router import Router

def main():
    bot = Bot()
    bot_app = bot.start(settings.temp_token)
    bot_task = asyncio.ensure_future(bot_app)

    server = Sanic("Spotify Supervisor")
    server_app = server.create_server(host="0.0.0.0", port="8080", return_asyncio_server=True)
    server_task = asyncio.ensure_future(server_app)
    router = Router()
    router.register_routes(server)

    loop = asyncio.get_event_loop()
    loop.run_forever()

    return

if __name__ == "__main__":
    main()