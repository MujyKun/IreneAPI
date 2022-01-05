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
from resources import twitter


@check_permission(permission_level=DEVELOPER)
async def add_twitter_account(
    requestor: Requestor, account_id: int, username: str
) -> dict:
    """
    Add a Twitter account's information to the Database.
    """
    return await self.db.execute(
        "SELECT public.addtwitteraccount($1, $2)", account_id, username.lower()
    )


@check_permission(permission_level=DEVELOPER)
async def delete_twitter_account(requestor: Requestor, account_id: int) -> dict:
    """Delete a Twitter account from the Database."""
    is_int64(account_id)
    return await self.db.execute("SELECT public.deletetwitteraccount($1)", account_id)


@check_permission(permission_level=DEVELOPER)
async def add_twitter_subscription(
    requestor: Requestor, account_id: int, channel_id: int, role_id: int = None
) -> dict:
    """
    Make a channel subscribe to a Twitter account.
    """
    is_int64(account_id)
    is_int64(channel_id)
    if role_id:
        is_int64(role_id)

    return await self.db.execute(
        "SELECT public.addtwittersubscription($1, $2, $3)",
        account_id,
        channel_id,
        role_id,
    )


@check_permission(permission_level=DEVELOPER)
async def delete_twitter_subscription(
    requestor: Requestor, account_id: int, channel_id: int
) -> dict:
    """
    Delete a channel's subscription to a Twitter account.
    """
    is_int64(account_id)
    is_int64(channel_id)
    return await self.db.execute(
        "SELECT public.deletetwittersubscription($1, $2)", account_id, channel_id
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
        return response

    # make a call to twitter api.
    account_id = await twitter.get_user_id(username=username)

    if account_id:
        await add_twitter_account(requestor, account_id, username)
        return {"results": {"account_id": account_id}}


@check_permission(permission_level=DEVELOPER)
async def get_subscriptions(
    requestor: Requestor, twitter_info: Optional[Union[int, str]]
):
    """
    Get the subscriptions of one or several accounts.
    """
    query = "SELECT accountid, channelid, roleid FROM public.twitterfollowage"
    if isinstance(twitter_info, str):
        twitter_id = await get_and_add_twitter_id(twitter_info)
    elif isinstance(twitter_info, int):
        twitter_id = twitter_info
    else:
        return await self.db.fetch(query)

    return await self.db.fetch(f"{query} WHERE accountid = $1", twitter_id)


@check_permission(permission_level=DEVELOPER)
async def get_accounts(requestor: Requestor):
    """
    Get the list of saved account ids and usernames.
    """
    return await self.db.fetch("SELECT accountid, username FROM public.twitteraccounts")


@check_permission(permission_level=DEVELOPER)
async def get_timeline(requestor: Requestor, twitter_id: int):
    """
    Get the timeline of an account.
    """
    return await twitter.get_user_timeline(user_id=twitter_id)


@check_permission(permission_level=DEVELOPER)
async def is_subscribed(requestor: Requestor, twitter_id: int, channel_id: int):
    """
    Check if a channel is subscribed.
    """
    return await self.db.fetch_row(
        "SELECT public.gettwitterstatus($1, $2)", twitter_id, channel_id
    )
