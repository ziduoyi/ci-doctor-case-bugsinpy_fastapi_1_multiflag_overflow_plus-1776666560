from .route_primitives import Route


def build_streaming_export(omit_defaults=False, omit_none=False):
    return Route(
        "STREAM_EXPORT",
        drop_defaults=omit_defaults,
        drop_none=omit_none,
    )
