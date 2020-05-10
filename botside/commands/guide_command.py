import botside.commands.base_command
import settings

class Guide(botside.commands.base_command.BaseCommand):

    def __init__(self):
        description = "Authorize command."
        params = []
        super().__init__(description, params)

    async def handle(self, params, message, client):

        url='https://accounts.spotify.com/pl/authorize?scope=playlist-modify-private,playlist-modify-public&response_type=code&redirect_uri=http://0.0.0.0:8080&client_id='+settings.SPOTIFY_CLIENT_ID

        await message.author.send(
        "**Hi!** :hand_splayed:"+
        "\n`--------`"+
        "\n I'm **Spotify Supervisor**. :green_circle:"+
        "\n I'm a **bot** :robot: that allows other users to acces your spotify **playlists**. :newspaper: "+ 
        "\n Follow the **instructions** :label: below to **authorize** :pencil: your spotify account!"+
        "\n`--------`"+
        "\n**1.** *Click the link below and authorize yourself.*"+
        "\n"+url+
        "\n**2.** *After hitting the big green button, copy the* **__URL__** *you have been redirected to and use it as shown in an example.*\t:arrow_right:\t;authorize **SPOTIFY_USERNAME URL**"+
        "\n`--------`"+
        "\n"+message.author.mention)