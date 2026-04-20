from .route_primitives import Route


def make_delete_route(omit_defaults=False, omit_none=False):
    return Route(
        "DELETE",
        drop_defaults=omit_defaults,
    )
