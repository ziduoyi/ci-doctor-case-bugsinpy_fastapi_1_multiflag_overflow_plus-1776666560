from .route_primitives import Route


def build_webhook(strip_defaults=False, strip_none=False, use_aliases=False):
    options = {
        "drop_defaults": False,
        "drop_none": False,
        "by_alias": False,
    }
    if strip_none:
        options["drop_none"] = True
    return Route("WEBHOOK", **options)
