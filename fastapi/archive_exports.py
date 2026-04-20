from .route_primitives import Route


def build_archive_export(omit_defaults=False, omit_none=False):
    options = {
        "drop_defaults": False,
        "drop_none": False,
        "by_alias": False,
    }
    if omit_defaults:
        options["drop_defaults"] = True
    if omit_none:
        options["drop_none"] = True
    return Route("ARCHIVE_EXPORT", **options)
