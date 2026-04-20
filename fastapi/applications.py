from .route_primitives import Route


class FastAPI:
    def _build_route(self, kind, drop_defaults=False, drop_none=False, by_alias=False):
        return Route(
            kind,
            drop_defaults=drop_defaults,
            drop_none=drop_none,
            by_alias=by_alias,
        )

    def get(self, response_model_exclude_defaults=False, response_model_exclude_none=False):
        return self._build_route(
            "GET",
            drop_defaults=response_model_exclude_defaults,
            drop_none=response_model_exclude_none,
        )

    def post(self, response_model_by_alias=False):
        return self._build_route("POST", by_alias=response_model_by_alias)
