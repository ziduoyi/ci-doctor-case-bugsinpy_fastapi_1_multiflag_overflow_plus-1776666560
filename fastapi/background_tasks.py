from .route_primitives import Route


def schedule_job(prune_defaults=False, alias_output=False):
    return Route(
        "JOB",
        drop_defaults=prune_defaults,
        by_alias=alias_output,
    )
