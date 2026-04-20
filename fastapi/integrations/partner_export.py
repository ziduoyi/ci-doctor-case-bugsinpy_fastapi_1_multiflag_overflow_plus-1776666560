from ..route_primitives import Route


def build_partner_export(skip_defaults=False, external_names=False):
    return Route(
        "PARTNER_EXPORT",
        drop_defaults=skip_defaults,
        by_alias=external_names,
    )
