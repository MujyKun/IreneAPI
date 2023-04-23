# noinspection PyPackageRequirements
from .drive import Drive, File, convert_os_file_to_faces_dict
from . import keys
from .twitter import Twitter
from .twitch import Twitch
from .wolfram import Wolfram
from .urban import Urban
from .datadog import DataDog
from .tiktok import Tiktok
from .theysaidso import TheySaidSo

twitters = []

for idx, account_id in enumerate(keys.twitter_account_ids):
    consumer_key = keys.twitter_consumer_keys[idx]
    consumer_secret = keys.twitter_consumer_secrets[idx]
    access_key = keys.twitter_access_keys[idx]
    access_secret = keys.twitter_access_secrets[idx]
    _twitter = Twitter(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_key,
        access_token_secret=access_secret,
    )
    twitters.append(_twitter)


drive = Drive()
twitch = Twitch()
wolfram = Wolfram()
urban = Urban()
datadog = DataDog()
tiktok = Tiktok()
theysaidso = TheySaidSo()
