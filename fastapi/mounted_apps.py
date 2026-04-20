from .route_primitives import Route


class MountedApp:
    def patch(self, trim_defaults=False, trim_none=False):
        return Route(
            "PATCH",
            drop_defaults=trim_defaults,
        )
