# noinspection PyPackageRequirements
from .drive import Drive, File, convert_os_file_to_faces_dict
from . import keys
from .twitter import Twitter
from .twitch import Twitch
from .wolfram import Wolfram
from .urban import Urban


drive = Drive()
twitter = Twitter()
twitch = Twitch()
wolfram = Wolfram()
urban = Urban()
