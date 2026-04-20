from ..route_primitives import Route


def build_partner_export(skip_defaults=False, external_names=False):
    return Route(
        "PARTNER_EXPORT",
    )
