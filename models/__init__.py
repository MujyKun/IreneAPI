from .Access import Access
from .Requestor import Requestor
from .DbConn import DbConnection
from .PgConn import PgConnection
from .WebSocketSession import WebSocketSession
from quart_openapi import Pint as PintApp
from quart import Response
from routes import cors_handler
from typing import Optional, Iterable, Callable
from quart.routing import QuartRule


class CustomQuartRule(QuartRule):
    def __init__(
        self,
        string: str,
        defaults: Optional[dict] = None,
        subdomain: Optional[str] = None,
        methods: Optional[Iterable[str]] = None,
        endpoint: Optional[str] = None,
        strict_slashes: Optional[bool] = None,
        merge_slashes: Optional[bool] = None,
        host: Optional[str] = None,
        websocket: bool = False,
        provide_automatic_options: bool = False,
    ) -> None:
        super().__init__(
            string,
            defaults=defaults,
            subdomain=subdomain,
            methods=methods,
            endpoint=endpoint,
            strict_slashes=False,
            merge_slashes=merge_slashes,
            host=host,
            websocket=websocket,
            provide_automatic_options=provide_automatic_options
        )


class Pint(PintApp):
    def __init__(self, *args, **kwargs):
        super(Pint, self).__init__(*args, **kwargs)
        self.url_rule_class = CustomQuartRule

    async def make_default_options_response(self, overwritten=True) -> Response:
        """This is the default route function for OPTIONS requests.

        :param overwritten: bool
            Whether to send the overwritten method's response.
            This is essential as it can avoid infinite recursion.
        """
        from quart.globals import _request_ctx_stack
        methods = _request_ctx_stack.top.url_adapter.allowed_methods()
        if overwritten:
            handler = await cors_handler(self.response_class)
            return await handler("", headers={"Allow": ", ".join(methods)})
        else:
            return self.response_class("", headers={"Allow": ", ".join(methods)})
