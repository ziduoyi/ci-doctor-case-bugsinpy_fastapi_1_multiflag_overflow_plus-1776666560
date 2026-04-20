from .route_primitives import Route


def build_webhook(strip_defaults=False, strip_none=False, use_aliases=False):
    return Route(
        "WEBHOOK",
        drop_defaults=strip_defaults,
        drop_none=strip_none,
        by_alias=use_aliases,
    )
