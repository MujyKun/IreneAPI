import asyncio
from typing import Union

from quart import Blueprint, request
from quart_openapi import PintBlueprint, Resource
from . import login
import routes.helpers.groupmembers as helper
import routes.helpers.api as api_helper
from models import Requestor
from .helpers import BadRequest, is_int64, USER, GOD

person = PintBlueprint("person", __name__, url_prefix="/person/")


@person.route("<int:person_id>")
@person.doc(
    params={
        "person_id": "Person ID to manage.",
    }
)
class Person(Resource):
    async def get(self, person_id: int):
        """Get a person.

        Use this route to get a person.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_person(requestor, person_id)

    async def post(self, person_id: int):
        """Add a person.

        Use this route to add a person.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.add_person(requestor, person_id)

    async def delete(self, person_id: int):
        """Delete a person.

        Use this route to delete a person. This will cascade all objects dependent on the person and is not reversible.
        Use with caution.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.delete_person(requestor, person_id)


@person.route("")
@person.doc()
class Persons(Resource):
    async def get(self):
        """Get all persons.

        Use this route to get all persons.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_persons(requestor)


@person.route("<int:person_id>/media")
@person.doc(
    params={
        "person_id": "Person ID to get media information for.",
    }
)
class PersonMedia(Resource):
    async def get(self, person_id: int):
        """Get a list of media information that belong to a Person.

        Use this route to get a list of media information that belong to a Person.
        """
        requestor = await login(headers=request.headers, data=request.args)
        return await helper.get_person_media_info(requestor, person_id)

    async def post(self, person_id: int):
        """Generate random person media that can be filtered.

        Use this route to generate random person media that can be filtered.

        """
        requestor = await login(headers=request.headers, data=request.args)
        kwargs = helper.get_media_kwargs(requestor, request.args)
        kwargs["person_id"] = person_id
        return await helper.generate_media_person(**kwargs)
