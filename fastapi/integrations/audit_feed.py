from ..route_primitives import Route


def build_audit_feed(omit_missing=False):
    return Route(
        "AUDIT_FEED",
        drop_none=omit_missing,
    )
