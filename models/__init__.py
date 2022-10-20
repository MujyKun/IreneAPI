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
    #
    # def add_url_rule(
    #     self,
    #     rule: str,
    #     endpoint: Optional[str] = None,
    #     view_func: Optional[Callable] = None,
    #     provide_automatic_options: Optional[bool] = None,
    #     *,
    #     methods: Optional[Iterable[str]] = None,
    #     defaults: Optional[dict] = None,
    #     host: Optional[str] = None,
    #     subdomain: Optional[str] = None,
    #     is_websocket: bool = False,
    #     strict_slashes: Optional[bool] = None,
    #     merge_slashes: Optional[bool] = None,
    # ) -> None:
    #     """Add a route/url rule to the application.
    #
    #     This is designed to be used on the application directly. An
    #     example usage,
    #
    #     .. code-block:: python
    #
    #         def route():
    #             ...
    #
    #         app.add_url_rule('/', route)
    #
    #     Arguments:
    #         rule: The path to route on, should start with a ``/``.
    #         endpoint: Optional endpoint name, if not present the
    #             function name is used.
    #         view_func: Callable that returns a response.
    #         provide_automatic_options: Optionally False to prevent
    #             OPTION handling.
    #         methods: List of HTTP verbs the function routes.
    #         defaults: A dictionary of variables to provide automatically, use
    #             to provide a simpler default path for a route, e.g. to allow
    #             for ``/book`` rather than ``/book/0``,
    #
    #             .. code-block:: python
    #
    #                 @app.route('/book', defaults={'page': 0})
    #                 @app.route('/book/<int:page>')
    #                 def book(page):
    #                     ...
    #
    #         host: The full host name for this route (should include subdomain
    #             if needed) - cannot be used with subdomain.
    #         subdomain: A subdomain for this specific route.
    #         strict_slashes: Strictly match the trailing slash present in the
    #             path. Will redirect a leaf (no slash) to a branch (with slash).
    #         is_websocket: Whether or not the view_func is a websocket.
    #         merge_slashes: Merge consecutive slashes to a single slash (unless
    #             as part of the path variable).
    #     """
    #     from quart.globals import _request_ctx_stack
    #     endpoint = endpoint or _endpoint_from_view_func(view_func)
    #     if methods is None:
    #         methods = getattr(view_func, "methods", ["GET"])
    #
    #     methods = cast(Set[str], set(methods))
    #     required_methods = set(getattr(view_func, "required_methods", set()))
    #
    #     if provide_automatic_options is None:
    #         automatic_options = getattr(view_func, "provide_automatic_options", None)
    #         if automatic_options is None:
    #             automatic_options = "OPTIONS" not in methods
    #     else:
    #         automatic_options = provide_automatic_options
    #
    #     if automatic_options:
    #         required_methods.add("OPTIONS")
    #
    #     methods.update(required_methods)
    #
    #     rule = self.url_rule_class(
    #         rule,
    #         methods=methods,
    #         endpoint=endpoint,
    #         host=host,
    #         subdomain=subdomain,
    #         defaults=defaults,
    #         websocket=is_websocket,
    #         strict_slashes=strict_slashes,
    #         merge_slashes=merge_slashes,
    #         provide_automatic_options=automatic_options,
    #     )
    #     self.url_map.add(rule)
    #
    #     if view_func is not None:
    #         old_view_func = self.view_functions.get(endpoint)
    #         if old_view_func is not None and old_view_func != view_func:
    #             raise AssertionError(f"Handler is overwriting existing for endpoint {endpoint}")
    #
    #         self.view_functions[endpoint] = view_func
