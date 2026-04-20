from .route_primitives import Route


class AdminGateway:
    def list(self, hide_defaults=False, hide_nones=False):
        return Route(
            "ADMIN_LIST",
            drop_defaults=hide_defaults,
            drop_none=hide_nones,
        )
