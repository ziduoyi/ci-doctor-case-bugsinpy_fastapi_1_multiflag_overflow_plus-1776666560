from .route_primitives import Route


class APIRouter:
    def delete(self, omit_defaults=False, omit_none=False):
        return Route(
            "ROUTER_DELETE",
            drop_none=omit_none,
        )
