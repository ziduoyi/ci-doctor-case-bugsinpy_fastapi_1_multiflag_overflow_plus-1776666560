from .route_primitives import Route


def schedule_job(prune_defaults=False, alias_output=False):
    return Route(
        "JOB",
        by_alias=False,
    )
