from BWFMUSIC.core.bot import romeomusic
from BWFMUSIC.core.dir import dirr
from BWFMUSIC.core.git import git
from BWFMUSIC.core.userbot import Userbot
from BWFMUSIC.misc import dbb, heroku
from BWFMUSIC.logging import LOGGER

git()


dirr()

dbb()

heroku()

# Clients
app = romeomusic()

userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()
