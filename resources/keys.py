import os
from dotenv import load_dotenv


load_dotenv()  # Adds .env to memory
# postgres db connection
postgres_options = {
    "db_host": os.getenv("POSTGRES_HOST"),
    "db_name": os.getenv("POSTGRES_DATABASE"),
    "db_user": os.getenv("POSTGRES_USER"),
    "db_pass": os.getenv("POSTGRES_PASSWORD"),
    "db_port": os.getenv("POSTGRES_PORT"),
}

# Idol Avatar Location (include / at the end)
# IDOL_AVATAR_LOCATION="/var/www/images.irenebot/public_html/avatar/"
avatar_location = os.getenv("IDOL_AVATAR_LOCATION")

# Idol Banner Location (include / at the end)
banner_location = os.getenv("IDOL_BANNER_LOCATION")

# Bias Game Folder Location (include / at the end)
bias_game_location = os.getenv("BIAS_GAME_LOCATION")

# DataDog - DO NOT CHANGE NAMES OF THESE ENV VARIABLES - https://github.com/DataDog/datadogpy
datadog_api_key = os.getenv("DATADOG_API_KEY")
datadog_app_key = "DATADOG_APP_KEY"

# BlackJack Card Location
# CARD_LOCATION="/var/www/images.irenebot/public_html/cards/"
card_location = os.getenv("CARD_LOCATION")

# API
api_port = os.getenv("API_PORT")

# Private Keys are separated by commas
private_keys: list = (os.getenv("PRIVATE_KEYS")).split(",")

person_folder = os.getenv("FOLDER_LOCATION")

# MAIN SITE
main_site_port = os.getenv("SITE_PORT")

bot_invite_link = os.getenv("BOT_INVITE_LINK")
support_server_id = os.getenv("SUPPORT_SERVER_ID")
support_server_link = os.getenv("SUPPORT_SERVER_LINK")
bot_website = os.getenv("BOT_WEBSITE")
image_host = os.getenv("IMAGE_HOST")
github_url = os.getenv("GITHUB_LINK")

top_gg_webhook_key = os.getenv("TOP_GG_WEBHOOK")

patreon_url = os.getenv("PATREON_LINK")

urban_key = os.getenv("URBAN_KEY")

twitter_account_ids = os.getenv("TWITTER_ACCOUNT_IDS").split(",")
twitter_usernames = os.getenv("TWITTER_USERNAMES").split(",")
twitter_consumer_keys = os.getenv("TWITTER_CONSUMER_KEYS").split(",")
twitter_consumer_secrets = os.getenv("TWITTER_CONSUMER_SECRETS").split(",")
twitter_access_keys = os.getenv("TWITTER_ACCESS_KEYS").split(",")
twitter_access_secrets = os.getenv("TWITTER_ACCESS_SECRETS").split(",")

twitch_client_id = os.getenv("TWITCH_CLIENT_ID")
twitch_client_secret = os.getenv("TWITCH_CLIENT_SECRET")

wolfram_app_id = os.getenv("WOLFRAM_APP_ID")

# db_conn = psycopg2.connect(**postgres_options)
# c = db_conn.cursor()
