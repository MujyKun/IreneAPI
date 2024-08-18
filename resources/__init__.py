# noinspection PyPackageRequirements
from .drive import Drive, File, convert_os_file_to_faces_dict
from . import keys
from .twitch import Twitch
from .wolfram import Wolfram
from .urban import Urban
from .datadog import DataDog
from .tiktok import Tiktok
from .discord import Discord


drive = Drive()
twitch = Twitch()
wolfram = Wolfram()
urban = Urban()
datadog = DataDog()
tiktok = Tiktok()
discord = Discord()
