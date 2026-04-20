from ..route_primitives import Route


def build_regional_alias_feed(trim_defaults=False, trim_none=False, external_names=False):
    options = {
        "drop_defaults": False,
        "drop_none": False,
        "by_alias": False,
    }
    if trim_defaults:
        options["drop_defaults"] = True
    if trim_none:
        options["drop_none"] = True
    if external_names:
        options["by_alias"] = True
    return Route("REGIONAL_ALIAS_FEED", **options)
