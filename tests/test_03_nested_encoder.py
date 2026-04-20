from fastapi import ContainerModel, ItemModel
from fastapi.encoders import jsonable_encoder


def test_nested_encoder_excludes_defaults_and_none() -> None:
    container = ContainerModel(
        label=None,
        items=[
            ItemModel(enabled=True, nickname=None, priority=1, count=2),
            ItemModel(enabled=False, nickname="x", priority=3, count=4),
        ],
    )
    payload = jsonable_encoder(container, drop_defaults=True, drop_none=True)
    assert payload == {
        "items": [
            {"count": 2},
            {"enabled": False, "nickname": "x", "priority": 3, "count": 4},
        ]
    }
