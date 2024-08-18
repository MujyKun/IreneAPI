import asyncio
import datetime
import random
from typing import Optional, List, Dict, Tuple

from datetime import datetime, timedelta
import json
import aiofiles
import io
from dataclasses import dataclass

import aiohttp
from PIL import Image
from .keys import discord_redirect_uri


class Discord:
    """Handle communication from/to discord."""
    def __init__(self):
        self.version = 10
        self.session = aiohttp.ClientSession()
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        self._base_url = 'https://discord.com/api'
        self.token_url = f'{self._base_url}/oauth2/token'
        self.user_url = f'{self._base_url}/users/@me'

    @property
    def client_id(self):
        from .keys import discord_client_id
        return discord_client_id

    @property
    def client_secret(self):
        from .keys import discord_client_secret
        return discord_client_secret

    async def fetch_user_token(self, code: str):
        """
        Fetch the user's token

        :param code: str
            Code provided from discord.
        :return: Tuple[str, Optional[datetime], str, str]
            access_token, expires_at, refresh_token, scope
        """
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': discord_redirect_uri
        }

        async with self.session.post(self.token_url, data=data, headers=self.headers) as resp:
            response_data = await resp.json()
            return self.get_credentials(response_data)

    @staticmethod
    def get_credentials(response_data) -> Tuple[str, Optional[datetime], str, str]:
        """
        Parse and return the discord credentials

        :param response_data:
            Response directly from discord's api.
        :return: Tuple[str, Optional[datetime], str, str]
            access_token, expires_at, refresh_token, scope
        """
        access_token = response_data.get('access_token')
        expires_in = response_data.get('expires_in')
        refresh_token = response_data.get('refresh_token')
        scope = response_data.get('scope')
        expires_at = None
        if expires_in:
            expires_at = datetime.utcnow() + timedelta(seconds=expires_in - 10)

        return access_token, expires_at, refresh_token, scope

    async def refresh_access_token(self, refresh_token):
        """Refresh the access token."""
        data = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        async with self.session.post(self.token_url, data=data, headers=self.headers) as resp:
            token_data = await resp.json()
            return self.get_credentials(token_data)

    async def get_user(self, access_token):
        """Get the user's information"""
        headers = self.headers.copy()
        headers['Authorization'] = f"Bearer {access_token}"
        async with self.session.get(self.user_url, headers=headers) as resp:
            user_info = await resp.json()
            return user_info
