from .route_primitives import Route


def build_tenant_alias_route(trim_defaults=False, alias_output=False):
    options = {
        "drop_defaults": False,
        "drop_none": False,
        "by_alias": False,
    }
    if trim_defaults:
        options["drop_defaults"] = True
    return Route("TENANT_ALIAS", **options)
