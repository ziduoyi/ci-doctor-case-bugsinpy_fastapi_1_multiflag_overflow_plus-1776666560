from .encoders import jsonable_encoder


class Route:
    def __init__(self, kind, drop_defaults=False, drop_none=False, by_alias=False):
        self.kind = kind
        self.drop_defaults = drop_defaults
        self.drop_none = drop_none
        self.by_alias = by_alias

    def render(self, model):
        return jsonable_encoder(
            model,
            drop_defaults=self.drop_defaults,
            drop_none=self.drop_none,
            by_alias=self.by_alias,
        )
