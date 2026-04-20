from .models import BaseModel


def jsonable_encoder(obj, drop_defaults=False, drop_none=False, by_alias=False):
    if isinstance(obj, BaseModel):
        obj_dict = obj.dict(
            exclude_defaults=drop_defaults,
            exclude_none=drop_none,
            by_alias=by_alias,
        )
        return jsonable_encoder(
            obj_dict,
            drop_defaults=drop_defaults,
            drop_none=drop_none,
            by_alias=by_alias,
        )

    if isinstance(obj, dict):
        encoded = {}
        for key, value in obj.items():
            if value is None and drop_none:
                continue
            encoded[key] = jsonable_encoder(value)
        return encoded

    if isinstance(obj, list):
        return [jsonable_encoder(item) for item in obj]

    if isinstance(obj, tuple):
        return [jsonable_encoder(item) for item in obj]

    return obj
