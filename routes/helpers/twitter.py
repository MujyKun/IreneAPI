import datetime
from typing import Optional, Union

from . import (
    self,
    check_permission,
    is_int64,
    GOD,
    OWNER,
    DEVELOPER,
    SUPER_PATRON,
    FRIEND,
    USER,
)
from models import Requestor


async def get_working_twitter_acc():
    """Get a working twitter account if one exists."""
    from resources import twitters

    for idx, twitter_acc in enumerate(twitters):
        if not twitter_acc.exceeded:
            return twitter_acc
        elif (
            twitter_acc.exceeded
            and datetime.datetime.now()
            > twitter_acc.last_tried_at + datetime.timedelta(days=1)
        ):
            return twitter_acc


@check_permission(permission_level=DEVELOPER)
async def _add_twitter_account(
    requestor: Requestor, twitter_id: int, username: str
) -> dict:
    """
    Add a Twitter account's information to the Database.
    """
    return await self.db.execute(
        "SELECT public.addtwitteraccount($1, $2)", int(twitter_id), username.lower()
    )


@check_permission(permission_level=DEVELOPER)
async def get_and_add_twitter_id(requestor: Requestor, username: str) -> dict:
    """
    Get and add a Twitter account to the database if it does not already exist.
    Will search database first and then make an api call.
    """
    username = username.lower()
    response = await self.db.fetch_row(
        "SELECT * FROM public.gettwitterid($1)", username
    )
    if response.get("results"):
        return {"results": {"twitter_id": response["results"]["t_accountid"]}}

    # make a call to twitter api.
    twitter_acc = await get_working_twitter_acc()
    if twitter_acc:
        twitter_id = await twitter_acc.get_user_id(username=username)

        if twitter_id:
            await _add_twitter_account(requestor, twitter_id, username)
            return {"results": {"twitter_id": twitter_id}}
    return {"results": None}


@check_permission(permission_level=DEVELOPER)
async def username_exists(requestor: Requestor, username: str) -> dict:
    exists = False
    twitter_acc = await get_working_twitter_acc()
    if twitter_acc:
        exists = bool(await twitter_acc.get_user_id(username=username))
    return {"results": exists}


@check_permission(permission_level=DEVELOPER)
async def add_twitter_subscription(
    requestor: Requestor, twitter_id: int, channel_id: int, role_id: int = None
) -> dict:
    """
    Make a channel subscribe to a Twitter account.
    """
    is_int64(twitter_id)
    is_int64(channel_id)
    if role_id:
        is_int64(role_id)

    return await self.db.execute(
        "SELECT public.addtwittersubscription($1, $2, $3)",
        twitter_id,
        channel_id,
        role_id,
    )


@check_permission(permission_level=DEVELOPER)
async def delete_twitter_subscription(
    requestor: Requestor, twitter_id: int, channel_id: int
) -> dict:
    """
    Delete a channel's subscription to a Twitter account.
    """
    is_int64(twitter_id)
    is_int64(channel_id)
    return await self.db.execute(
        "SELECT public.deletetwittersubscription($1, $2)", twitter_id, channel_id
    )


@check_permission(permission_level=DEVELOPER)
async def get_all_subscriptions(requestor: Requestor):
    """Get all subscriptions."""
    return await self.db.fetch("SELECT * FROM public.gettwitterchannels")


@check_permission(permission_level=DEVELOPER)
async def get_subscriptions(requestor: Requestor, username):
    """Get all subscriptions for a specific Twitter username."""
    return await self.db.fetch(
        "SELECT * FROM public.gettwitterchannels WHERE username = $1", username
    )


@check_permission(permission_level=DEVELOPER)
async def get_twitter_channels_by_guild(requestor: Requestor, guild_id: int) -> dict:
    """Get specific Twitter channels subscribed to by a guild.

    NOTE: This will return several rows (each row containing a subscription)
    """
    is_int64(guild_id)
    return await self.db.fetch(
        "SELECT * FROM public.gettwitterchannels WHERE guildid = $1", guild_id
    )


@check_permission(permission_level=DEVELOPER)
async def get_timeline(requestor: Requestor, twitter_id: int):
    """
    Get the timeline of an account.

    Will return None if there is no access to a user.
    """
    full_info = dict()
    twitter_acc = await get_working_twitter_acc()
    if twitter_acc:
        full_info = await twitter_acc.get_user_timeline(user_id=twitter_id)
    data = []
    if full_info.get("errors"):
        data = full_info["errors"][0]
    elif full_info.get("data"):
        data = full_info["data"]
    return {"results": data}
