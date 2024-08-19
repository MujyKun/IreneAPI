import datetime
from typing import Optional

from . import (
    self,
    check_permission,
    is_int64,
    generate_cookie,
    encrypt_data,
    decrypt_data
)
from datetime import datetime

from quart import session, jsonify, redirect
from resources import discord
from resources.keys import discord_auth_url


async def handle_discord_login(code: str, fallback_url: str = None):
    """Handle a discord login.

    :param code: str
    :param fallback_url: Optional[str]
        Where to send the user after logging in.
    """
    access_token, expires_at, refresh_token, scope = await discord.fetch_user_token(code)
    if not access_token:
        return jsonify({"error": "Invalid code parameter"}), 400

    await process_new_access_token(access_token, expires_at, refresh_token, scope)

    if fallback_url:
        return redirect(fallback_url)

    return redirect("/")


async def get_session_details(session_id: str = None):
    """
    Get a session's details

    :param session_id: str
        An existing session id.
    :returns:
        access_token, refresh_token, expires_at, scope
    """
    existing_session_id = session_id or session.get('session_id')
    select_query = """
        SELECT access_token, refresh_token, expires_at, scope FROM public.discordtokens WHERE session_id = $1
    """
    data = await self.db.fetch_row(select_query, existing_session_id)
    results = data.get('results') or {}
    access_token = results.get('access_token')
    refresh_token = results.get('refresh_token')
    expires_at = results.get('expires_at')
    scope = results.get('scope')
    return decrypt_data(access_token), expires_at, decrypt_data(refresh_token), scope


async def delete_current_session() -> bool:
    """
    Delete the current session

    :returns: bool
        Whether the session was deleted.
    """
    try:
        existing_session_id = session.pop("session_id")
    except KeyError:
        return False

    delete_query = """
        DELETE FROM public.discordtokens WHERE session_id = $1
    """
    await self.db.execute(delete_query, existing_session_id)
    return True


async def process_new_access_token(access_token, expires_at, refresh_token, scope) -> str:
    """
    Process a new access token and session.

    :param access_token: str
        Access Token
    :param expires_at: datetime.datetime
        Datetime object
    :param refresh_token: str
        Refresh Token
    :param scope: str
        Scope
    :return: str
        New Access Token
    """
    await delete_current_session()

    cookie = generate_cookie()

    insert_query = """
        INSERT INTO public.discordtokens(session_id, access_token, refresh_token, scope, expires_at) 
        VALUES ($1, $2, $3, $4, $5)
    """

    encrypted_refresh_token = encrypt_data(refresh_token)
    encrypted_access_token = encrypt_data(access_token)

    result = await self.db.execute(insert_query, cookie, encrypted_access_token, encrypted_refresh_token, scope, expires_at)
    session['session_id'] = cookie
    return access_token


async def get_access_token() -> Optional[str]:
    """
    Returns an access token while handling any necessary refreshes.

    :returns: str
        access token
    """
    access_token, expires_at, refresh_token, _ = await get_session_details()

    if not access_token:
        return None

    if datetime.utcnow() > expires_at:
        access_creds = await discord.refresh_access_token(refresh_token)
        access_token = await process_new_access_token(*access_creds)

    return access_token


async def get_user_info():
    """Get the current user's info"""
    access_token = await get_access_token()
    if not access_token:
        return {"error": "Not Logged In"}

    return await discord.get_user(access_token)


async def is_logged_in() -> bool:
    """
    Get whether the user is logged in.

    Does not check if the access token is still active.

    :return: bool
        Whether the user is still logged in (a session exists)
    """
    return bool(session.get("session_id"))

    # Getting the access token will take longer for verifying and requires a sql operation.
    # return bool(await get_access_token())
