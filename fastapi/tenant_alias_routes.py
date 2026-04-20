from .route_primitives import Route


def build_tenant_alias_route(trim_defaults=False, alias_output=False):
    return Route(
        "TENANT_ALIAS",
        drop_defaults=trim_defaults,
        by_alias=alias_output,
    )
