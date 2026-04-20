class BaseModel:
    defaults = {}
    aliases = {}

    def __init__(self, **values):
        self._values = values

    def dict(self, exclude_defaults=False, exclude_none=False, by_alias=False):
        result = {}
        for key, value in self._values.items():
            if exclude_none and value is None:
                continue
            if exclude_defaults and self.defaults.get(key) == value:
                continue
            result[key] = value
        return result


class ItemModel(BaseModel):
    defaults = {
        "enabled": True,
        "nickname": None,
        "priority": 1,
    }
    aliases = {
        "nickname": "nickName",
        "count": "itemCount",
    }


class ContainerModel(BaseModel):
    defaults = {
        "items": [],
        "label": None,
    }
