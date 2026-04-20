from .route_primitives import Route


def build_put_route(skip_defaults=False, skip_missing=False):
    return Route(
        "PUT",
        drop_none=skip_missing,
    )
