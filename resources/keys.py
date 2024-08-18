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
datadog_app_key = os.getenv("DATADOG_APP_KEY")

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
discord_auth_url = os.getenv("DISCORD_AUTH_URL")
discord_client_id = os.getenv("DISCORD_CLIENT_ID")
discord_client_secret = os.getenv("DISCORD_CLIENT_SECRET")
discord_redirect_uri = os.getenv("DISCORD_REDIRECT_URI")
signing_key = os.getenv("COOKIE_SIGNING_KEY")
support_server_id = os.getenv("SUPPORT_SERVER_ID")
support_server_link = os.getenv("SUPPORT_SERVER_LINK")
bot_website = os.getenv("BOT_WEBSITE")
image_host = os.getenv("IMAGE_HOST")
github_url = os.getenv("GITHUB_LINK")

encryption_key = os.getenv("ENCRYPTION_KEY")

top_gg_webhook_key = os.getenv("TOP_GG_WEBHOOK")

patreon_url = os.getenv("PATREON_LINK")

urban_key = os.getenv("URBAN_KEY")

twitch_client_id = os.getenv("TWITCH_CLIENT_ID")
twitch_client_secret = os.getenv("TWITCH_CLIENT_SECRET")

wolfram_app_id = os.getenv("WOLFRAM_APP_ID")

# db_conn = psycopg2.connect(**postgres_options)
# c = db_conn.cursor()
