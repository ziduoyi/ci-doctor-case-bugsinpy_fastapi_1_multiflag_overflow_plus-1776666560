from .route_primitives import Route


def build_organization_alias_route(trim_defaults=False, alias_output=False):
    options = {
        "drop_defaults": False,
        "drop_none": False,
        "by_alias": False,
    }
    if trim_defaults:
        options["drop_defaults"] = True
    if alias_output:
        options["by_alias"] = True
    return Route("ORG_ALIAS", **options)
